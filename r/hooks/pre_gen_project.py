import os
import shutil
import json

# Map context variable values to source templates
SHARED_ASSETS = [
    {
        "context_var": "license",  # just the key name
        "expected_values": {
            "MIT": "_assets/licenses/mit.txt",
            "Apache-2.0": "_assets/licenses/apache-2.0.txt",
        },
        "destination": "LICENSE.txt",
    },
]

def copy_assets():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    output_dir = os.getcwd()

    context_raw = os.environ.get("COOKIECUTTER_CONTEXT")
    if context_raw is None:
        print("[ERROR] COOKIECUTTER_CONTEXT not found.")
        return

    context = json.loads(context_raw)

    for asset in SHARED_ASSETS:
        value = context.get(asset["context_var"])
        expected_values = asset["expected_values"]
        rel_src = expected_values.get(value)

        if rel_src:
            src_path = os.path.join(base_dir, rel_src)
            dst_path = os.path.join(output_dir, asset["destination"])

            if os.path.exists(src_path):
                shutil.copyfile(src_path, dst_path)
                print(f"[INFO] Copied {rel_src} → {asset['destination']}")
            else:
                print(f"[WARN] Missing file: {src_path}")
        else:
            print(f"[SKIP] No match for value '{value}' in {list(expected_values.keys())}")

if __name__ == '__main__':
    copy_assets()