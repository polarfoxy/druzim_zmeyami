# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randint
import pytest
import random
import string



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

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count()


