# add password, user id and array of tests on 243, 243 and 249 line
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys, getopt
def file_name(info):
    for file_name in os.listdir('D:/Projects/Codetantra_Bot'):
        if file_name.startswith(info):
            return file_name
def file_add(filename,question):
    m=0
    for file_name in os.listdir('D:/Projects/Codetantra_Bot'):
            if file_name.startswith('NewQuestions'):
                file1 = open("NewQuestions.txt","a")
                file1.write(filename + '\n')
                file1.write(question + '\n\n')
                break

            else:
                while m < 1:
                    with open("NewQuestions.txt", mode = "a") as file1:
                        file1.write(filename + '\n')
                        file1.write(question + '\n\n')
                        m = m+1
def question_solving():
    WebDriverWait(browser, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'modal-backdrop fade')))
    WebDriverWait(browser, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'preloader-box')))
    WebDriverWait(browser, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'preloader-dot')))
    browser.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div[4]/div/div/div[2]/div[2]/button").click()
    WebDriverWait(browser, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'modal-backdrop fade')))
    WebDriverWait(browser, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'preloader-box')))
    WebDriverWait(browser, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'preloader-dot')))
    try:
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'questionInfo')))
        f = browser.find_element(By.ID,'questionInfo').text
        g = f.split(' of ')[1]
        k = f.split('Q')[1]
        l = k.split(' of ')[0]
        m=int(l)
        if m!=1:
            x=0
            while x<int(g):
                e = browser.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/span')
                browser.execute_script("arguments[0].scrollIntoView();", e)
                e.click()
                browser.implicitly_wait(3)
                time.sleep(3)
                x1 = str(x)
                h= browser.find_element(By.XPATH, f'//span[@data-cscqi="{x1}"]')
                h.click()
                browser.implicitly_wait(2)
                time.sleep(2)
                j= browser.find_element(By.XPATH, '/html/body')
                j.click()
                browser.implicitly_wait(2)
                time.sleep(2)
                a = browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[3]/div/div/div').get_attribute("filename")
                b = browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div').get_attribute("textContent")
                time.sleep(2)
                browser.implicitly_wait(2)
                i=0
                x = x+1
                d = file_name(a)
                if d == None:
                    file_add(a,b)
                elif '.txt' in d:
                    text = open(d)
                    file = open(d)
                    n = file.read()
                    count = n.count('{')
                    count = count*10
                    try:
                        browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div[1]/ul/li[3]')
                        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div/div/div[2]/div"))).click()
                        pyautogui.hotkey('ctrl', 'a')
                        pyautogui.press('backspace')
                        pyautogui.press('ctrl','a')
                        pyautogui.press('ctrl', '/')
                        pyautogui.press('enter')
                        for each_line in text:
                            pyautogui.typewrite(each_line)
                        while i <= count:
                            pyautogui.press('delete')
                            i=i+1
                        send4 = browser.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div[1]/div[2]/form/div[4]/div[1]/span[2]/span[2]/i")
                        browser.execute_script("arguments[0].scrollIntoView();", send4)
                        send4.click()
                        time.sleep(3)
                    except NoSuchElementException:
                        send3 = browser.find_element(By.CLASS_NAME,"ace_content")
                        send3.click()
                        pyautogui.hotkey('ctrl', 'a')
                        pyautogui.press('backspace')
                        pyautogui.press('ctrl','a')
                        pyautogui.press('ctrl', '/')
                        pyautogui.press('enter')
                        for each_line in text:
                            pyautogui.typewrite(each_line)
                        while i <= count:
                            pyautogui.press('delete')
                            i=i+1
                        send4 = browser.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div[1]/div[2]/form/div[4]/div[1]/span[2]/span[2]/i")
                        browser.execute_script("arguments[0].scrollIntoView();", send4)
                        send4.click()
                        time.sleep(3)
        elif m==1:
            v=1
            a = browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[3]/div/div/div').get_attribute("filename")
            Ṇb = browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div').get_attribute("textContent")
            browser.implicitly_wait(2)
            i=0
            d = file_name(a)
            if d == None:
                file_add(a,b)
            elif '.txt' in d:
                text = open(d)
                file = open(d)
                n = file.read()
                count = n.count('{')
                count = count*10
                try:
                    browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div[1]/ul/li[3]')
                    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div/div/div[2]/div"))).click()
                    pyautogui.hotkey('ctrl', 'a')
                    pyautogui.press('backspace')
                    pyautogui.press('ctrl','a')
                    pyautogui.press('ctrl', '/')
                    pyautogui.press('enter')
                    for each_line in text:
                        pyautogui.typewrite(each_line)
                    while i <= count:
                        pyautogui.press('delete')
                        i=i+1
                    send4 = browser.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div[1]/div[2]/form/div[4]/div[1]/span[2]/span[2]/i")
                    browser.execute_script("arguments[0].scrollIntoView();", send4)
                    send4.click()
                    time.sleep(3)
                except NoSuchElementException:
                    send3 = browser.find_element(By.CLASS_NAME,"ace_content")
                    send3.click()
                    pyautogui.hotkey('ctrl', 'a')
                    pyautogui.press('backspace')
                    pyautogui.press('ctrl','a')
                    pyautogui.press('ctrl', '/')
                    pyautogui.press('enter')
                    for each_line in text:
                        pyautogui.typewrite(each_line)
                    while i <= count:
                        pyautogui.press('delete')
                        i=i+1
                    send4 = browser.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div[1]/div[2]/form/div[4]/div[1]/span[2]/span[2]/i")
                    browser.execute_script("arguments[0].scrollIntoView();", send4)
                    send4.click()
                    time.sleep(3)
                while v<int(g):
                    e = browser.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/span')
                    browser.execute_script("arguments[0].scrollIntoView();", e)
                    e.click()
                    browser.implicitly_wait(3)
                    time.sleep(3)
                    v1 = str(v)
                    h= browser.find_element(By.XPATH, f'//span[@data-cscqi="{v1}"]')
                    h.click()
                    browser.implicitly_wait(2)
                    time.sleep(2)
                    j= browser.find_element(By.XPATH, '/html/body')
                    j.click()
                    browser.implicitly_wait(2)
                    time.sleep(2)
                    a = browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div[3]/div/div/div').get_attribute("filename")
                    b = browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div[2]/form/div[1]/div/div[1]').get_attribute("textContent")
                    time.sleep(2)
                    browser.implicitly_wait(2)
                    i=0
                    v = v+1
                    d = file_name(a)
                    if d == None:
                        file_add(a,b)
                    elif '.txt' in d:
                        text = open(d)
                        file = open(d)
                        n = file.read()
                        count = n.count('{')
                        count = count*10
                        try:
                            browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div[1]/ul/li[3]')
                            WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div/div/div[2]/div"))).click()
                            pyautogui.hotkey('ctrl', 'a')
                            pyautogui.press('backspace')
                            pyautogui.press('ctrl','a')
                            pyautogui.press('ctrl', '/')
                            pyautogui.press('enter')
                            for each_line in text:
                                pyautogui.typewrite(each_line)
                            while i <= count:
                                pyautogui.press('delete')
                                i=i+1
                            send4 = browser.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div[1]/div[2]/form/div[4]/div[1]/span[2]/span[2]/i")
                            browser.execute_script("arguments[0].scrollIntoView();", send4)
                            send4.click()
                            time.sleep(3)
                        except NoSuchElementException:
                            send3 = browser.find_element(By.CLASS_NAME,"ace_content")
                            send3.click()
                            pyautogui.hotkey('ctrl', 'a')
                            pyautogui.press('backspace')
                            pyautogui.press('ctrl','a')
                            pyautogui.press('ctrl', '/')
                            pyautogui.press('enter')
                            for each_line in text:
                                pyautogui.typewrite(each_line)
                            while i <= count:
                                pyautogui.press('delete')
                                i=i+1
                            send4 = browser.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div[1]/div[2]/form/div[4]/div[1]/span[2]/span[2]/i")
                            browser.execute_script("arguments[0].scrollIntoView();", send4)
                            send4.click()
                            time.sleep(3)                
    finally:
        browser.get('https://srmist.codetantra.com/secure/home/tests.jsp')
