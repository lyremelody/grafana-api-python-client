#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import requests
from setting import GRAFANA_INFO


def get_admin_setting(cookies):
    uri = 'http://{0}:{1}/api/admin/settings'.format(GRAFANA_INFO['host'], GRAFANA_INFO['port'])
    r = requests.get(uri, cookies=cookies)
    return (r.status_code, r.text)


def get_admin_stats(cookies):
    uri = 'http://{0}:{1}/api/admin/stats'.format(GRAFANA_INFO['host'], GRAFANA_INFO['port'])
    r = requests.get(uri, cookies=cookies)
    return (r.status_code, r.text)


def get_api_keys(cookies):
    uri = 'http://{0}:{1}/api/auth/keys'.format(GRAFANA_INFO['host'], GRAFANA_INFO['port'])
    r = requests.get(uri, cookies=cookies)
    return (r.status_code, r.text)


def delete_api_key(cookies, key_id):
    uri = 'http://{0}:{1}/api/auth/keys/{2}'.format(GRAFANA_INFO['host'], GRAFANA_INFO['port'], key_id)
    r = requests.delete(uri, cookies=cookies)
    return (r.status_code, r.text)


if __name__ == '__main__':
    # from common import get_cookies
    # cookies = get_cookies('admin', 'password')
    # print(get_admin_setting(cookies))
    # print(get_admin_stats(cookies))

    # print(get_api_keys(cookies))
    # print(delete_api_key(cookies, '2'))
    pass

