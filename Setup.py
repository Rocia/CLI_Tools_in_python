#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 17:03:37 2018

@author: root
"""
import sys
try:
    import requests
except:
    sys.exit("Import module requests before proceeding")

try:
    import argparse
except:
    sys.exit("Import module argparse before proceeding")

try:
    import click
except:
    sys.exit("Import module click before proceeding")
