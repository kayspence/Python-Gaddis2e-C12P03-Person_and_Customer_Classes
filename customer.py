__author__ = 'dwight'

import person


class Customer(person.Person):
    def __init__(self, name, address, phone, customer_number, mailing_list_status):
        person.Person.__init__(self, name, address, phone)
        self.customer_number = customer_number
        self.mailing_list_status = mailing_list_status

    def get_customer_number(self):
        return self.customer_number

    def get_mailing_list_status(self):
        return self.mailing_list_status

    def set_customer_number(self, customer_number):
        self.customer_number = customer_number

    def set_mailing_list_status(self, mailing_list_status):
        self.mailing_list_status = mailing_list_status

    def __str__(self):
        super_str = super().__str__()
        cstnm = 'Customer #: ' + self.customer_number + '\n'
        mlok = 'On mailing list: ' + str(self.mailing_list_status) + '\n'

        return super_str + cstnm + mlok
