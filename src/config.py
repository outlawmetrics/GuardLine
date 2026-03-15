import yaml
import os

def load_config(repo_root="."):
    config_path = os.path.join(repo_root, ".guardline.yml")

    if not os.path.exists(config_path):
        return {}

    try:
        with open(config_path, "r") as f:
            data = yaml.safe_load(f)
        return data if data else {}
    except (IOError, yaml.YAMLError):
        return {} # does not require custom settings, use default for everything