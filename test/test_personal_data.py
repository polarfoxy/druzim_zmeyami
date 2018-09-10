import random


def test_personal_data(app):
    index = random.randint(0,app.contact.count())
    data_from_home_page = app.contact.get_contacts_list()[index]
    data_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert data_from_home_page.firstname == data_from_edit_page.firstname
