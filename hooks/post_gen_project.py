# #!/usr/bin/env python
# import os
# from pathlib import Path

# PROJECT_DIRECTORY = Path.cwd()


# def remove_path(path):
#     if path.is_file():
#         path.unlink()
#     elif path.is_dir():
#         for f in path.iterdir():
#             remove_path(f)
#         path.rmdir()


# if __name__ == "__main__":

#     if not "{{ cookiecutter }}".lower().startswith("y"):
#         for f in (
#             "{{ cookiecutter }}",
#             "jupyter-config",
#             "MANIFEST.in",
#             "pyproject.toml",
#             "setup.py",
#             "src/{{ cookiecutter }}.ts",
#         ):
#             remove_path(PROJECT_DIRECTORY / f)
#     else:
#         if "-" in "{{ cookiecutter }}":
#             for f in (
#                 "{{ cookiecutter }}",
#                 "jupyter-config/{{ cookiecutter }}.json",
#             ):
#                 absolute_f = PROJECT_DIRECTORY / f
#                 absolute_f.rename(absolute_f.parent / absolute_f.name.replace("-", "_"))
#         if "_" in "{{ cookiecutter }}":
#             for f in ("src/{{ cookiecutter }}.ts", ):
#                 absolute_f = PROJECT_DIRECTORY / f
#                 absolute_f.rename(absolute_f.parent / absolute_f.name.replace("_", ""))

#     if not "{{ cookiecutter }}".lower().startswith("y"):
#         remove_path(PROJECT_DIRECTORY / "binder")
