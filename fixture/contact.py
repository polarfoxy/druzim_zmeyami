from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//a[@href='edit.php']").click()
        self.fill_form(contact)
        wd.find_element_by_name("submit").click()
        self.app.open_home_page()
        self.contact_cache = None

    def fill_form(self, contact):
        self.type("firstname", contact.firstname)
        self.type("lastname", contact.lastname)
        self.type("address", contact.address)
        self.type("home", contact.home)
        self.type("mobile", contact.mobile)
        self.type("work", contact.work)
        self.type("phone2", contact.phone2)

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        return wd.find_elements_by_name("entry")[index]

    def modify_by_index(self, contact, index):
        wd = self.app.wd
        self.app.open_home_page()
        element = self.select_contact_by_index(index)
        element.find_element_by_css_selector("[src='icons/pencil.png']").click()
        self.type("firstname", contact.firstname)
        self.type("lastname", contact.lastname)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contact_cache = None


    def delete_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        element = self.select_contact_by_index(index)
        element.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None


    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                id = cells[0].find_element_by_css_selector("input").get_attribute("id")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname,
                                                   all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails, id=id))
            return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = wd.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, home=homephone, mobile=mobilephone,
                       work=workphone, phone2=secondaryphone, email=email, email2=email2,
                       email3=email3, id=id)


    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        content = wd.find_element_by_css_selector("div[id='content']")
        emails = content.find_elements_by_tag_name("a")
        email = emails[0].text
        email2 = emails[1].text
        email3 = emails[2].text
        return Contact(home=homephone, mobile=mobilephone, work=workphone, phone2=secondaryphone,
                       email=email, email2=email2, email3=email3, id=id)
