import os
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException

if __name__ == "__main__":

    # ----------- 1. Basic -----------
    # 1_Basic_Number app은 ㅇㅇㅇ 이다.
    app = 1234
    
    # 3_Basic_String
    app = "C:\\Users\\User\\Desktop\\업무\\Appium\\5. TestFiles"
    app = app + "\\ApiDemos-debug.apk"

    print(app)

    # ----------- 다음 단계 -----------
    
    # app = os.path.join(os.path.dirname(__file__), 'C:\\Users\\User\\Desktop\\업무\\Appium\\5. TestFiles', 'ApiDemos-debug.apk')
    # app = os.path.abspath(app)

    # 핸드폰 정보, OS 정보, 패키지 이름을 적습니다.
    cap = {
        'udid': '127.0.0.1:62001',                          # adb상 일련번호
        'platformName': 'Android',                          # OS 종류
        'platformVersion': '7.1.2',                         # OS 버전
        'deviceName': 'Test Device',                        # deviceName
        'automationName': 'Appium',                         # 사용할 자동화 툴
        'appPackage': 'io.appium.android.apis',             # 설치할 appPackage Name
        'appActivity': 'io.appium.android.apis.ApiDemos',   # 첫 실행할 apk 
        'newCommandTimeout': 300,                           # 명령 실행 안될 경우 Timeout
        'app': app                                          # 패키지 설치할 경로
    }

    # Set up appium
    # 그리고 desired_capabilities에 연결하려는 디바이스의 정보를 넣습니다.
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities=cap
        )
    
    
    # 테스트 시나리오
    # 버튼 Click
    Button1 = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Accessibility"]')
    Button1.click()

    Button2 = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Accessibility Node Querying"]')
    Button2.click()

    Button3 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.CheckBox')
    Button3.click()
    Button3.click()
    Button3.click()

    # 잠시 쉬었다 (5 초간)
    sleep(5)

    # 테스트 종료
    driver.quit()
    
    # 테스트 종료됨을 알림
    print('Test End')