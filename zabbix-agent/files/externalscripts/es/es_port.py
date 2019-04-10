#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json, sys, os

name=sys.argv[1]


with open(os.path.join("/etc/zabbix/externalscripts/es", name), "r") as f:
  print json.dumps(json.load(f), indent=4)
