from model.contact import Contact
from random import randrange


def test_mod_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="131", middlename="werwer", lastname="11", nickname="hhjhj",
                               title="hj", company="jjjjj", home="hhh", address="hhh", mobile="hhh",
                               work="hhhh", fax="hhhhh", email="hhhhh", email2="hhhhh", email3="hhhh", homepage="hhhhh",
                               byear="2000", ayear="2000", phone2="11111", address2="111111", notes="11111")
    contact.id = old_contacts[index].id
    app.contact.modify_by_index(contact, index)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


