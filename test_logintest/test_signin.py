import re

import allure
import pytest

from All_Request import All_Requests
from yaml_util import write_yaml, read_testcase

@allure.feature('登陆模块')
@pytest.mark.login
class Test_signin:
    @allure.story('测试登陆')
    @pytest.mark.parametrize('casedata',read_testcase(r'F:\interfacetest/test_logintest/text_example.yaml'))
    def test_post_signin(self,casedata):
        res = All_Requests().requests_upload(
            method = casedata['request']['method'],
            url = casedata['request']['url'],
            headers = casedata['request']['headers'],
            data =casedata['request']['params']
        )
        value = res.headers.get('Set-Cookie')
        if value and 'sessionid' in value:
            match = re.search(r'sessionid=[^;]+',value)
            session_str = match.group()
            datas = {'Cookie': session_str}
            write_yaml(datas)
        else:
            print('')
        a = res.json()
        assert a['ret'] == 0





