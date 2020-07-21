import os
import random

BASE = os.getcwd()
PATH = r"D:\Python_files\files"
os.chdir(PATH)
os.chdir(os.path.join(PATH,"cleaned"))
print(os.getcwd())

f_names = []
l_names = []

with open("first_names.txt") as f :
    for line in f :
        f_names.append(line[:len(line)-1])
with open("surnames_cleaned.txt") as f :
    for line in f :
        l_names.append(line[:len(line)-1])

def get_name():
    return random.choice(f_names),random.choice(l_names)

def get_username(name):
    return str(name[0]+name[1]+str(random.randint(1,1000)))

def get_email(name):
    n = random.randint(1,10000)
    fname,lname = name[0],name[1]
    hosts = ["gmail","yahoo","rediffmail","outlook"]
    rhost = random.choices(hosts,weights=[10,8,5,4])
    email = fname + lname + str(n)+ "@" + rhost[0] + ".com"
    return email

def get_pass():
    return "Methylene"

# for i in range(10,12):
#     name= get_name()
#     print(name)
#     print(get_email(name))
#     print(get_username(name))
#     pass
