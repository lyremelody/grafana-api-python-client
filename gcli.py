#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#
# Copyright 2017 lyremelody
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import cmd

CMD_ENV = {
    'host': '127.0.0.1',
    'port': 3000
}


class GrafanaCmd(cmd.Cmd):
    @staticmethod
    def _sp1str(host, port):
        return '[Grafana CMD {0}:{1}] '.format(host, port)

    def _refresh_prompt(self):
        global CMD_ENV
        self.prompt = GrafanaCmd._sp1str(CMD_ENV['host'], CMD_ENV['port'])

    def preloop(self):
        self._refresh_prompt()

    def do_connect(self, line):
        host = raw_input('Grafana Host: ')
        port = raw_input('Grafana Port: ')

        global CMD_ENV
        CMD_ENV['host'] = host
        CMD_ENV['port'] = int(port)

        self._refresh_prompt()

    def do_exit(self, line):
        return True


if __name__ == '__main__':
    GrafanaCmd().cmdloop()
