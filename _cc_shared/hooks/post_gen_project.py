import os
import shutil
import json


OPTIONAL_PATHS = [
    {
        "path": "docs",
        "should_remove": lambda ctx: ctx.get("include_docs", "").strip().lower() != "yes"
    },
    {
        "path": "tests",
        "should_remove": lambda ctx: ctx.get("include_tests", "").strip().lower() != "yes"
    },
    {
        "path": "github",
        "should_remove": lambda ctx: ctx.get("using_ci", "").strip().lower() != "yes"
    },
    {
        "path": "LICENSE.txt",
        "should_remove": lambda ctx: ctx.get("license", "").strip().lower() in ("none", "", "no")
    },
]

def load_context():
    return {
        "include_docs": "{{ cookiecutter.include_docs }}",
        "include_tests": "{{ cookiecutter.include_tests }}",
        "using_ci": "{{ cookiecutter.using_ci }}",
        "license": "{{ cookiecutter.license }}",
    }

ALWAYS_REMOVE_PATHS = [
    "licenses",
]

def remove_path(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
        print(f"[INFO] Removed {path}")
    else:
        print(f"[SKIP] {path} does not exist")


def cleanup():
    ctx = load_context()
    cwd = os.getcwd()

    for entry in OPTIONAL_PATHS:
        if entry["should_remove"](ctx):
            target = os.path.join(cwd, entry["path"])
            print(f"[INFO] Removing {entry['path']}")
            remove_path(target)

    for rel_path in ALWAYS_REMOVE_PATHS:
        target = os.path.join(cwd, rel_path)
        print(f"[INFO] Removing always-remove path: {rel_path}")
        remove_path(target)


if __name__ == '__main__':
    cleanup()