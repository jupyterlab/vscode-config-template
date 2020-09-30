# JupyterLab debug-config-cookiecutter

A [cookiecutter](https://github.com/audreyr/cookiecutter) template for creating the IDE config needed to debug the Python and Typescript code in Jupyter projects. Works with both JupyterLab core and any extension.

Currently only supports vscode. PRs for setting up other debug tools/techniques are welcome.

## Setup vscode debugging for any Jupyter project

Install cookiecutter.

```bash
pip install cookiecutter
```

Navigate to the root of your Jupyter project, then run

```bash
cookiecutter gh:jupyterlab/debug-config-cookiecutter
```

A number of prompts will pop up. DO NOT CHANGE `vscode_config_path`. Answer the rest of the prompts as appropriate for your project

## Troubleshooting

- `Error: ".vscode" directory already exists`: you'll need to delete the existing `.vscode` dir at your project's root. You can force cookiecutter to overwrite the existing dir with:

  ```bash
  cookiecutter gh:jupyterlab/debug-config-cookiecutter -f
  ```
