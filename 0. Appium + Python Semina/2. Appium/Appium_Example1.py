import os
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException

if __name__ == "__main__":

    app = os.path.join(os.path.dirname(__file__), 'C:\\Users\\User\\Desktop\\업무\\Appium\\5. TestFiles', 'ApiDemos-debug.apk')
    app = os.path.abspath(app)

    # 핸드폰 정보, OS 정보, 패키지 이름을 적습니다.
    cap = {
        'udid': '127.0.0.1:62001',
        'platformName': 'Android',
        'platformVersion': '7.1.2',
        'deviceName': 'Test Device',
        'automationName': 'Appium',
        'appPackage': 'io.appium.android.apis',
        'appActivity': 'io.appium.android.apis.ApiDemos',
        'newCommandTimeout': 300,
        'app': app
    }

    # Set up appium
    # 그리고 desired_capabilities에 연결하려는 디바이스의 정보를 넣습니다.
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities=cap
        )

    Button1 = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Accessibility"]')
    Button1.click()

    Button2 = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Accessibility Node Querying"]')
    Button2.click()

    Button3 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.CheckBox')
    Button3.click()
    Button3.click()
    Button3.click()

    sleep(5)

    driver.quit()
    
    print('Test End')
    pass