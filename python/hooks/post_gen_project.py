import os
import shutil


OPTIONAL_PATHS = [
    {
        "path": "docs",
        "condition": "{{ cookiecutter.include_docs }}",
        "expected": "yes",
    },
    {
        "path": "tests",
        "condition": "{{ cookiecutter.include_tests }}",
        "expected": "yes",
    },
    {
        "path": "github",
        "condition": "{{ cookiecutter.using_ci }}",
        "expected": "yes",
    },
    {
        "path": "LICENSE.txt",
        "condition": "{{ cookiecutter.include_license }}",
        "expected": "yes",
    },
]

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
    cwd = os.getcwd()

    # Clean optional
    for entry in OPTIONAL_PATHS:
        condition_val = entry["condition"].strip()
        expected_val = entry["expected"]
        target = os.path.join(cwd, entry["path"])

        if condition_val != expected_val:
            print(f"[INFO] Removing {entry['path']} (condition: {condition_val} != {expected_val})")
            remove_path(target)

    # Clean always-remove
    for rel_path in ALWAYS_REMOVE_PATHS:
        target = os.path.join(cwd, rel_path)
        print(f"[INFO] Removing always-remove path: {rel_path}")
        remove_path(target)


if __name__ == '__main__':
    cleanup()