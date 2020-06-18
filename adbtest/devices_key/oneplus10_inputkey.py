import unittest
import selenium
import logging
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {};
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '5203adddfc7334c1'
desired_caps['noReset'] = 'true'
oneplus_desired_caps = {};
oneplus_desired_caps['platformName'] = 'Android'
oneplus_desired_caps['platformVersion'] = '10'
oneplus_desired_caps['deviceName'] = '4e62be76'
oneplus_desired_caps['noReset'] = 'true'


# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps);

def a(self, n):
    self.driver.tap([(108, 1784)], n);


def b(self, n):
    self.driver.tap([(643, 1949)], n);


def c(self, n):
    self.driver.tap([(427, 1953)], n);


def d(self, n):
    self.driver.tap([(424, 1775)], n);


def e(self, n):
    self.driver.tap([(272, 1615)], n);


def f(self, n):
    self.driver.tap([(427, 1775)], n);


def g(self, n):
    self.driver.tap([(540, 1775)], n);


def h(self, n):
    self.driver.tap([(639, 1775)], n);


def i(self, n):
    self.driver.tap([(803, 1615)], n)


def j(self, n):
    self.driver.tap([(506, 1005)], n);


def k(self, n):
    self.driver.tap([(756, 1784)], n);


def l(self, n):
    self.driver.tap([(963, 1780)], n);


def m(self, n):
    self.driver.tap([(864, 1949)], n);


def n(self, n):
    self.driver.tap([(761, 1949)], n);


def o(self, n):
    self.driver.tap([(916, 1625)], n);


def p(self, n):
    self.driver.tap([(1019, 1629)], n);


def q(self, n):
    self.driver.tap([(56, 1629)], n);


def r(self, n):
    self.driver.tap([(380, 1625)], n);


def s(self, n):
    self.driver.tap([(216, 1789)], n);


def t(self, n):
    self.driver.tap([(484, 1615)], n);


def u(self, n):
    self.driver.tap([(704, 1620)], n);


def v(self, n):
    self.driver.tap([(540, 1953)], n);


def w(self, n):
    self.driver.tap([(160, 1625)], n);


def x(self, n):
    self.driver.tap([(324, 1953)], n);


def y(self, n):
    self.driver.tap([(596, 1629)], n);


def z(self, n):
    self.driver.tap([(211, 1953)], n);


def space(self, n):
    self.driver.tap([(587, 2118)], n);


def enter(self, n):
    self.driver.tap([(1000, 2113)], n);


def delete(self, n):
    self.driver.tap([(1000, 1953)], n);


def emoji(self, n):
    self.driver.tap([(216, 2108)], n);


def click_mid_sugg(self, n):
    self.driver.tap([(531, 1484)], n);  # 点击中间候选词


def longpress_sugg(self, n):  # 长按候选词
    self.driver.tap([(531, 1484)], n);


def close_sugg(self, n):  # 关闭候选词栏
    self.driver.tap([(23, 1479)], n);


def longpress_sugg_input(self, n):
    self.driver.tap([(540, 1254)], n)
