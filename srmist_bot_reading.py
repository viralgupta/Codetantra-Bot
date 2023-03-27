# Add your user id and password to 92 and 93 line
import time
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire.utils import decode
import re
import os

def file_name(info):
    for file_name in os.listdir('D:/Projects/Codetantra_Bot/'):
        if file_name.startswith(info):
            return file_name
def answer_add(filename,answer):
    with open(f"D:/Projects/Codetantra_Bot/{filename}.txt", mode = "a") as file1:
        file1.truncate(0)
        file1.write(answer)
        file1.close()
        with open(f'D:/Projects/Codetantra_Bot/{filename}.txt', mode='r') as f1:
            data = f1.read()
            data = data.replace(r'\\\\n', r'\n')
            data = data.replace(r'\\n', '\n')
            data = data.replace(r'\\t', '    ')
            data = data.replace(r'\\"', '"')
            data = data.replace(r"\'", "'")
            data = data.replace(r'\\\\', '\\')
            with open(f"D:/Projects/Codetantra_Bot/{filename}.txt", mode = "a") as f2:
                f2.truncate(0)
                f2.write(data)
                f2.close()
def answer_getting():
    WebDriverWait(browser, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'modal-backdrop fade')))
    WebDriverWait(browser, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'preloader-box')))
    WebDriverWait(browser, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'preloader-dot')))
    browser.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div[4]/div/div/div[2]/div[2]/button").click()
    WebDriverWait(browser, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'modal-backdrop fade')))
    WebDriverWait(browser, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'preloader-box')))
    WebDriverWait(browser, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'preloader-dot')))
    uncut_url = browser.current_url
    cut_url = uncut_url.split('&')[1]
    try:
        for request in browser.requests:
            if request.url == f'https://srmist.codetantra.com/secure/rest/qhs/gnqit?{cut_url}':
                body = str(decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity')))
                question_name = re.findall('{ "filesContentArr" : \[ { "fileName" : "([^"]*)" , "fileContent" : ', body)
                lentimespent = re.findall('{ "markForReview" : ([^"]*) , "answeredAndMarkForReview" :', body)
                question_no = len(lentimespent)
                lst = [i for i in body.split('"markForReview"', maxsplit=1)][1]
                for_lst=[]
                for for_loop_counter in range(question_no-1):
                    xyzabc = [i for i in lst.split('"markForReview"', maxsplit=1)]
                    for_lst.append(xyzabc[0])
                    lst = xyzabc[1]
                xyzabcd = [i for i in lst.split('"responsesMap"')]
                for_lst.append(xyzabcd[0])
                correct_list=[]
                for i in for_lst:
                    if "firstCorrectAnswerSubmittedTime" in i:
                        correct_list.append(1)
                    else:
                        correct_list.append(0)
                answer_str = xyzabcd[1].split('multiLanguageResponsesMap')[0]
                answer_lst = []
                answer_str_1 = answer_str.split(', "fileContent" : "')
                for i in range(1,len(answer_str_1)):
                    if '"}]} , "' in answer_str_1[i]:
                        answer_lst.append(answer_str_1[i].split('"}]} , "')[0])
                    elif '" , "readOnlyRanges"' in answer_str_1[i]:
                        answer_lst.append(answer_str_1[i].split('" , "readOnlyRanges"')[0])
                    elif r'"}]}} , "' in answer_str_1[i]:
                        answer_lst.append(answer_str_1[i].split(r'"}]}} , "')[0])
                for i in range(len(correct_list)):
                    if correct_list[i] == 1:
                        answer_add(question_name[i],answer_lst[i])
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
        answer_getting()
    except NoSuchElementException:
        answer_getting()

no_question = [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 17, 18, 19, 20, 22, 23, 24]  #Array of test no. to search
input_username = "" #user id goes here
input_password = ""  #password goes here
browser = webdriver.Firefox()
browser.get('https://srmist.codetantra.com/login.jsp')
#bypassing kaspersky
# WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, "showDetails")))
# browser.find_element(By.ID, "showDetails").click()
# browser.find_element(By.XPATH, "/html/body/table/tbody/tr/td/div/table/tbody/tr/td[2]/div/div/p[4]/a").click()
time.sleep(2)
username = browser.find_element(By.ID, 'loginEmail')
password = browser.find_element(By.ID, 'loginPassword')
username.send_keys(input_username)
password.send_keys(input_password)
send = browser.find_element(By.ID, 'loginBtn')
send.click()
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/div[1]/div/div/div[3]/div"))).click()
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div[1]/div/div/div[1]/div"))).click()
for question_to_do in no_question:
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[8]/div/div/div[2]/div[2]/table/tbody/tr[{question_to_do}]/td[4]/span"))).click()
    before_solving()
browser.close()
browser.quit()
