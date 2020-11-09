import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("https://www.linkedin.com")

def login():
    username = driver.find_element_by_id("session_key")
    username.clear()
    usernameinp = input("What is your username?")
    username.send_keys(usernameinp)
    password = driver.find_element_by_name("session_password")
    password.clear()
    passwordinp = input("What is your password?")
    password.send_keys(passwordinp)
    driver.find_element_by_class_name("sign-in-form__submit-button").click()
    driver.get("https://www.linkedin.com/mynetwork/")
    driver.maximize_window()


def main():
    clicked_buttons = []
    buttons = driver.find_elements_by_class_name("mt2")
    for i in range(16):
        if buttons[i-1].id in clicked_buttons:
            continue
        else:
            clicked_buttons.append(buttons[i-1].id)
            buttons[i-1].click()
    time.sleep(1)
    driver.refresh()


login()
time.sleep(5)
while __name__ == "__main__":
    main()
    time.sleep(4)