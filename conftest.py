import pytest

from yaml_util import clear_testcase

import time


@pytest.fixture(scope='module', autouse=True)
def exe_sql():
    """测试用例的夹具，提供前后置操作"""
    print("\n" + "="*30)  # 添加分隔线
    print("开始测试".center(28))  # 居中显示
    yield  # 这里是测试用例执行的位置
    print("\n" + "结束测试".center(28))
    print("="*30 + "\n")


# @pytest.fixture(scope='module', autouse=True)
# def clear_extract():
#     yield
#     clear_testcase(r'F:\interfacetest\extract.yaml')
#     print('已经成功清除Cookie')