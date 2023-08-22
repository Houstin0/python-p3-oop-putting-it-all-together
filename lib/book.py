#!/usr/bin/env python3

class Book:
    
    def __init__ (self,title,page_count):
        self.title=title
        self._page_count=page_count

    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self,page_count):
        if type(page_count) == int:
            self._page_count=page_count
        else:
            print("page_count must be an integer") 

    page_count=property(get_page_count,set_page_count)  

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")         

joy=Book("And Then There Were None",272)
print(joy.page_count)
ben=Book("The World According to Garp", 69)
ben.turn_page()


    
        