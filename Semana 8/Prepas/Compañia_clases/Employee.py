from unicodedata import name


class Employee:
    def __init__(self,name,title):
        self.name=name
        self.title=title


    def get_name(self):
        return self.name

    def set_name(self,n):
        self.name=n

    def get_title(self):
        return self.title

    def set_title(self,t):
        self.title=t