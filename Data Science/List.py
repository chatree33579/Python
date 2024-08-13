Mylist = [['Chazam','Chasea'],'Bird','Cat','Cat','Cat']

""" 
# 1. Recalling

Chazam = Mylist[0][0]
Slicing = Mylist[0:3:2] #[First data : After Final data : step]
""" 

""" 
# 2. Adding

Append = Mylist.append('Doctor') #Adding data in list after last index
Insert = Mylist.insert(2, 'Dog') #Adding data in the position sastified
Extended = Mylist.extend(["Frog", "Turtle"]) #Connecting List + List
""" 

""" 
3. Removing

# Remove = Mylist.remove("Bird") #Removing specific data which we want to delete
# Pop = Mylist.pop(0) #Removing data at specific index and return the data removed
""" 

""" 
# 4. Deleting

Clear = Mylist.clear() # Delete all member in list
del Mylist # Deleting List to be not defined
""" 

""" 
# 5. Copy List

Mylist2 = Mylist.copy() # Copy list to the another list
print(Mylist2)
""" 

""" 
# 6. Changing type of data to be list

Mylist3 = list(("Pa","Mama"))
Mylist4 = list({2,3,4})
print(Mylist3,Mylist4)
""" 

""" 
# 7. Counting List

Counting_all = len(Mylist) # Counting the number of members in list
print(Counting_all)
Counting_cat = Mylist.count('Cat')
print(Counting_cat) 
Index = Mylist.index('Cat')
print(Index)
""" 

""" 
# 8. Sorting List

List = [1,3,2,7,4,6,5,9,10,8]
List.sort()
List1 = [1,3,2,7,4,6,5,9,10,8]
List1.sort(reverse=True)
print(List1,List)

""" 

""" 
# 9. 


""" 