# 写入
import os
import yaml


def write_yaml(data):
    with open('F:\interfacetest\extract.yaml', encoding='utf-8', mode='a+') as f:
        yaml.dump(data, stream=f, allow_unicode=True)

def read_yaml(key):
    with open('F:\interfacetest\extract.yaml', encoding='utf-8', mode='r') as f:
        value = yaml.load(f, yaml.FullLoader)
        return value[key]

def read_testcase(path):
    with open(path, encoding='utf-8', mode='r') as f:
        value = yaml.load(f, yaml.FullLoader)
        return value

def clear_testcase(path):
    with open(path, encoding='utf-8', mode='w') as f:
        f.truncate()

