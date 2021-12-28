# coding:utf8


# @Time:    2021/12/23 21:25
# @Auth:    xiejun
# @filename: 
import yaml
def readyaml(filename):
    with open(filename,encoding='utf8') as f:
        data= yaml.safe_load(f)
        return data
        # datas = yaml.load(f, Loader=yaml.FullLoader)
        # print(datas)


if __name__ == "__main__":
    a=readyaml('./cases.yaml')
    # print(a)
    datas = a['loginpage'][0]
    # print(datas)
    testcases = datas['cases']
    # print(testcases)
    for cases in testcases:
        listcase = list(cases.values())
        print(listcase)

