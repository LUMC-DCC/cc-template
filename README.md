# Cookiecutter Multi-Language Template

⚠️ ***This project is under active development***

This repository provides a multi-language project template for use with 
[cookiecutter](https://cookiecutter.readthedocs.io/). 
It supports different languages (e.g., Python, R) in subdirectories, using a single shared `cookiecutter.json` and shared hooks for consistent project creation.

- `_shared/` contains the shared `cookiecutter.json` and post-generation hooks.
- Each language directory (`python`, `r`, etc.) contains the actual template files.

## How to use locally

Use the `--directory` option to select the language-specific subdirectory:

```bash
cookiecutter https://github.com/LUMC-DCC/cc-template.git --directory="python"
```

This will generate the template in a new folder named my-cool-project, substituting the provided context variables.

## How to use with API

This template is designed to work seamlessly with the [Cookiecutter SMP API](https://github.com/LUMC-DCC/cookiecutter-smp-api), 
which accepts a JSON file containing the context and the language field to determine which subdirectory to use.

Example JSON context can be found in [example_input.json](example_input.json).

---

## License
This project is licensed under the Apache 2.0. See the [LICENSE](LICENSE.txt) file for details.
