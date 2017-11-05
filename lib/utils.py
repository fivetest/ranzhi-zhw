#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: samren
import time
import os

def captureScreen(driver):
    driver.get_screenshot_as_file("./screenshots/mypic_%s.jpg" % time.strftime("%Y-%m-%d %H-%M-%S"))