"""Draft concept diagrams for plans/storage-layout.md.

All dimensions are ESTIMATES (1 unit = 1 block). Regenerate with:
    python tools/storage_diagrams.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Patch

C = {
    "wall": "#7a7a7a",        # cobblestone base / outer wall
    "spruce": "#6b4a2b",      # spruce frame
    "service": "#c9b79c",     # service gap: filters + item stream
    "chest": "#b8862f",       # chest walls
    "aisle": "#e8dcc4",       # retrieval aisle floor (spruce + carpet runner)
    "foyer": "#efe3cf",       # foyer floor
    "gallery": "#7fc8c2",     # golem gallery (glass + copper)
    "input": "#e07b39",       # input barrels / unloader
    "smelter": "#a33b2b",     # smelter
    "lava": "#ff5a1f",        # overflow + lava
    "machine": "#9fa8b3",     # basement machine floor
    "lift": "#5d6d7e",        # dropper lift / router
    "stairs": "#d2b48c",
    "expansion": "#ffffff",
    "roof": "#d9b44a",        # hay bale "thatch"
    "copper": "#c87533",
    "glass": "#bfe6f5",
}

def box(ax, x, y, w, h, color, label=None, hatch=None, ls="-", fs=7, alpha=1.0, tc="black"):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=color, edgecolor="black",
                           linewidth=0.6, hatch=hatch, linestyle=ls, alpha=alpha))
    if label:
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=fs, color=tc, wrap=True)

def floorplan(path):
    fig, axes = plt.subplots(1, 2, figsize=(13, 10))
    W = 13
    for ax, title in zip(axes, ["Level 1 (ground): foyer, golem gallery, browsing hall",
                                "Level 0 (basement): machines"]):
        ax.set_title(title, fontsize=10)
        ax.set_xlim(-1, W + 7); ax.set_ylim(-2, 58); ax.set_aspect("equal")
        ax.set_xlabel("blocks (W → E)"); ax.set_ylabel("blocks (S → N)")
        # outer wall built part + expansion
        box(ax, 0, 0, W, 33, C["wall"])
        box(ax, 0, 33, W, 24, C["expansion"], "EXPANSION\n(+24 blocks north,\nsame cross-section)", hatch="//", ls="--", fs=8)

    a = axes[0]
    # foyer
    box(a, 1, 1, 11, 6, C["foyer"])
    box(a, 1, 1, 4, 6, C["gallery"], "GOLEM\nGALLERY\n2 modules\nglass front", fs=7)
    box(a, 5, 1, 3, 6, C["foyer"], "FOYER\nwalk-\nway", fs=7)
    box(a, 8, 1, 4, 3, C["input"], "INPUT\nbarrels +\nbox drop", fs=6.5)
    box(a, 8, 4, 4, 3, C["foyer"], "stairs ↓\n+ non-stack\nreturn chest", fs=6)
    box(a, 5.5, -0.5, 2, 1, C["spruce"], "door", fs=6, tc="white")
    # hall
    box(a, 1, 7, 3, 25, C["service"])
    a.text(2.5, 19.5, "SERVICE GAP (3): filters + item stream", rotation=90, ha="center", va="center", fontsize=7)
    box(a, 4, 7, 1, 25, C["chest"])
    a.text(4.5, 19.5, "CHEST WALL (4 high)", rotation=90, ha="center", va="center", fontsize=6.5)
    box(a, 5, 7, 3, 25, C["aisle"])
    a.text(6.5, 19.5, "BROWSING AISLE (3 wide): carpet runner, item frames on chests", rotation=90, ha="center", va="center", fontsize=7)
    box(a, 8, 7, 1, 25, C["chest"])
    a.text(8.5, 19.5, "CHEST WALL (4 high)", rotation=90, ha="center", va="center", fontsize=6.5)
    box(a, 9, 7, 3, 25, C["service"])
    a.text(10.5, 19.5, "SERVICE GAP (3): filters + item stream", rotation=90, ha="center", va="center", fontsize=7)
    for y in range(7, 33, 6):
        box(a, 4, y, 1, 0.6, C["spruce"]); box(a, 8, y, 1, 0.6, C["spruce"])
    box(a, 5, 31, 3, 1, C["lava"])
    a.annotate("overflow chest\n(drains to lava below)", xy=(6.5, 31.5), xytext=(14.5, 30), fontsize=7, ha="left", arrowprops=dict(arrowstyle="->"))
    a.annotate("spruce log pillars\nevery 6 blocks", xy=(4.5, 13.3), xytext=(14.5, 13), fontsize=7, ha="left", arrowprops=dict(arrowstyle="->"))

    b = axes[1]
    box(b, 1, 1, 11, 31, C["machine"])
    box(b, 8, 4, 4, 3, C["stairs"], "stairs ↑", fs=7)
    box(b, 8, 1, 4, 3, C["lift"], "INPUT LINE\nnon-stack split\n+ box unloader", fs=6)
    box(b, 9, 7, 3, 6, C["lift"], "ROUTER /\nlift up to\nitem stream", fs=6.5, tc="white")
    box(b, 1, 7, 3, 12, C["smelter"], "AUTO\nSMELTER\nblast furnaces\n+ smokers", fs=7, tc="white")
    box(b, 5, 1, 3, 31, "#d5d9de", "MAINTENANCE WALKWAY (3)", fs=7)
    b.texts[-1].set_rotation(90)
    box(b, 9, 25, 3, 7, C["lava"], "OVERFLOW\n+ LAVA\n(sealed,\nno wood)", fs=6.5)
    box(b, 1, 19, 3, 13, C["machine"], "spare /\nbulk\noverflow\nchests", fs=6.5)
    box(b, 9, 13, 3, 12, C["machine"], "filter\nunderside /\nexpansion", fs=6.5)
    box(b, 1, 1, 4, 6, C["machine"], "under\ngallery:\nsolid\n(keep golems\nsealed)", fs=6)

    legend = [Patch(facecolor=C[k], edgecolor="black", label=l) for k, l in [
        ("gallery", "Golem gallery (glass + waxed copper)"), ("foyer", "Foyer"),
        ("input", "Input (barrels, shulker box drop)"), ("aisle", "Browsing aisle"),
        ("chest", "Chest walls (labeled with item frames)"), ("service", "Service gap: filters + item stream"),
        ("lift", "Router / lift / input processing"), ("smelter", "Auto smelter"),
        ("lava", "Overflow + lava"), ("machine", "Basement machine floor"),
        ("wall", "Outer wall (cobble base)"), ("expansion", "Expansion (reserved)")]]
    fig.legend(handles=legend, loc="lower center", ncol=4, fontsize=8, frameon=False)
    fig.suptitle("Bleepbloop City storage hall: DRAFT concept floor plan (all dimensions are estimates, 1 square = 1 block)", fontsize=11)
    fig.tight_layout(rect=(0, 0.07, 1, 0.96))
    fig.savefig(path, dpi=130)
    plt.close(fig)

def section(path):
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(-1, 14); ax.set_ylim(-8, 13); ax.set_aspect("equal")
    ax.set_title("Cross-section through the browsing hall, looking north. DRAFT concept, all dimensions are estimates", fontsize=10)
    ax.set_xlabel("blocks (W → E)"); ax.set_ylabel("height (blocks, 0 = ground floor)")
    # ground
    box(ax, -1, -8, 15, 1, "#5b4636")
    # basement
    box(ax, 0, -7, 13, 1, C["wall"])                     # basement floor
    box(ax, 0, -6, 1, 6, C["wall"]); box(ax, 12, -6, 1, 6, C["wall"])
    box(ax, 1, -6, 3, 5, C["smelter"], "smelter row\n(furnace array)", fs=7, tc="white")
    box(ax, 4, -6, 5, 5, "#d5d9de", "maintenance walkway", fs=7)
    box(ax, 9, -6, 3, 5, C["lift"], "router / lift\n(dropper elevator)", fs=7, tc="white")
    box(ax, 1, -1, 11, 1, C["wall"], "floor / basement ceiling (cobble + spruce)", fs=6.5)
    # ground floor
    box(ax, 0, 0, 1, 7, C["wall"]); box(ax, 12, 0, 1, 7, C["wall"])
    box(ax, 0, 0, 1, 2, "#5f5f5f"); box(ax, 12, 0, 1, 2, "#5f5f5f")
    box(ax, 1, 0, 3, 4, C["service"], "filters\n(hoppers +\ncomparators)", fs=7)
    box(ax, 9, 0, 3, 4, C["service"], "filters\n(hoppers +\ncomparators)", fs=7)
    box(ax, 1, 4, 3, 1, "#6fa8dc", "item stream (water/ice)", fs=6)
    box(ax, 9, 4, 3, 1, "#6fa8dc", "item stream (water/ice)", fs=6)
    for z in range(4):
        box(ax, 4, z, 1, 1, C["chest"], "chest", fs=5.5)
        box(ax, 8, z, 1, 1, C["chest"], "chest", fs=5.5)
        ax.add_patch(Rectangle((5, z + 0.3), 0.15, 0.4, color="#333"))
        ax.add_patch(Rectangle((7.85, z + 0.3), 0.15, 0.4, color="#333"))
    box(ax, 4, 4, 1, 1, C["spruce"], "stair\ntrim", fs=5, tc="white")
    box(ax, 8, 4, 1, 1, C["spruce"], "stair\ntrim", fs=5, tc="white")
    box(ax, 5, 0, 3, 0.15, C["input"])
    ax.text(6.5, 0.45, "carpet runner", ha="center", fontsize=6)
    box(ax, 5, 0.6, 3, 5.4, "#fbf6ec", "BROWSING AISLE\n3 wide, 6 high\n(item frames on\nchest faces)", fs=7.5, alpha=0.7)
    box(ax, 1, 5, 11, 1, "#fbf6ec", alpha=0.3)
    box(ax, 0, 6, 13, 1, C["spruce"], "spruce ceiling + copper beams (waxed)", fs=6.5, tc="white")
    ax.add_patch(Rectangle((6.3, 4.6), 0.4, 0.6, color=C["copper"])); ax.text(7.0, 4.9, "copper lantern", fontsize=6)
    # roof
    ax.add_patch(Polygon([[-0.5, 7], [6.5, 11.5], [13.5, 7]], closed=True, facecolor=C["roof"], edgecolor="black"))
    ax.text(6.5, 8.6, "hay-bale \"thatch\" roof on spruce stairs (style choice)", ha="center", fontsize=7)
    legend = [Patch(facecolor=c, edgecolor="black", label=l) for c, l in [
        (C["chest"], "Chests (4 high, octa-style slice)"), (C["service"], "Service gap: filters"),
        ("#6fa8dc", "Item stream"), (C["wall"], "Cobblestone"), (C["spruce"], "Spruce"),
        (C["roof"], "Hay bale thatch"), (C["copper"], "Waxed copper accents"),
        (C["smelter"], "Smelter"), (C["lift"], "Router / lift"), ("#d5d9de", "Walkway")]]
    fig.legend(handles=legend, loc="lower center", fontsize=8, ncol=5, frameon=False)
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    fig.savefig(path, dpi=130)
    plt.close(fig)

if __name__ == "__main__":
    import os, shutil
    here = os.path.dirname(os.path.abspath(__file__))
    assets = os.path.join(here, "..", "assets")
    os.makedirs(assets, exist_ok=True)
    fp = os.path.join(assets, "storage-floorplan.png")
    sc = os.path.join(assets, "storage-section.png")
    floorplan(fp); section(sc)
    print("wrote", fp, sc)
