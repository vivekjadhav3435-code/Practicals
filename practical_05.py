data = {}
print("Empty dictionary:", data)

#Ask how many items to add
n=int(input("How many items do you want to add? "))

#Add key-value pairs
for i in range (n):
    key= input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value
    print("Dictionary after adding items:", data)

#Update a key's value

update_key = input("Enter key to update: ")

if update_key in data:
    new_value = input("Enter new value: ")
    data[update_key] = new_value
    print("Value updated")
else:
    print("Key not found")
 # Retrieve value using key (normal method)

search_key = input("Enter key to retrieve value: ")

if search_key in data:
    print("Value:", data[search_key])
else:
    print("Key not found")

#Retrieve value using get() I

get_key = input("Enter key to retrieve using get(): ")

value = data.get(get_key)

if value is not None:
    print("Value:", value)
else:
    print("Key not found")

#Delete a key-value pair

delete_key = input("Enter key to delete: ")

if delete_key in data:
    del data[delete_key]
    print("Key-value pair deleted")
else:
    print("Key not found")