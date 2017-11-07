#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import requests
from setting import GRAFANA_INFO
from common import get_auth_headers


def get_dashboard(api_token, dashboard_slug):
    uri = 'http://{0}:{1}/api/dashboards/db/{2}'.format(GRAFANA_INFO['host'], GRAFANA_INFO['port'], dashboard_slug)
    r = requests.get(uri, headers=get_auth_headers(api_token))
    return (r.status_code, r.text)


def delete_dashboard(api_token, dashboard_slug):
    uri = 'http://{0}:{1}/api/dashboards/db/{2}'.format(GRAFANA_INFO['host'], GRAFANA_INFO['port'], dashboard_slug)
    r = requests.delete(uri, headers=get_auth_headers(api_token))
    return (r.status_code, r.text)


if __name__ == '__main__':
    from common import get_cookies, get_api_token
    cookies = get_cookies('admin', 'password')

    api_token = get_api_token(cookies=cookies)
    print(get_dashboard(api_token, "prometheus-stats"))
    pass

