# coding:utf8


# @Time:    2021/12/23 22:50
# @Auth:    xiejun
# @filename: 

import yaml
def readyaml(filename):
    with open(filename,encoding='utf8') as f:
        data= yaml.safe_load(f)
        return data

if __name__ == "__main__":
    a=readyaml('../lib/cases.yaml')
    print(a)
