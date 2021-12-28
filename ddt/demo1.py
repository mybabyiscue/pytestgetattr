# coding:utf8


# @Time:    2021/12/27 22:50
# @Auth:    xiejun
# @filename: 
import pytest

@pytest.mark.parametrize('a,b,c',[(1,1,1),(2,2,2),(3,3,3)],
                         ids=['星期1','星期2','星期3'])

def test_1(a,b,c):
    print(a,b,c)

'''
    1.叠加使用和不叠加使用同时存在时，优先叠加使用
    2.叠加后，dis也会叠加
    3.叠加后，ids显示顺序是下面的叠加在上面的前面
    4.参数执行顺序是（a=11,b=21,c=31）,(a=11,b=21,c=31),(a=12,b=21,c=31),(a=12,b=22,c=32)
'''
# @pytest.mark.parametrize('a',[11,12],
#                          ids=['星期11','星期12'])
# @pytest.mark.parametrize('b,c',[(21,31),(22,32)],
#                          ids=['星期111','星期112'])
#
# def test_1(a,b,c):
#     print(a,b,c)

if __name__ == '__main__':
    pytest.main(['-sv','test_overlay.py'])
