# Example with dictionary

dict_example ={'a':1,'b':2,'c':3,'d':4}


#clear() - removes all items from the dictionary
#dict_example.clear()
#print("dictionary after clear():",dict_example)
#
# # reinitialize dictionary for other example
#dict_example ={'a':1,'b':2,'c':3,'d':4}
#dict_copy= dict_example.copy()
#print("dictionary copy:",dict_copy)


#fromkeys()- returns a dictionary with specified and their associated values
keys = ['e','f','g']
default_values =0
new_dict =dict.fromkeys(keys,default_values)
print("new dictionary with from keys():",new_dict)

#get() - returns the value associated with the specified key
print("values for key b :",dict_example.get('b')) #output:2

#items()- returns a view object displaying the dictionary's key-value pairs
print("dictionary items:",dict_example.items())

#keys() - returns a view object displaying all the dictionary's keys
print("dictionary keys:",dict_example.keys())

#pop() -removes the specified key and return the associated value
popped_values = dict_example.pop('b')
print("popped value for key 'b':",popped_values)
print("dictionary after pop():",dict_example)


last_item = dict_example.popitem()
print("popped last item:",last_item)
print("dictionary after popitem()",dict_example)

#setdefault() - returns the value for the specified key, and if not found inserts it with a default value
print("values for key 'z' with setdefault:",dict_example.setdefault('z',100))
print("dictionary after setdefault():",dict_example)

#update()- updates the dictionary with elements from another dictionary or iterable
new_data ={'x':10,'y':20}
dict_example.update(new_data)
print("dictionary after update():",dict_example)

#values() - returns a view object displaying all the dictionary's values
print("dictionary values:",dict_example.values())









