import time

import pytest
import os


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    pytest.main()
    time.sleep(2)
    os.system('allure generate ./temps -o ./reports --clean')


