from unicodedata import name


class Company:
    def __init__(self,name):
            self.name=name

    def get_name(self):
        return self.name

    def set_name(self,n):
        self.name=n