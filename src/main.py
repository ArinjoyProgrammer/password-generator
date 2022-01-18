from email import message
import random
import variables
import welcoming


class PaswordGen:
    def passGenWork():

        welcome = welcoming.message
        print(welcome)

        password = [variables.d1, variables.d2, variables.d3, variables.d4, variables.d5, variables.d6, variables.d7, variables.d8, variables.d9, variables.d10]
        
        print("Your Random Password is generated bellow:")

        for items in password:
            print(items, end='')
    
    passGenWork()