def before_solving():
    try:
        browser.find_element(By.ID, "termsAcceptedCheckBox").click()
        browser.implicitly_wait(4)
        time.sleep(4)
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/b/div/button[1]').click()
        browser.implicitly_wait(5)
        time.sleep(5)
        question_solving()
    except NoSuchElementException:
        question_solving()
browser = webdriver.Firefox()

# IF USING WITHOUT MAIN FILE

browser.get('https://srmist.codetantra.com/login.jsp')
time.sleep(2)
input_username = "" # user id goes here
input_password = "" # user pass goes here
username = browser.find_element(By.ID, 'loginEmail')
password = browser.find_element(By.ID, 'loginPassword')
username.send_keys(input_username)  
password.send_keys(input_password)  
no_question = [1,2,3,4,5,6,7]  # Array of tests to be solved
send = browser.find_element(By.ID, 'loginBtn')
send.click()
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/div[1]/div/div/div[3]/div"))).click()
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div[1]/div/div/div[1]/div"))).click()
for question_to_do in no_question:
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[8]/div/div/div[2]/div[2]/table/tbody/tr[{question_to_do}]/td[4]/span"))).click()
    before_solving()
browser.close()
browser.quit()

#   IF USING MAIN.PY FILE

# def main_fun(string):
#     xab = str(string)
#     yab = xab.split('~')
#     no_question = []
#     input_username = yab[1]
#     input_password = yab[2]
#     for i in yab[3]:
#         no_question.append(i)
#     browser.get('https://srmist.codetantra.com/login.jsp')
#     time.sleep(2)
#     username = browser.find_element(By.ID, 'loginEmail')
#     password = browser.find_element(By.ID, 'loginPassword')
#     username.send_keys(input_username)
#     password.send_keys(input_password)
#     send = browser.find_element(By.ID, 'loginBtn')
#     send.click()
#     WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/div[1]/div/div/div[3]/div"))).click()
#     WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div[1]/div/div/div[1]/div"))).click()
#     for question_to_do in no_question:
#         WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[8]/div/div/div[2]/div[2]/table/tbody/tr[{question_to_do}]/td[4]/span"))).click()
#         before_solving()
#     browser.close()
#     browser.quit()
# def main(argv):
#    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
#    for opt, args in opts:
#       if opt == '-h':
#          print ('test.py -i <inputfile>')
#          sys.exit()
#       elif opt in ("-i", "--ifile"):
#          inputfile = args
#          main_fun(inputfile) 
# if __name__ == "__main__":
#    main(sys.argv[1:])
