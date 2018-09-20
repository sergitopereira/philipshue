# -*- coding: UTF-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from builtins import object
import requests


class PyHue(object):
    def __init__(self, hub_ip="", user_name=""):
        """
        :param hub_ip: Private IP address of HUE hub
        :param user_name: Username
        """
        self.URL = "http://{}/api/{}/".format(hub_ip, user_name)

    def scan_lights(self):
        """
        scan lights connected to hue bridge
        :return: lights
        """
        url = self.URL + "lights"
        headers = {"Content-Type": "application/json"}
        try:
            http_query = requests.get(url, headers=headers)
            lights = http_query.json()
            return lights
        except requests.exceptions.RequestException as e:
            print(e)
            print("failed to obtain available lights")
