"""images_src/*.png → images/{코드}.webp  (실행: uv run --no-project --python 3.12 --with pillow python -I clean_images.py images_src images)

EXIF·PNG 텍스트는 새 이미지로 옮겨 담으며 버리고, NovelAI가 픽셀 끝 비트에 숨긴 생성 정보(stealth_pnginfo 등)는
색 채널 끝 비트를 0, 알파 끝 비트를 1로 고정해 지운다. 저장은 WebP quality 90, method 6, exact."""
import re, sys
from pathlib import Path
from PIL import Image

src_dir, out_dir = Path(sys.argv[1]), Path(sys.argv[2])
out_dir.mkdir(exist_ok=True)
for src in sorted(src_dir.glob("*.png")):
    code = re.match(r"(\d+)\s", src.name).group(1)
    im = Image.open(src).convert("RGBA")
    r, g, b, a = im.split()
    clear = lambda ch: ch.point(lambda v: v & 0xFE)
    a = a.point(lambda v: v | 1 if v else 0)
    clean = Image.merge("RGBA", (clear(r), clear(g), clear(b), a))  # 새 이미지 = info/EXIF 없음
    dst = out_dir / f"{code}.webp"
    clean.save(dst, "WEBP", quality=90, method=6, exact=True)
    print(f"{src.name} -> {dst.name} ({src.stat().st_size//1024}K -> {dst.stat().st_size//1024}K)")
