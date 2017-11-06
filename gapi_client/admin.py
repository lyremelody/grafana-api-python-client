#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import requests
from setting import GRAFANA_INFO


def get_cookies(user, password):
    login_uri = 'http://{0}:{1}/login'.format(GRAFANA_INFO['host'], GRAFANA_INFO['port'])
    payload = {'user': user, 'password': password, 'email': ''}
    r = requests.post(login_uri, data=payload)
    if r.status_code == requests.codes.ok:
         return r.cookies
    return None


def get_admin_setting(cookies):
    uri = 'http://{0}:{1}/api/admin/settings'.format(GRAFANA_INFO['host'], GRAFANA_INFO['port'])
    r = requests.get(uri, cookies=cookies)
    return (r.status_code, r.text)


def get_admin_stats(cookies):
    uri = 'http://{0}:{1}/api/admin/stats'.format(GRAFANA_INFO['host'], GRAFANA_INFO['port'])
    r = requests.get(uri, cookies=cookies)
    return (r.status_code, r.text)


if __name__ == '__main__':
    cookies = get_cookies('admin', 'password')
    # print(get_admin_setting(cookies))
    # print(get_admin_stats(cookies))
