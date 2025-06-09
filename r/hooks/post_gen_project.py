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


def cleanup_optional_paths():
    cwd = os.getcwd()

    for entry in OPTIONAL_PATHS:
        condition_val = entry["condition"].strip()
        expected_val = entry["expected"]
        target = os.path.join(cwd, entry["path"])

        if condition_val != expected_val:
            if os.path.exists(target):
                print(f"[INFO] Removing {entry['path']} (condition: {condition_val} != {expected_val})")
                if os.path.isdir(target):
                    shutil.rmtree(target)
                else:
                    os.remove(target)


if __name__ == '__main__':
    cleanup_optional_paths()