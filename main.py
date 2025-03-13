from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

def send_danmu_at_specific_time(video_url, time_str, message, cookies, repeat=5):
    options = webdriver.ChromeOptions()
    # Prevent detection of Selenium
    options.add_argument("--disable-blink-features=AutomationControlled")
    # Set other WebDriver options as needed
    with webdriver.Chrome(options=options) as driver:
        try:
            driver.get(video_url)
            # Set cookies
            for cookie in cookies:
                driver.add_cookie(cookie)
            # Reload the page to apply cookies
            driver.get(video_url)
            # Wait for the page to load
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

            # Initialize WebDriverWait for waiting for elements
            wait = WebDriverWait(driver, 10)

            # Pause the video
            pause_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.bpx-player-ctrl-play')))
            pause_button.click()

            # Wait for the time label to be clickable
            time_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.bpx-player-ctrl-time-label')))
            time_label.click()  # Click to make the time input box interactable

            # Wait for the time input box to be interactable
            time_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.bpx-player-ctrl-time-seek')))
            time_input.send_keys(Keys.CONTROL + 'a')
            time_input.send_keys(Keys.BACKSPACE)
            time_input.send_keys(time_str)
            time_input.send_keys(Keys.ENTER)

            # Wait for skip and then pause
            time.sleep(0.5)
            pause_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.bpx-player-ctrl-play')))
            pause_button.click()

            # Wait for the danmu input box to be present
            danmu_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.bpx-player-dm-input')))

            for i in range(repeat):  # Loop to send the message a specified number of times
                for attempt in range(3):
                    try:
                        danmu_input.clear()
                        danmu_input.send_keys(message)
                        danmu_input.send_keys(Keys.ENTER)
                        print(f"Sent danmu {i + 1} times")
                        break
                    except StaleElementReferenceException:
                        if attempt == 2:
                            raise

                time.sleep(5.5)
        finally:
            # WebDriver will automatically close when exiting the context manager
            pass

# Usage example
if __name__ == "__main__":
    video_url = "https://www.bilibili.com/video/BV1xx411c7Xg/?spm_id_from=333.337.search-card.all.click&vd_source=5bde4bc0a9e594de5e2a1af1aaf663b7"
    time_str = "17:25"
    message = "弹幕测试12345"
    cookies = [
        {'name': 'CURRENT_FNVAL',       'value': 'your own', 'domain': '.bilibili.com', 'path': '/'},
        {'name': 'CURRENT_QUALITY',     'value': 'your own', 'domain': '.bilibili.com', 'path': '/'},
        {'name': 'DedeUserID',          'value': 'your own', 'domain': '.bilibili.com', 'path': '/'},
        {'name': 'DedeUserID__ckMd5',   'value': 'your own', 'domain': '.bilibili.com', 'path': '/'},
        {'name': 'SESSDATA',            'value': 'your own', 'domain': '.bilibili.com', 'path': '/'},
        {'name': 'bili_jct',            'value': 'your own', 'domain': '.bilibili.com', 'path': '/'},
        {'name': 'bili_ticket',         'value': 'your own', 'domain': '.bilibili.com', 'path': '/'}
    ]
    repeat = 3
    send_danmu_at_specific_time(video_url, time_str, message, cookies, repeat=repeat)