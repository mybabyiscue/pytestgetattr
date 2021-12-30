# 这是pytest_pom模式编写
## 欢迎大家来参观
其中采用发射机制来运行自动化测试
```
        testcases = listcases['cases']
        for cases in testcases:
            listcase = list(cases.values())
            with allure.step(listcase[0]):
                func = getattr(self.web,listcase[1])
                values = listcase[2:]
                func(*values)
```
