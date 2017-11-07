#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

from enum import Enum
from io import StringIO
import json
import uuid
import requests
from setting import GRAFANA_INFO


API_TOKEN=None


class NoValue(Enum):
    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)


class KeyRole(NoValue):
    VIEWER = 'Viewer'
    EDITOR = 'Editor'
    ADMIN = 'Admin'


def get_base_headers():
    headers = {}
    headers['Accept'] = 'application/json'
    headers['Content-Type'] = 'application/json'
    return headers


def get_auth_headers(api_token):
    headers = get_base_headers()
    headers['Authorization'] = 'Bearer {0}'.format(api_token)
    return headers


def get_cookies(user, password):
    login_uri = 'http://{0}:{1}/login'.format(GRAFANA_INFO['host'], GRAFANA_INFO['port'])
    payload = {'user': user, 'password': password, 'email': ''} 
    r = requests.post(login_uri, data=payload)
    if r.status_code == requests.codes.ok:
         return r.cookies
    return None


def create_admin_api_token(cookies, key_name, role=KeyRole.VIEWER.value):
    uri = 'http://{0}:{1}/api/auth/keys'.format(GRAFANA_INFO['host'], GRAFANA_INFO['port'])
    payload = {'name': key_name, 'role': role}
    r = requests.post(uri, cookies=cookies, data=payload)
    return (r.status_code, r.text)


def get_api_token(cookies):
    global API_TOKEN
    if API_TOKEN is None:
        print("API_TOKEN is None")
        result = create_admin_api_token(cookies=cookies, key_name=str(uuid.uuid1()), role=KeyRole.ADMIN.value)
        if result[0] == requests.codes.ok:
            io = StringIO(result[1])
            res = json.load(io)
            API_TOKEN = res.get("key")
    return API_TOKEN


if __name__ == '__main__':
    cookies = get_cookies('admin', 'password')
    print(API_TOKEN)
    get_api_token(cookies)
    print(API_TOKEN)
    get_api_token(cookies)
    print(API_TOKEN)
    pass

