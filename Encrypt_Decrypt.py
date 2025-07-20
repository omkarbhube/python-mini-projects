#encrypt logic - remove the first letter of the word and append it to the end of the word and if the word is less than 3 characters then just reverse it
# and add 3 random characters in the start and end of the word
import random
print("Encryption and Decryption")
text = input("Enter the Text: ")
choice = int(input("1. Encrypt       2. Decrypt"))
random_list = ["rhf","wki","los","dhe","ifn","lok","eyh","omk","ked","qpe"]
if(choice==1):
    if(len(text)<=3):
        rev_text = text[::-1]
        print(rev_text)
    else:
        text_list = text.split(" ") #splits the word and converts it into list
        new_text = []
        for word in text_list:
            prefix = random.choice(random_list)
            suffix = random.choice(random_list)
            words =  prefix + word[1::] + word[0] + suffix
            new_text.append(words)
elif(choice==2):
    if(len(text)<=3):
        straight_text = text[1::]
        print(straight_text)
    else:
        text_list = text.split(" ")
        new_text = []
        for word in text_list:
            original_text = word[3:-3]
            words = original_text[-1] + original_text[0:-1] # in word[0:-1], -1 is used bcuz in str[0:n] it print from 0 to n-1 
            new_text.append(words)
print(" ".join(new_text))
