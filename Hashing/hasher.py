import hashlib



# print(hashlib.algorithms_available) # display all the hashing algorithms
# print("\n")
# print(hashlib.algorithms_guaranteed) # display the best hashing algorithms

text = "hello mate"
encoded_text = hashlib.sha1(text.encode())
print(encoded_text.hexdigest())

