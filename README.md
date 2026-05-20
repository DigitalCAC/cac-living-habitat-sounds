# Chicago's Living Habitat — Soundscape QR Pages

Mobile-friendly web pages for the *Chicago's Living Habitat* exhibit at the Chicago Architecture Center. Each page presents one ecosystem soundscape with an audio player, description, and species list.

**Hosted free on GitHub Pages.** Brand-aligned to CAC 2023 Brand Style Guide.

---

## Structure

```
cac-living-habitat-sounds/
├── index.html              # Landing page with all five
├── studio-gang.html
├── northerly-island.html
├── midewin.html
├── big-marsh.html
├── salt-creek-woods.html
├── styles.css              # Brand-aligned styling
├── audio/                  # MP3 files
├── img/                    # CAC logo files
│   ├── cac-logo-black.png  # For light backgrounds (brand bar)
│   └── cac-logo-white.png  # For dark backgrounds (footer)
├── qr-codes/               # Generated QR PNGs
├── generate_qr.py
└── README.md
```

---

## Brand assets

- **Fonts:** Franklin Gothic Condensed + Avenir Next, loaded via Adobe Fonts (Typekit)
- **Red:** `#cc0000`
- **Logo:** CAC C-bug, black version on light backgrounds, white version on dark
- **Typography rules:** Headlines in Franklin Gothic Condensed caps; body in Avenir Next; emphasis via color (red), never typeface change

---

## Editing pages

All pages share `styles.css`. Edit text in the individual HTML files using GitHub's web editor or any text editor.

For copy edits: each ecosystem page has three sections — `About this place`, `What you're hearing`, and `Listen for`. Use `<span class="highlight">word</span>` for red emphasis (per brand guide, color is the emphasis tool, not italics).

---

## Generating QR codes

```bash
pip install qrcode[pil]
python generate_qr.py
```

Six PNG files will appear in `qr-codes/`, one per ecosystem plus a bonus index page QR.
