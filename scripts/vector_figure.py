"""Embed a single-page PDF or self-contained SVG as SVG with a PNG fallback."""

from io import BytesIO
from pathlib import Path
import re

from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.opc.part import Part
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from lxml import etree


SVG_NS = "http://www.w3.org/2000/svg"
ASVG_NS = "http://schemas.microsoft.com/office/drawing/2016/SVG/main"


def validate_svg(data: bytes) -> None:
    """Reject active content and file/network dependencies before rendering."""
    root = etree.fromstring(data, etree.XMLParser(resolve_entities=False, no_network=True))
    tree = root.getroottree()
    if root.tag != f"{{{SVG_NS}}}svg" or tree.docinfo.doctype or tree.xpath("//processing-instruction()"):
        raise ValueError("SVG must be a self-contained static SVG without a DTD or processing instructions")
    for node in root.iter():
        if not isinstance(node.tag, str):
            continue
        if etree.QName(node).localname in {"script", "foreignObject", "animate", "set", "animateTransform", "animateMotion"}:
            raise ValueError("Active SVG content is not supported")
        for key, value in node.attrib.items():
            name = etree.QName(key).localname.lower()
            if name.startswith("on"):
                raise ValueError("SVG event handlers are not supported")
            if name == "href" and not (value.startswith("#") or re.match(r"data:image/(png|jpeg);base64,", value)):
                raise ValueError("SVG references must be local fragments or embedded PNG/JPEG data")
        css = " ".join(node.attrib.values())
        if etree.QName(node).localname == "style":
            css += node.text or ""
        if "@import" in css.lower() or "\\" in css:
            raise ValueError("SVG CSS imports and escaped resource names are not supported")
        for target in re.findall(r"url\s*\((.*?)\)", css, re.IGNORECASE):
            if not target.strip(" \t\r\n\"'").startswith("#"):
                raise ValueError("SVG external resources are not supported")


def vector_assets(path: Path) -> tuple[bytes, bytes]:
    """Return vector SVG bytes and a bounded-resolution compatibility preview."""
    try:
        import pymupdf
    except ImportError as exc:
        raise RuntimeError("PDF/SVG figures require PyMuPDF in this Python environment: python -m pip install PyMuPDF") from exc

    if path.suffix.lower() not in {".pdf", ".svg"}:
        raise ValueError("Expected a PDF or SVG figure")
    data = path.read_bytes()
    if path.suffix.lower() == ".svg":
        validate_svg(data)
    with pymupdf.open(stream=data, filetype=path.suffix[1:].lower()) as source:
        if source.needs_pass or len(source) != 1:
            raise ValueError("Figure must be unencrypted and contain exactly one page; export the desired slide separately")
        page = source[0]
        # Text outlines keep PDF glyphs independent of fonts on the receiving computer.
        svg = page.get_svg_image(text_as_path=True).encode("utf-8") if path.suffix.lower() == ".pdf" else data
        validate_svg(svg)
        scale = min(300 / 72, 2400 / max(page.rect.width, page.rect.height))
        png = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), alpha=True).tobytes("png")
    return svg, png


def add_vector_picture(run, path: Path, width):
    svg, png = vector_assets(path)
    picture = run.add_picture(BytesIO(png), width=width)
    part = run.part
    svg_part = Part(part.package.next_partname("/word/media/vector%d.svg"), "image/svg+xml", svg, part.package)
    svg_id = part.relate_to(svg_part, RT.IMAGE)
    blip = picture._inline.graphic.graphicData.pic.blipFill.blip
    extensions = OxmlElement("a:extLst")
    extension = OxmlElement("a:ext")
    extension.set("uri", "{96DAC541-7B7A-43D3-8B79-37D633B846F1}")
    svg_blip = etree.SubElement(extension, f"{{{ASVG_NS}}}svgBlip", nsmap={"asvg": ASVG_NS})
    svg_blip.set(qn("r:embed"), svg_id)
    extensions.append(extension)
    blip.append(extensions)
    return picture
