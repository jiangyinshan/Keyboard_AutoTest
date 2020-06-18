import time

from adbtest.devices_key import samsung6_inputkey
from openpyxl import *
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {};
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '5203adddfc7334c1'
desired_caps['noReset'] = 'true'


# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps);

def getsize(self):
    x = self.driver.get_window_size()['width']  # 获取x轴的长度
    y = self.driver.get_window_size()['height']  # 获取y轴的长度
    print(x, y)


def cleartext(self):  # messenger输入框文本
    self.driver.find_element_by_xpath(
        "//android.widget.EditText[@resource-id='com.facebook.orca:id/(name removed)']").clear()


def swichlanguage(self):  # 右滑向左切换键盘语言
    TouchAction(self.driver).long_press(x=408, y=1225).move_to(x=250, y=1225).release().perform()


def gettext(self):  # 获取输入框内容
    str = self.driver.find_element_by_xpath(
        "//android.widget.EditText[@resource-id='com.facebook.orca:id/(name removed)']").text
    text = str.strip()
    return text


def keyboard_show(self):  # 点击messenger输入框，拉起键盘
    el1 = self.driver.find_element_by_xpath(
        "//android.widget.EditText[@resource-id='com.facebook.orca:id/(name removed)']")
    el1.click();


def click_apps(self, n):
    el1 = self.driver.find_element_by_xpath(
        "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[5]")
    el1.click();


def click_emojipro(self):
    el1 = self.driver.find_element_by_xpath(
        "//android.widget.TextView[@text='Emoji Keyboard' and @content-desc='Emoji Keyboard']")
    el1.click();


def click_mine(self):
    el1 = self.driver.find_element_by_xpath(
        "/hierarchy/ankeyboard_showdroid.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[4]/android.widget.ImageView")
    el1.click();


def click_preferences(self):
    el1 = self.driver.find_element_by_xpath(
        "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.emoji.coolkeyboard:id/rv_settings']/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView[1]")
    el1.click();


def click_number_row(self):
    el1 = self.driver.find_element_by_xpath(
        "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.emoji.coolkeyboard:id/recycler_view']/android.widget.LinearLayout[6]/android.widget.LinearLayout[1]/android.widget.CheckBox[1]")
    el1.click();


def click_selector_row(self):
    el1 = self.driver.find_element_by_xpath(
        "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.emoji.coolkeyboard:id/recycler_view']/android.widget.LinearLayout[7]/android.widget.LinearLayout[1]/android.widget.CheckBox[1]")
    el1.click();


def click_messenger(self):
    el1 = self.driver.find_element_by_xpath(
        "//android.widget.EditText[@resource-id='com.facebook.orca:id/(name removed)']")
    el1.click();


def send_message(self):
    el1 = self.driver.find_element_by_xpath(
        "//android.widget.ImageView[@content-desc='Send']")
    el1.click();


def send_popup(self, n):
    self.driver.tap([(603, 568)], n);


def click_language(self):
    language = self.driver.find_element_by_xpath(
        "//androidx.recyclerview.widget.RecyclerView[@resource-id='kika.emoji.keyboard.teclados.clavier:id/rv_settings']/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]")
    language.click()


def add_es(self):
    TouchAction(self.driver).press(x=343, y=1203).move_to(x=351, y=225).release().perform()
    TouchAction(self.driver).press(x=276, y=1218).move_to(x=312, y=392).release().perform()
    TouchAction(self.driver).press(x=343, y=1200).move_to(x=320, y=570).release().perform()
    el1 = self.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.FrameLayout[6]/android.widget.RelativeLayout/android.widget.TextView[2]")
    el1.click()


def input_by_tag(word, self):
    if word == "a" or word == "A":
        samsung6_inputkey.a(self, 0)
    elif word == "b" or word == "B":
        samsung6_inputkey.b(self, 0)
    elif word == "c" or word == "C":
        samsung6_inputkey.c(self, 0)
    elif word == "d" or word == "D":
        samsung6_inputkey.d(self, 0)
    elif word == "e" or word == "E":
        samsung6_inputkey.e(self, 0)
    elif word == "f" or word == "F":
        samsung6_inputkey.f(self, 0)
    elif word == "g" or word == "G":
        samsung6_inputkey.g(self, 0)
    elif word == "h" or word == "H":
        samsung6_inputkey.h(self, 0)
    elif word == "i" or word == "I":
        samsung6_inputkey.i(self, 0)
    elif word == "j" or word == "J":
        samsung6_inputkey.j(self, 0)
    elif word == "k" or word == "K":
        samsung6_inputkey.k(self, 0)
    elif word == "l" or word == "L":
        samsung6_inputkey.l(self, 0)
    elif word == "m" or word == "M":
        samsung6_inputkey.m(self, 0)
    elif word == "n" or word == "N":
        samsung6_inputkey.n(self, 0)
    elif word == "o" or word == "O":
        samsung6_inputkey.o(self, 0)
    elif word == "p" or word == "P":
        samsung6_inputkey.p(self, 0)
    elif word == "q" or word == "Q":
        samsung6_inputkey.q(self, 0)
    elif word == "r" or word == "R":
        samsung6_inputkey.r(self, 0)
    elif word == "s" or word == "S":
        samsung6_inputkey.s(self, 0)
    elif word == "t" or word == "J":
        samsung6_inputkey.t(self, 0)
    elif word == "u" or word == "U":
        samsung6_inputkey.u(self, 0)
    elif word == "v" or word == "V":
        samsung6_inputkey.v(self, 0)
    elif word == "w" or word == "W":
        samsung6_inputkey.w(self, 0)
    elif word == "x" or word == "X":
        samsung6_inputkey.x(self, 0)
    elif word == "y" or word == "Y":
        samsung6_inputkey.y(self, 0)
    elif word == "z" or word == "Z":
        samsung6_inputkey.z(self, 0)
    elif word == "😀":
        samsung6_inputkey.emoji_input(self, 0)


def change_emoji_style(self):
    samsung6_inputkey.menu(self, 0)
    time.sleep(1)
    samsung6_inputkey.menu_emoji_style(self, 0)
    time.sleep(1)
    samsung6_inputkey.defult_emoji_style(self, 0)
    time.sleep(1)
