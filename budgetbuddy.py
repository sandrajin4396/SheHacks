#!/usr/bin/env python
# coding: utf-8

# In[10]:


class Profile:
  ''' Sets up user profile based on: name, location, occupation, and 
      specified spending categories
  '''
  def __init__(self, name, i_location, i_occupation):
    self.symbol = name
    self.location = [i_location]
    self.occupation = [i_occupation]
    
  def __eq__(self, other):
    return (isinstance(other, Person) and
            self.symbol == other.symbol and
            self.location == other.location and
            self.occupation == other.occupation)
  
  def __repr__(self):
    return "Profile: {0},{1},{2}".format(self.symbol, self.location, self.occupation)
  

s_categories = ["Food\t", "Travel/leisure", "Clothes", "Entertainment", "Education"]

class Categories:
  '''Sets up spending categories'''
  
  def __init__(self,name,total):
    self.name = name
    self.total = 0
  
def MainMenu():
  print()
  action = input("Main Menu \n--Type number to choose option--\n\n (1)Add entry \n (2)See Report \n (X)Exit\n").upper()
  while not action in '12X':
    action = input('Please try again ').upper()
  return action

def add_entry(totals):
  category = input("Choose a category: \n\n (1)Food \n (2)Travel/Leisure \n (3)Clothes \n (4)Entertainment \n (5)Education\n")
  while not category in '12345':
    category = input('Please try again ')
  category = int(category)
  print()
  n = int(input("How much money did you spent? "))
  totals[category-1] += n
  return totals

def summary(totals):
  if not sum(totals) == 0:
      percents = [i/sum(totals)*100 for i in totals]
      print()
      print("Here is your updated summary report: ")
      print(" Category \t Total Spent \t Percentage of Total Spending")
      for i in range(len(totals)):
        print(s_categories[i],'\t\t',totals[i],'\t\t',percents[i])
  else:
    print('You have not spent any money yet')
  
def main():
  food = Categories("Food",0)
  travel = Categories("Travel/Leisure",0)
  clothes = Categories("Clothes",0)
  entertain = Categories("Entertainment",0)
  edu = Categories("Education",0)
  
  totals = [food.total,travel.total,clothes.total,entertain.total,edu.total]

  use = True
  
  while use == True:
  
    act = MainMenu()
    if act == '1':
      print()
      add_entry(totals)
      summary(totals)
      print()
      again = input("Would you like to add another entry? (Y/N) ").upper()
      while not again in 'YN':
        again = input('Please try again ').upper()
      if again == 'Y':
        add_entry(totals)
        summary(totals)
      elif again == 'N':
        MainMenu()
    elif act == '2':
        print()
        summary(totals)
    
    if act == 'X':
      use = False
      
main()


# In[ ]:





# In[ ]:





# In[1]:


e


# In[ ]:




