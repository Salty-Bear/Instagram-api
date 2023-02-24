import os
import time
from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/profile/<string:userid>')
def stalk(userid):
    data = {}
    os.environ['PATH'] += r"E:/selenium_driver"
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/")
    driver.implicitly_wait(10)
    # time.sleep(2)

    username = driver.find_element(By.NAME, "username")
    username.send_keys("aryamanraj123456789@gmail.com")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("zombiesmasher12")

    button = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]")
    button.click()
    # element = driver.find_element(By.ID, "downloadButton")
    # element.click()
    time.sleep(5)

    driver.get("https://www.instagram.com/" + userid)
    l1 = []
    try:
        ul = driver.find_element(By.TAG_NAME, 'ul')
        items = ul.find_elements(By.TAG_NAME, 'li')

        for k in items:
            l1.append(k.text)
    except:
        data['stats'] = ["Failed to get stats"]

    data['stats'] = l1

    time.sleep((1))
    try:
        bio = driver.find_element(By.XPATH,
                                  '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[3]')
        # print(bio.text)
        data['bio'] = [bio.text]
    except:
        data['bio'] = ["Failed to get Bio"]

    try:
        pfp = driver.find_elements(By.XPATH,
                                   '//*[@class="x6umtig x1b1mbwd xaqea5y xav7gou xk390pu x5yr21d xpdipgo xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x11njtxf xh8yej3"]')
        # print(pfp[1].get_attribute('src'))
        data['pfp'] = [pfp[1].get_attribute('src')]
    except:
        data['pfp'] = []

    try:
        picture = driver.find_elements(By.XPATH, '//*[@class="_aagv"]/img')

        l1 = []
        for i in picture:
            l1.append(i.get_attribute('src'))

        data['pictures'] = l1
    except:
        data['pictures'] = ["failed to get pictures"]
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
