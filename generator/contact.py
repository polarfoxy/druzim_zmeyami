import os.path
import jsonpickle
import getopt
import sys
from model.contact import Contact
from random import randint
import random
import string


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_name(length):
    symbols = string.ascii_letters
    return "".join(random.choice(symbols) for i in range(random.randrange(length)))

def random_address(length):
    symbols = string.ascii_letters + string.digits + " "*10
    return "".join(random.choice(symbols) for i in range(random.randrange(length)))

def random_phone():
    return str(randint(10000, 99999))

def random_email(length):
    symbols = string.ascii_letters + string.digits
    return "".join(random.choice(symbols) for i in range(random.randrange(1, length))) + "@" + \
           "".join(random.choice(symbols) for i in range(random.randrange(1, length))) + ".com"

testdata = [
    Contact(firstname=random_name(7), lastname=random_name(10), address=random_address(20),
            home=random_phone(), work=random_phone(), phone2=random_phone(),
            email=random_email(5), email2=random_email(6), email3=random_email(7))
    for i in range(3)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))