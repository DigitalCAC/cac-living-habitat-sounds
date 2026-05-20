"""
Chicago's Living Habitat — QR Code Generator

Generates print-ready QR codes for all five ecosystem pages.

USAGE:
1. Install qrcode library:    pip install qrcode[pil]
2. Run:                       python generate_qr.py

QR codes save to qr-codes/ as 1200x1200 PNGs, ready for printing on exhibit graphics.
"""

import qrcode
from pathlib import Path

GITHUB_USERNAME = "DigitalCAC"
REPO_NAME = "cac-living-habitat-sounds"

ECOSYSTEMS = [
    ("studio-gang", "Studio Gang"),
    ("northerly-island", "Northerly Island"),
    ("midewin", "Midewin"),
    ("big-marsh", "Big Marsh"),
    ("salt-creek-woods", "Salt Creek Woods"),
]

BASE_URL = f"https://{GITHUB_USERNAME.lower()}.github.io/{REPO_NAME}"
OUTPUT_DIR = Path(__file__).parent / "qr-codes"
OUTPUT_DIR.mkdir(exist_ok=True)


def generate_qr(url, output_path):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=40,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)


def main():
    print(f"Generating QR codes for {BASE_URL}\n")

    for slug, name in ECOSYSTEMS:
        url = f"{BASE_URL}/{slug}.html"
        output_path = OUTPUT_DIR / f"{slug}-qr.png"
        generate_qr(url, output_path)
        print(f"  {name:25s} -> {output_path.name}")

    index_url = f"{BASE_URL}/"
    generate_qr(index_url, OUTPUT_DIR / "index-qr.png")
    print(f"  {'All five (index)':25s} -> index-qr.png")

    print(f"\nDone. QR codes saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
