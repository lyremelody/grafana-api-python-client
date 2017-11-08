#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import requests
import json
from setting import GRAFANA_INFO
from common import NoValue, get_auth_headers


class DataSourceType(NoValue):
    PROMETHEUS = 'prometheus'


def get_datasources(api_token):
    uri = 'http://{0}:{1}/api/datasources'.format(GRAFANA_INFO['host'], GRAFANA_INFO['port'])
    r = requests.get(uri, headers=get_auth_headers(api_token))
    return (r.status_code, r.text)


def get_single_datasource(api_token, datasource_id):
    uri = 'http://{0}:{1}/api/datasources/{2}'.format(GRAFANA_INFO['host'], GRAFANA_INFO['port'], datasource_id)
    r = requests.get(uri, headers=get_auth_headers(api_token))
    return (r.status_code, r.text)


def create_datasource(api_token, data_source_name, data_source_type, url, access='proxy', basic_auth=False):
    uri = 'http://{0}:{1}/api/datasources'.format(GRAFANA_INFO['host'], GRAFANA_INFO['port'])
    payload = {
        'name': data_source_name,
        'type': data_source_type,
        'url': url,
        'access': access,
        'basicAuth': basic_auth
    }
    r = requests.post(uri, headers=get_auth_headers(api_token), data=json.dumps(payload))
    return (r.status_code, r.text)


def create_datasource_prometheus(api_token, data_source_name, url, access='proxy', basic_auth=False):
    return create_datasource(api_token=api_token, 
        data_source_name=data_source_name, 
        data_source_type=DataSourceType.PROMETHEUS.value, 
        url=url, access=access, basic_auth=basic_auth)


def delete_datasource_by_name(api_token, datasource_name):
    uri = 'http://{0}:{1}/api/datasources/name/{2}'.format(GRAFANA_INFO['host'], GRAFANA_INFO['port'], datasource_name)
    r = requests.delete(uri, headers=get_auth_headers(api_token))
    return (r.status_code, r.text)


def delete_datasource_by_id(api_token, datasource_id):
    uri = 'http://{0}:{1}/api/datasources/{2}'.format(GRAFANA_INFO['host'], GRAFANA_INFO['port'], datasource_id)
    r = requests.delete(uri, headers=get_auth_headers(api_token))
    return (r.status_code, r.text)


if __name__ == '__main__':
    from common import get_cookies, get_api_token
    cookies = get_cookies('admin', 'password')

    api_token = get_api_token(cookies=cookies)
    # print(get_datasources(api_token))
    # print(create_datasource_prometheus(api_token=api_token, data_source_name='dcos1', url='http://192.168.84.68:8090'))
    print(delete_datasource_by_name(api_token, 'dcos1'))
    pass

