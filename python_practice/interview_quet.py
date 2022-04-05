# """intro"""
# """Write a program to find the length of the string without using inbuilt function (len)"""
# count = 0
# string_ = "mohana kasi"
# for char in string_:
#     count += 1
# print(count)
#
# def

"""checking the link is broken or not using package requests"""
# from selenium import webdriver
# from requests import request
# driver = webdriver.Chrome(".\chromedriver.exe")
# response = request("GET","https://www.amazon.in/") # request will hit the link given and gives the response back
# print(response)
# print(dir(response))
# print(type(response)) # response we b element contains a attribute status_code
# print(type(response.status_code)) # status_code is always integer only i.e of 200 or 400 like that
# print(response.status_code)
#
# if response.status_code == 200:
#     print("the link is working fine")
# else:
#     print("the link is broken")


"""checking multiple links"""
# links = driver.find_element_by_xpath("//a")
# all_links = [item.get_attribute("href") for item in links]
# for link in all_links:
#     response = request("GET", link)
#     if response.status_code == 200:
#         print("heart is working fine")
#     else:
#         print("heart is broken")
#

import json
# res = request("GET", "https://ifsc.razorpay.com/SBIN0004758")
# print(res.text)
# expec_branch = json.loads(res.text)
# print(type(expec_branch))
# print(expec_branch['BRANCH'])
# assert 'SANGADIGUNTA' in expec_branch['BRANCH']



# res = request("GET", "https://ifsc.razorpay.com/SBIN0004758")
# print(res.text)
# expec_branch = json.loads(res.text)
# print(type(expec_branch))
# print(expec_branch['BRANCH'])
# assert 'SANGADIGUNTA' in expec_branch['BRANCH']
#

"""Write a program to reverse a string without using any inbuilt functions."""
s = 'mohana kasi'
res = ''
for char in s:
    res = char + res
# print(res)

"""Write a program to replace one string with another. e.g. "Hello World" replace "World" with "Universe"""
s = "hello world"


"""Write program to read a random line in a file. (ex. 50, 65, 78th line)"""
path = r"C:\Users\Hp\PycharmProjects\Kasi_Python_TestYantra\my_files\text files\sindhu12.txt"
# count = 0
n = 15
# with open(path) as file:
#     for line in file:
#         count += 1
#         if count == n:
#             print(line)

# from itertools import islice
# with open(path) as file:
#     print(list(islice(file, n, n+1)))

# with open(path) as file:
#     for line_no, line in enumerate(file):
#         if line_no == n:
#             print(line)


"""Write program to read a random lines in a file. (ex. I want read all lines 10th to 15th line)"""
from itertools import islice
n = 10
# with open(path) as file:
#     line = islice(file, n, n+5)
#     print(list(line))

"""Program to print last "N" lines of a file."""
from collections import deque
n = 5
# with open(path) as file:
#     n_lines  = deque(file, n)
#     for line in n_lines:
#         print(line)

"""Write a program to search for a character in a given string and return the corresponding index"""
char = 's'
def temp_str(string_):
    for index, item in enumerate(string_):
        if char == item:
            print(char, index)

temp_str('kasi')

"""write a decorator that returns only postive values after substraction"""
def samp(func):
    def warpper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res <0:
            return abs(res)
        return res
    return warpper
@samp
def sub(a, b):
    return a - b
# print(sub(2,8))




class C_instance:
    instance_count = 0
    def __init__(self):
        C_instance.instance_count += 1


# a = C_instance()
# b = C_instance()
# c = C_instance()
# print(C_instance.instance_count)

"""Write a function which takes a list of strings and integers.If the item is a string it should print as is and if the item is integer of float it should reverse it"""
def st_num(list_):
    for item in list_:
        if isinstance(item, str):
            print(item)
        elif isinstance(item, (int, float)):
            print(str(item)[::-1])
# st_num([1,2,3,'kasi',83.3])
class Simple:
    def __init__(self, items):
        self._items = items

    def __iter__(self):
        return iter(self._items)
c = Simple([1,2,3,4])
for item in c:
    print(item)
#Write a python program to get the below output o/p should be "iH woH era uoy"""
sentence = "Hi How are you"
res = ''
for word in sentence.split():
    res += word[::-1]
    res += ' '
# print(res)

#Write a python program to get the below output

sentence = "Hi How are you"
#o/p should be "ouy era woH iH"

print(sentence[-2:]+sentence[:len(sentence)-2][::-1])
#Write a lambda function to add two numbers (a, b)
res = lambda a,b: a+b
print(res(10,20))


