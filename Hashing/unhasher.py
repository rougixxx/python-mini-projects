import hashlib


def unhash():
    hashed_message = str(input("Enter Your  Hashed Message: "))
    f = open("wordlist", 'r')
    for line in f:
        text = line.split()[0]
        encoded_txt = hashlib.md5(text.encode())
        genrated_hash = encoded_txt.hexdigest()
        if genrated_hash == hashed_message:
            print(f"[+] Your Message is ====>>> {text}")
    
    f.close()

unhash()