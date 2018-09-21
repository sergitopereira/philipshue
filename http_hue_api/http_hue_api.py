# -*- coding: UTF-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from builtins import object
import requests
from prettytable import PrettyTable


class PyHue(object):
    def __init__(self, hub_ip="", user_name=""):
        """
        :param hub_ip: Private IP address of HUE hub
        :param user_name: Username
        """
        self.url = "http://{}/api/{}/".format(hub_ip, user_name)
        self.headers = {"Content-Type": "application/json"}

    def scan_lights(self):
        """
        scan lights connected to hue bridge
        """
        url = self.url + "lights"

        try:
            http_query = requests.get(url, headers=self.headers)
            lights = http_query.json()
            table = PrettyTable()
            table.field_names = ["ID", "NAME", "STATE", "UPDATE"]
            table.align = 'l'
            for key, light in lights.items():
                if light['state']['on']:
                    state = 'ON'
                else:
                    state = 'OFF'
                table.add_row([key, light['name'], state, light['swupdate']['state']])
            print(table)
        except requests.exceptions.RequestException as e:
            print(e)
            print("failed to obtain available lights")

    def light(self, id, power):
        """
        Turn on/off lights
        :param id: light unique id number
        :param power: boolean True=on False=off
        :return: none
        """
        url = '{}lights/{}/state'.format(self.url, id)
        payload = {"on": power}
        if power:
            power = 'ON'
        else:
            power = 'OFF'
        try:
            http_put = requests.put(url, json=payload, headers=self.headers)
            print("light {} has been turned {}".format(id, power))
        except requests.exceptions.RequestException as e:
            print(e)
            print("failed to turn: {} light id: {}".format(power, id))
