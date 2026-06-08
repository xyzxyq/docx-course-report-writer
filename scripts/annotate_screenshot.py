#!/usr/bin/env python3
"""Annotate real screenshots with jittered red boxes and transparent red labels."""

from __future__ import annotations

import argparse
import random
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


RED = (220, 0, 0)


def parse_box(spec: str) -> tuple[str, int, int, int, int]:
    match = re.match(r"^(.+?):\s*(-?\d+),\s*(-?\d+),\s*(\d+),\s*(\d+)$", spec)
    if not match:
        raise ValueError(f"Invalid --box format: {spec!r}. Use label:x,y,w,h")
    label = match.group(1).strip()
    x, y, w, h = map(int, match.groups()[1:])
    if not label:
        raise ValueError("Box label must not be empty.")
    if len(label) > 10:
        raise ValueError(f"Box label exceeds 10 characters: {label}")
    if w <= 0 or h <= 0:
        raise ValueError(f"Box width/height must be positive: {spec}")
    return label, x, y, w, h


def load_font(size: int) -> ImageFont.ImageFont:
    candidates = [
        r"C:\Windows\Fonts\msyh.ttc",
        r"C:\Windows\Fonts\simhei.ttf",
        r"C:\Windows\Fonts\simsun.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            try:
                return ImageFont.truetype(str(path), size=size)
            except OSError:
                continue
    return ImageFont.load_default()


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def clamp_box(x: int, y: int, w: int, h: int, image_w: int, image_h: int) -> tuple[int, int, int, int]:
    x = max(0, min(x, image_w - 1))
    y = max(0, min(y, image_h - 1))
    w = max(1, min(w, image_w - x))
    h = max(1, min(h, image_h - y))
    return x, y, w, h


def jittered_line_points(
    start: tuple[int, int],
    end: tuple[int, int],
    rng: random.Random,
    segments: int = 9,
    jitter: int = 3,
) -> list[tuple[int, int]]:
    points: list[tuple[int, int]] = []
    sx, sy = start
    ex, ey = end
    for i in range(segments + 1):
        t = i / segments
        x = round(sx + (ex - sx) * t)
        y = round(sy + (ey - sy) * t)
        if 0 < i < segments:
            x += rng.randint(-jitter, jitter)
            y += rng.randint(-jitter, jitter)
        points.append((x, y))
    return points


def draw_jittered_rect(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], rng: random.Random) -> None:
    x, y, w, h = box
    pad_l = rng.randint(-3, 4)
    pad_t = rng.randint(-3, 4)
    pad_r = rng.randint(-4, 3)
    pad_b = rng.randint(-4, 3)
    left = x + pad_l
    top = y + pad_t
    right = x + w + pad_r
    bottom = y + h + pad_b
    corners = [(left, top), (right, top), (right, bottom), (left, bottom)]
    for start, end in zip(corners, corners[1:] + corners[:1]):
        width = rng.choice([3, 3, 4])
        draw.line(jittered_line_points(start, end, rng), fill=RED, width=width, joint="curve")


def label_position(
    x: int,
    y: int,
    w: int,
    h: int,
    tw: int,
    th: int,
    image_w: int,
    image_h: int,
) -> tuple[int, int]:
    margin = 6
    candidates = [
        (x + w + margin, y),
        (x, y - th - margin),
        (x, y + h + margin),
        (x + margin, y + margin),
        (x - tw - margin, y),
    ]
    for lx, ly in candidates:
        if 0 <= lx and 0 <= ly and lx + tw <= image_w and ly + th <= image_h:
            return lx, ly
    return max(0, min(x, image_w - tw)), max(0, min(y, image_h - th))


def annotate(input_path: Path, output_path: Path, box_specs: list[str], seed: str | None, font_size: int) -> None:
    image = Image.open(input_path).convert("RGB")
    draw = ImageDraw.Draw(image)
    font = load_font(font_size)
    rng = random.Random(seed or str(input_path.resolve()))
    image_w, image_h = image.size

    for spec in box_specs:
        label, x, y, w, h = parse_box(spec)
        x, y, w, h = clamp_box(x, y, w, h, image_w, image_h)
        draw_jittered_rect(draw, (x, y, w, h), rng)
        tw, th = text_size(draw, label, font)
        lx, ly = label_position(x, y, w, h, tw, th, image_w, image_h)
        if lx + tw > image_w or ly + th > image_h:
            raise ValueError(f"Label out of bounds after clamping: {label}")
        draw.text((lx, ly), label, fill=RED, font=font)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Add jittered red boxes and transparent red labels to a screenshot.")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--box", action="append", required=True, help="label:x,y,w,h")
    parser.add_argument("--seed", default=None)
    parser.add_argument("--font-size", type=int, default=28)
    args = parser.parse_args()
    annotate(args.input, args.output, args.box, args.seed, args.font_size)
    print(f"Annotated screenshot written to: {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
