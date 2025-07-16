import allure
import pytest
import requests

from All_Request import All_Requests
from yaml_util import read_testcase, read_yaml,write_yaml

@allure.feature('客户模块')
class Test_customer:
    @allure.story('获取客户列表')
    @pytest.mark.parametrize('casedata', read_testcase(r'F:\interfacetest\test_customer\text_customerexample.yaml'))

    def test_showcustomer(self, casedata):
        headers = casedata['request']['headers']
        cookie = read_yaml('Cookie')
        if cookie:
            headers['Cookie'] = cookie
        else:
            pytest.skip('跳过测试')
        res = All_Requests().requests_upload(
            method=casedata['request']['method'],
            url=casedata['request']['url'],
            headers=headers,
            params=casedata['request']['params']
        )
        a = res.json()
        assert a['ret'] == 0

    @pytest.mark.parametrize('casedata', read_testcase(r'F:\interfacetest\test_customer\test_add_customers.yaml'))
    @allure.story('添加客户')

    def test_add_customers(self, casedata):
        headers = casedata['request']['headers']
        cookie = read_yaml('Cookie')
        if cookie:
            headers['Cookie'] = cookie
        else:
            pytest.skip('跳过测试')
        res = All_Requests().requests_upload(
            url=casedata['request']['url'],
            method=casedata['request']['method'],
            json=casedata['request']['json'],
            headers=headers
        )
        a = res.json()
        idsequence = a['id']
        datas = {'Id':idsequence}
        write_yaml(datas)

        assert a['ret'] == 0

    @pytest.mark.parametrize('casedata',read_testcase(r'F:\interfacetest\test_customer\text_put_customer.yaml'))
    @allure.story('修改客户')

    def test_put_customer(self,casedata):
        headers = casedata['request']['headers']
        cookie = read_yaml('Cookie')
        if cookie:
            headers['Cookie'] = cookie
        else:
            pytest.skip('跳过测试')
        json = casedata['request']['json']
        id_sequence = read_yaml('Id')
        if id_sequence:
            json['Id'] = id_sequence
        else:
            pytest.skip('跳过测试')
        res = All_Requests().requests_upload(
            url = casedata['request']['url'],
            method = casedata['request']['method'],
            json = json,
            headers =headers
        )

    @pytest.mark.parametrize('casedata',read_testcase(r'F:\interfacetest\test_customer\test_delete_customer.yaml'))
    @allure.story('删除客户')

    def test_delete_customer(self,casedata):
        json = casedata['request']['json']
        id_sequence = read_yaml('Id')
        if id_sequence:
            json['id'] = id_sequence
        else:
            pytest.skip('跳过测试')
        headers = casedata['request']['headers']
        cookie = read_yaml('Cookie')
        if cookie:
            headers['Cookie'] = cookie
        else:
            pytest.skip('跳过测试')
        res = All_Requests().requests_upload(
            method = casedata['request']['method'],
            headers = headers,
            json = json,
            url = casedata['request']['url']
        )
        print(res.json())

