'''
Created on August 1, 2020
Mobile phone validation
@author: Ritu Kukreja
'''

import re #importing Regex function

class MobileValidation:

    # init method to initialze the object of MobileValidation
    def __init__(self):

        #Importing mobile number from user
        self.n = input("Enter mobile number to check for validation: ")

    # check_mobilenumber method to validate a number
    def check_mobilenumber(self):
        regex= "^[7-9][0-9]{9}$" #A valid regex expression

        #Checking input mobile number with regex expression
        if re.search(regex, self.n):
            print("Valid")
        else:
            print("Invalid")

#Creating object of the class
def main():
    obj = MobileValidation()
    obj.check()


if __name__=="__main__":
    main()
