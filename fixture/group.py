from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def go_to_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))):
            wd.find_element_by_xpath("//a[@href='group.php']").click()

    def add(self, group):
        wd = self.app.wd
        self.go_to_group_page()
        wd.find_element_by_name("new").click()
        self.fill_form(group)
        wd.find_element_by_name("submit").click()
        self.go_to_group_page()
        self.group_cache = None

    def fill_form(self, group):
        self.type("group_name", group.name)
        self.type("group_footer", group.footer)

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_group(self):
        self.select_group_by_index(self, 0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def mod_group_by_index(self, group, index):
        wd = self.app.wd
        self.go_to_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.type("group_name", group.name)
        wd.find_element_by_name("update").click()
        self.go_to_group_page()
        self.group_cache = None

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.go_to_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.go_to_group_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.go_to_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.go_to_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
