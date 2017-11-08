#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

from io import StringIO
import json
import requests
from setting import GRAFANA_INFO
from common import get_auth_headers


def get_gnet_dashboard(api_token, gnet_id):
    uri = 'http://{0}:{1}/api/gnet/dashboards/{2}'.format(GRAFANA_INFO['host'], GRAFANA_INFO['port'], gnet_id)
    r = requests.get(uri, headers=get_auth_headers(api_token))
    return (r.status_code, r.text)


def import_gnet_dashboard_for_prometheus_datasource(api_token, gnet_id, prometheus_datasource_name):
    dashboard_json = None
    input_json = dict()
    result = get_gnet_dashboard(api_token, gnet_id)
    if result[0] == requests.codes.ok:
        io = StringIO(result[1])
        res = json.load(io)
        dashboard_json = res.get("json")
        input_json = dashboard_json["__inputs"][0]    

    input_json['value'] = prometheus_datasource_name

    payload = {
        'dashboard': dashboard_json,
        'inputs': [input_json],
        'overwrite': True
    }

    uri = 'http://{0}:{1}/api/dashboards/import'.format(GRAFANA_INFO['host'], GRAFANA_INFO['port'])
    r = requests.post(uri, headers=get_auth_headers(api_token), data=json.dumps(payload))
    return (r.status_code, r.text)


if __name__ == '__main__':
    from common import get_cookies, get_api_token
    cookies = get_cookies('admin', 'password')

    api_token = get_api_token(cookies=cookies)
    #print(get_gnet_dashboard(api_token, 395))
    import_gnet_dashboard_for_prometheus_datasource(api_token, 395, 'dcos')
    import_gnet_dashboard_for_prometheus_datasource(api_token, 718, 'dcos')
    pass

