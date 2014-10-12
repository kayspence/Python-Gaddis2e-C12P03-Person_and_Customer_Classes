__author__ = 'dwight'


class Person():
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_phone_number(self):
        return self.phone

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_phone_number(self, phone):
        self.phone = phone

    def __str__(self):
        nm = 'Name: ' + self.name + '\n'
        addr = 'Address: ' + self.address + '\n'
        ph = 'Phone: ' + self.phone + '\n'

        return nm + addr + ph
