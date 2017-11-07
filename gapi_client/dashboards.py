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
    from common import get_cookies, create_admin_api_token, KeyRole
    cookies = get_cookies('admin', 'password')

    import uuid
    result = create_admin_api_token(cookies=cookies, key_name=str(uuid.uuid1()), role=KeyRole.ADMIN.value)

    if result[0] == requests.codes.ok:
        from io import StringIO
        io = StringIO(result[1])
        import json
        res = json.load(io)
        api_token = res.get("key")
        print(get_dashboard(api_token, "prometheus-stats"))
    else:
        print("error")
        print(result)

    pass

