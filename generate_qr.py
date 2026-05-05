"""
Chicago's Living Habitat — QR Code Generator

Generates print-ready QR codes for all five ecosystem pages.

USAGE:
1. Confirm GITHUB_USERNAME below matches the GitHub account hosting the repo.
   - If using a CAC organization account, this should be the org name (e.g. "DigitalCAC").
   - If you renamed the repo, update REPO_NAME too.
2. Install qrcode library:    pip install qrcode[pil]
3. Run:                       python generate_qr.py

QR codes save to qr-codes/ as 1200x1200 PNGs, ready for printing on exhibit graphics.
"""

import qrcode
from pathlib import Path

# === EDIT IF NEEDED ===
GITHUB_USERNAME = "chicago-architecture-center"
REPO_NAME = "cac-living-habitat-sounds"
# ======================

ECOSYSTEMS = [
    ("studio-gang", "Studio Gang"),
    ("northerly-island", "Northerly Island"),
    ("midewin", "Midewin"),
    ("big-marsh", "Big Marsh"),
    ("salt-creek-woods", "Salt Creek Woods"),
]

# GitHub Pages URLs are case-sensitive in their path but org names are lowercased
BASE_URL = f"https://{GITHUB_USERNAME.lower()}.github.io/{REPO_NAME}"
OUTPUT_DIR = Path(__file__).parent / "qr-codes"
OUTPUT_DIR.mkdir(exist_ok=True)


def generate_qr(url, output_path):
    """Generate a high-resolution QR code with strong error correction."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 30% error tolerance
        box_size=40,                                         # ~1200px output
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
        print(f"  {'':25s}    {url}\n")

    # Bonus: a QR for the index page (useful for press, marketing, etc.)
    index_url = f"{BASE_URL}/"
    generate_qr(index_url, OUTPUT_DIR / "index-qr.png")
    print(f"  {'All five (index)':25s} -> index-qr.png")
    print(f"  {'':25s}    {index_url}\n")

    print(f"Done. QR codes saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
