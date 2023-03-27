import os

string_user = "" # user id goes here
string_pass = ""  # user password goes here
list1 = [1]  # array of test to be done
str1 =''
for abc in list1:
    str1+=str(abc)
bashCommand = f'python -u "d:\\Projects\\Codetantra_Bot\\srmist_bot_writing.py" -i ~{string_user}~{string_pass}~{str1}'
os.system(bashCommand)
