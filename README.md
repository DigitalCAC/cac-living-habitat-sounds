# Chicago's Living Habitat — Soundscape QR Pages

Mobile-friendly web pages for the *Chicago's Living Habitat* exhibit at the Chicago Architecture Center. Each page presents one ecosystem soundscape with an audio player, description, and species list. Visitors scan a QR code at each exhibit station and listen on their own device with headphones.

**Cost: $0.** Hosted free on GitHub Pages.

---

## What's in this folder

```
cac-living-habitat-sounds/
├── index.html              # Landing page with all five (good for take-home)
├── studio-gang.html        # Five ecosystem pages
├── northerly-island.html
├── midewin.html
├── big-marsh.html
├── salt-creek-woods.html
├── styles.css              # Shared styling for all pages
├── audio/                  # The five MP3 files
├── qr-codes/               # Generated QR PNGs (created by the script)
├── generate_qr.py          # Script to generate print-ready QR codes
└── README.md               # This file
```

---

## Setup (one-time, ~15 minutes)

### 1. Sign in as DigitalCAC and create the repo inside the org

1. Go to [github.com](https://github.com) and sign in as `DigitalCAC`.
2. Click the **+** in the top-right and select **New repository**.
3. **Owner:** select `chicago-architecture-center` from the dropdown (NOT your personal account).
4. Repository name: `cac-living-habitat-sounds`
5. Visibility: **Public** (required for free GitHub Pages).
6. Click **Create repository**.

### 2. Upload the files

The easiest path: drag and drop in the browser.

1. On the new empty repo page, click **uploading an existing file**.
2. Drag the entire contents of this folder (all files and the `audio/` folder) into the upload area.
3. Wait for the upload to finish — the audio files are ~1MB each.
4. Scroll down, click **Commit changes**.

### 3. Enable GitHub Pages

1. In the repo, go to **Settings** → **Pages** (left sidebar).
2. Under **Source**, select **Deploy from a branch**.
3. Branch: `main`, folder: `/ (root)`.
4. Click **Save**.
5. Wait 1–2 minutes. Refresh the Pages settings — you'll see a green box with the live URL:
   ```
   https://chicago-architecture-center.github.io/cac-living-habitat-sounds/
   ```

### 4. Test it

Open the URL above on your phone. You should see the index page with all five ecosystems. Test each:

- `https://chicago-architecture-center.github.io/cac-living-habitat-sounds/studio-gang.html`
- `https://chicago-architecture-center.github.io/cac-living-habitat-sounds/northerly-island.html`
- `https://chicago-architecture-center.github.io/cac-living-habitat-sounds/midewin.html`
- `https://chicago-architecture-center.github.io/cac-living-habitat-sounds/big-marsh.html`
- `https://chicago-architecture-center.github.io/cac-living-habitat-sounds/salt-creek-woods.html`

### 5. Generate the QR codes

1. Open `generate_qr.py` and confirm this line:
   ```python
   GITHUB_USERNAME = "chicago-architecture-center"
   ```

2. Install the `qrcode` library (one-time):
   ```
   pip install qrcode[pil]
   ```

3. Run the script:
   ```
   python generate_qr.py
   ```

4. Six PNG files will appear in `qr-codes/`:
   - `studio-gang-qr.png`
   - `northerly-island-qr.png`
   - `midewin-qr.png`
   - `big-marsh-qr.png`
   - `salt-creek-woods-qr.png`
   - `index-qr.png` (bonus — links to all five, useful for press or marketing)

The QR codes are 1200×1200 pixels, suitable for printing at any reasonable exhibit-graphic size, and use high error correction (30%) so they still scan if a corner gets scuffed.

---

## Editing pages later

All five pages share `styles.css` — change colors or fonts there once and every page updates.

To edit text on a single page: open the matching HTML file in any text editor, change the description or species list, save, and either re-upload through GitHub's web interface or commit via Git.

If you change the page filenames (e.g. rename `salt-creek-woods.html`), you'll need to:
1. Update the link on `index.html`
2. Update the slug in `generate_qr.py`
3. Re-generate that QR code

---

## Troubleshooting

**"Audio doesn't play on iPhone"** — iOS requires a user tap to start audio. The standard play button handles this; visitors just need to actually tap it.

**"QR code goes to a 404"** — GitHub Pages can take 1–2 minutes to publish after a commit. Wait, then refresh.

**"I want a custom domain like sounds.architecture.org"** — GitHub Pages supports custom domains for free. In repo Settings → Pages, add the domain and configure DNS to point a CNAME record at `chicago-architecture-center.github.io`. Coordinate with whoever manages the CAC DNS.

---

## Notes

- Audio files are renamed to clean slugs (`studio-gang.mp3`, etc.) so URLs are easy to type and debug. The original filenames with timestamps are preserved in your source files.
- Pages are mobile-first but work fine on desktop.
- All copy is editable in the HTML files — no build step.
