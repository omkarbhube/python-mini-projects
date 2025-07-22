# This program simulates the Minion Game played with a given string.
# Stuart scores points for substrings that start with consonants.
# Kevin scores points for substrings that start with vowels (A, E, I, O, U).
# Instead of generating all substrings, the program calculates the 
# number of substrings starting at each index and adds points accordingly.
# The player with the higher score is declared the winner.
# The input string should be in uppercase.
def minion_game(string):
    kevin_score = 0
    stuart_score = 0
    vowels = 'AEIOU'
    length = len(string)
    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length -i
    
    if(kevin_score > stuart_score):
        print(f"Kevin {kevin_score}")
    elif(stuart_score > kevin_score):
        print(f"Stuart {stuart_score}")
    else:
        print("Draw") 
if __name__ == '__main__':
    s = input("Enter a String: (uppercase only) ").upper()
    minion_game(s)