__author__ = 'dwight'

# Write a class named Person with data attributes for a person’s name, address, and telephone number. Next, write a
# class named Customer that is a subclass of the Person class. The Customer class should have a data attribute for a
# customer number and a Boolean data attribute indicating whether the customer wishes to be on a mailing list.
# Demonstrate an instance of the Customer class in a simple program.

import customer


def main():
    name = 'Jonathan Davis'
    address = 'Somewhere, USA'
    phone = '(555) 555-5555'
    customer_number = '54321'
    bool_mailing_list = False
    my_customer = customer.Customer(name, address, phone, customer_number, bool_mailing_list)

    print(my_customer.get_name())
    print(my_customer.get_address())
    print(my_customer.get_phone_number())
    print(my_customer.get_customer_number())
    print(my_customer.get_mailing_list_status())
    print()
    print(my_customer)

    my_customer.set_name('Malik Taylor')
    my_customer.set_address('Somewhere Else, USA')
    my_customer.set_phone_number('(444) 555-4444')
    my_customer.set_customer_number('98765')
    my_customer.set_mailing_list_status(True)
    print(my_customer)


main()
