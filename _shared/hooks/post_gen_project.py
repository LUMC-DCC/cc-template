import os
import shutil


# all optional paths and their controlling cookiecutter variables
OPTIONAL_PATHS = [
    {
        "path": "docs",
        "condition": "{{ cookiecutter.include_docs }}",
        "expected": "yes"
    },
    {
        "path": "tests",
        "condition": "{{ cookiecutter.include_tests }}",
        "expected": "yes"
    },
    {
        "path": "github",
        "condition": "{{ cookiecutter.using_ci }}",
        "expected": "yes"
    },
    {
        "path": "LICENSE.txt",
        "condition": "{{ cookiecutter.include_license }}",
        "expected": "yes"
    },
]


def cleanup_optional_paths():
    cwd = os.getcwd()

    for entry in OPTIONAL_PATHS:
        condition = entry["condition"].strip()
        expected = entry["expected"]
        target_path = os.path.join(cwd, entry["path"])

        if condition != expected and os.path.exists(target_path):
            print(f"Removing {entry['path']} (condition: {condition} != {expected})")
            if os.path.isdir(target_path):
                shutil.rmtree(target_path)
            else:
                os.remove(target_path)


if __name__ == '__main__':
    cleanup_optional_paths()