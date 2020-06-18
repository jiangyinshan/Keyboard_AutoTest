import unittest
import selenium
import logging
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from pip._vendor.distlib.compat import raw_input

desired_caps = {};
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '5203adddfc7334c1'
desired_caps['noReset'] = 'true'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def a(self, n):
    self.driver.tap([(30, 1001)], n)


def b(self, n):
    self.driver.tap([(425, 1115)], n)


def c(self, n):
    self.driver.tap([(284, 1115)], n)


def d(self, n):
    self.driver.tap([(214, 999)], n)


def e(self, n):
    self.driver.tap([(189, 902)], n)


def f(self, n):
    self.driver.tap([(293, 1005)], n)


def g(self, n):
    self.driver.tap([(367, 1003)], n)


def h(self, n):
    self.driver.tap([(417, 982)], n)


def i(self, n):
    self.driver.tap([(547, 877)], n)


def j(self, n):
    self.driver.tap([(506, 1005)], n)


def k(self, n):
    self.driver.tap([(576, 1009)], n)


def l(self, n):
    self.driver.tap([(647, 989)], n)


def m(self, n):
    self.driver.tap([(572, 1119)], n)


def n(self, n):
    self.driver.tap([(502, 1119)], n)


def o(self, n):
    self.driver.tap([(610, 885)], n)


def p(self, n):
    self.driver.tap([(680, 879)], n)


def q(self, n):
    self.driver.tap([(32, 881)], n)


def r(self, n):
    self.driver.tap([(262, 891)], n)


def s(self, n):
    self.driver.tap([(143, 1007)], n)


def t(self, n):
    self.driver.tap([(326, 885)], n)


def u(self, n):
    self.driver.tap([(467, 893)], n)


def v(self, n):
    self.driver.tap([(359, 1117)], n)


def w(self, n):
    self.driver.tap([(114, 885)], n)


def x(self, n):
    self.driver.tap([(214, 1109)], n)


def y(self, n):
    self.driver.tap([(396, 897)], n)


def z(self, n):
    self.driver.tap([(137, 1113)], n)


def space(self, n):
    self.driver.tap([(393, 1221)], n)  # 点击键盘空格键


def menu(self, n):
    self.driver.tap([(50, 795)], n)  # 点击menu


def menu_emoji_style(self, n):
    self.driver.tap([(631, 995)], n)  # 点击menu内emoji style


def defult_emoji_style(self, n):
    self.driver.tap([(559, 950)], n)  # 点击键盘空格键


def enter(self, n):
    self.driver.tap([(668, 1216)], n)  # 点击键盘enter键


def delete(self, n):
    self.driver.tap([(673, 1111)], n)  # 点击键盘闪促


def emoji(self, n):
    self.driver.tap([(133, 1214)], n)  # 点击键盘emoji


def click_mid_sugg(self, n):
    self.driver.tap([(288, 796)], n)  # 点击中间候选词


def longpress_sugg(self, n):  # 长按候选词
    self.driver.tap([(288, 796)], n)


def longpress_sugg_input(self, n):
    self.driver.tap([(358, 700)], n)  # 点击候选词弹出框输入


def close_sugg(self, n):  # 关闭候选词栏
    self.driver.tap([(19, 797)], n)


def input_map(self):
    dict = {1: a(self, 0), 2: b(self, 0), 3: c(self, 0)}
    n = raw_input()
    i = int(n) % 10
    dict[i](self, 0)


def emoji_input(self, n):
    self.driver.tap([(52, 877)], n)
