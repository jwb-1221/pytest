#!/usr/bin/python
import os
import sys
import yaml
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


class read_yaml:
    def __init__(self, file):
        self.file = file

    def read_yaml(self):
        try:
            f = open(self.file, encoding="utf-8")
            data = yaml.load_all(f, Loader=yaml.FullLoader)
            for a in data:
                return a
        except Exception as e:
            print(e)


if __name__ == '__main__':
    read_yaml().read_yaml()
