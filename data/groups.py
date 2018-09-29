from model.group import Group
import random
import string

testdata = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]



#def random_string(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
#    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#testdata = [Group(name="", footer="")] + [
#    Group(name=random_string("name", 10), footer=random_string("footer", 10))
#    for i in range(5)
#]