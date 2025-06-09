import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TEMPLATE_DIRS = [
    d for d in ROOT.iterdir()
    if d.is_dir()
    and not d.name.startswith((".", "_"))
    and (d / "{{cookiecutter.project_slug}}").exists()
]

RELATIVE_SYNC_MAP = {
    "hooks": "hooks",
    "cookiecutter.json": "cookiecutter.json",
    "LICENSE.txt": "{{cookiecutter.project_slug}}/LICENSE.txt",
    "licenses": "licenses",
}

def sync_path(src: Path, dst: Path):
    print(f"[sync] Syncing {src} → {dst}")
    if src.is_file():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    elif src.is_dir():
        # Python 3.8+ only
        shutil.copytree(src, dst, dirs_exist_ok=True)
    else:
        print(f"[warning] Unknown source type: {src}")

def main():
    seen = set()
    for template_dir in TEMPLATE_DIRS:
        for rel_src, rel_dst in RELATIVE_SYNC_MAP.items():
            src = ROOT / "_cc_shared" / rel_src
            dst = template_dir / rel_dst
            key = (str(src), str(dst))

            if key in seen:
                continue
            seen.add(key)

            sync_path(src, dst)

if __name__ == "__main__":
    main()