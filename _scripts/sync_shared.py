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
    "licenses": "{{cookiecutter.project_slug}}/licenses",
}

# Collect modified paths
MODIFIED_PATHS = []

def sync_path(src: Path, dst: Path):
    if src.is_file():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        MODIFIED_PATHS.append(dst)
    elif src.is_dir():
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        MODIFIED_PATHS.append(dst)
    else:
        print(f"[warning] Unknown source type: {src}")
        return
    print(f"[sync] Synced {src} → {dst}")

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

    for path in MODIFIED_PATHS:
        print(f"[modified]{path}")

if __name__ == "__main__":
    main()