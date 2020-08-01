'''
Created on August 1, 2020
Mobile phone validation
@author: Ritu Kukreja
'''

class Enterlist():

    # init method to initialze the object of Enterlist
    def __init__(self):
        #Number of elements 
        self.n = int(input("Enter number of elements in the list : "))

        #Below lines read inputs from user using map() function 
        self.a = set(list(map(str,input("\nEnter the elements of first list : ").split()))[:self.n])
        self.b = set(list(map(str,input("\nEnter the elements of second list : ").split()))[:self.n])

    # differentiate method to remove common elements from joined list
    def differentiate(self):
        common_elements = self.a.intersection(self.b) #Intersecting sets
        final_set = self.a.union(self.b)  #Union of 2 sets
        final_set.difference_update(common_elements) #Removing common elements from both the list
        final_list = list(final_set) #Casting set to list
        final_list.sort()  #Sorting of list
        print(final_list)

#Creating object of the class
def main():
    obj = Enterlist()
    obj.differentiate()

if __name__=="__main__":
    main()
