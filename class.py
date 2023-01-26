from datetime import date


class Contact(object):
    
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.creation_date = date.today()
    
    def update(self, phone):
        self.updated_date = date.today()
        self.phone_number = phone