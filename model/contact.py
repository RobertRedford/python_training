from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, home=None, mobile=None, work=None, phone2=None, id=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.home = home
        self.mobile = mobile
        self.work = work
        self.phone2 = phone2
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s: %s: %s " % (self.firstname, self.lastname, self.id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
