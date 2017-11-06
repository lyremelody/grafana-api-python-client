#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

from enum import Enum
import requests
from setting import GRAFANA_INFO


class NoValue(Enum):
    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)


class KeyRole(NoValue):
    VIEWER = 'Viewer'
    EDITOR = 'Editor'
    ADMIN = 'Admin'


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


def create_admin_api_token(cookies, key_name, role=KeyRole.VIEWER.value):
    uri = 'http://{0}:{1}/api/auth/keys'.format(GRAFANA_INFO['host'], GRAFANA_INFO['port'])
    payload = {'name': key_name, 'role': role}
    r = requests.post(uri, cookies=cookies, data=payload)
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
    # cookies = get_cookies('admin', 'password')
    # print(get_admin_setting(cookies))
    # print(get_admin_stats(cookies))
    
    # import uuid
    # print(create_admin_api_token(cookies, str(uuid.uuid1()), role='Admin'))

    # print(KeyRole.VIEWER.value)
    # print(get_api_keys(cookies))
    # print(delete_api_key(cookies, '2'))
    pass

