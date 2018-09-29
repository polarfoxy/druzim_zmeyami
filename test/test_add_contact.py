# -*- coding: utf-8 -*-
from model.contact import Contact




# @pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contacts_list()
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count()


