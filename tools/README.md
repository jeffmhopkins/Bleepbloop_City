# Tools

| Script | Makes |
| --- | --- |
| [`storage_hall_flow.py`](storage_hall_flow.py) | [`assets/storage-hall-flow.png`](../assets/storage-hall-flow.png), the storage hall item-flow diagram |

## Regenerate the storage hall diagram

From the repo root:

```sh
pip install -r tools/requirements.txt && python3 tools/storage_hall_flow.py
```

**Fonts:** the committed PNG was drawn with **DejaVu Sans**, and only DejaVu Sans reproduces it exactly. On non-Linux machines, or anywhere DejaVu Sans is missing, the script still runs (it falls back to Arial/Helvetica on macOS, Arial/Segoe UI on Windows, then Pillow's built-in font), but the text shifts slightly, so the regenerated PNG will differ from the committed one. For an identical render, install the DejaVu fonts first:

- Debian/Ubuntu: `sudo apt install fonts-dejavu-core`
- macOS (Homebrew): `brew install --cask font-dejavu`
- Windows: download from [dejavu-fonts.github.io](https://dejavu-fonts.github.io/) and install `DejaVuSans.ttf` and `DejaVuSans-Bold.ttf` for all users (right-click → "Install for all users") so they land in `C:\Windows\Fonts`

If you change the diagram on purpose, view the new PNG before committing it.
