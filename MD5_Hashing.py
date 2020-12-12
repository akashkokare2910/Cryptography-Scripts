import hashlib 

Hash_Object = input("Enter Hash Object Here --> ")
result =  hashlib.md5(b'Hash_Object') 

  
# printing the equivalent byte value. 
print("The byte equivalent of hash is : ", end ="") 
print(result.digest()) 

  
string_to_hash = input("Enter string to hash --> ")
  
result = hashlib.md5(string_to_hash.encode()) 
  
# printing the equivalent hexadecimal value of hash
print("The hexadecimal equivalent of hash is : ", end ="") 
print(result.hexdigest()) 
