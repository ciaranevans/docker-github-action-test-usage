import sys

import yaml


def install_packages(path_to_meta_yml: str):
    with open(f"/github/workspace/{path_to_meta_yml}", "r") as file_in:
        test_yaml = yaml.load(file_in, Loader=yaml.FullLoader)
        print(test_yaml["test"]["packages"])


if __name__ == "__main__":
    install_packages(sys.argv[1])
