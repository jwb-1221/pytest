import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import yaml


class read_yaml():
    def __init__(self,file):
        self.file = file
    def read_yaml(self):
        try:
            f=open(self.file,encoding="utf-8")
            data= yaml.load_all(f,Loader=yaml.FullLoader)
            for a in data:
                print(a)
                return a
        except Exception as e:
            print(e)
if __name__ == '__main__':
    read_yaml("D:\\request\腾讯云代码库\pytest_request\config\\requests.yaml").read_yaml()
