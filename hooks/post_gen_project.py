#!/usr/bin/env python
import json
import os
import shutil
import sys
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()

def update_package_json():
    try:
        pkg_config = {}
        pkg_config_path = PROJECT_DIRECTORY.parent / 'package.json'
        
        with open(pkg_config_path, 'r', encoding='utf-8') as f:
            pkg_config = json.load(f)
        
        # Add webpack config
        jlab_config = pkg_config.get("jupyterlab")
        if "webpackConfig" not in jlab_config:
            jlab_config["webpackConfig"] = "webpack.config.js"
            pkg_config["jupyterlab"] = jlab_config

        # Add source-map-loader
        dev_dependencies = pkg_config.get("devDependencies")
        if "source-map-loader" not in dev_dependencies:
            dev_dependencies["source-map-loader"] = "^3.0.1"
            pkg_config["devDependencies"] = dev_dependencies
        
        with open(pkg_config_path, 'w') as f:
            json.dump(pkg_config, f, indent=2)
    except KeyError as e:
        raise ValueError("package.json doesn't have the jupyterlab configuration.")


def update_tsconfig():
    tsconfig_path = PROJECT_DIRECTORY.parent / 'tsconfig.json'
    tsconfig = {}
    
    with open(tsconfig_path, 'r', encoding='utf-8') as f:
        tsconfig = json.load(f)

    # make sure sourceMap is true
    compiler_options = tsconfig.get("compilerOptions")    
    compiler_options["sourceMap"] = True
    tsconfig["compilerOptions"] = compiler_options

    with open(tsconfig_path, 'w') as f:
        json.dump(tsconfig, f, indent=2)


def create_notebooks_dir():
    notebooks_dir = "{{cookiecutter.notebooks_dir}}"
    if not Path(notebooks_dir).is_absolute():
        notebooks_dir = PROJECT_DIRECTORY.parent / notebooks_dir

    if not os.path.isdir(notebooks_dir):
        os.makedirs(notebooks_dir)

def copy_webpack_config():
    shutil.move(
        os.path.join(str(PROJECT_DIRECTORY), "webpack.config.js"), 
        os.path.join(str(PROJECT_DIRECTORY.parent), "webpack.config.js")
    )


if __name__ == "__main__":
    update_package_json()
    update_tsconfig()
    copy_webpack_config()
    create_notebooks_dir()

