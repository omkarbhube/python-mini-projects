# a classic game of Kaun Banega Crorepati, where if you answer the question correctly -then you win money!
#just like KBC you have checkpoints wherein if u cross a certain amount then you win that amount of money if you answer wrong
questions = [["How many states are there in India?",29,34,22,19,1],
 ["Where is Mumbai situated?","Haryana","Rajasthan","Maharashtra","Madhya Pradesh",3],
 ["What is the Capital of India?","Mumbai","Surat","Delhi","Kashmir",3],
 ["India is a part of which continent?","South America","Europe","Asia","Australia",3],
 ["Name the only desert in India.","Thar Dessert","Sahara Dessert","Gobi Dessert","Great Sandy Dessert",1],
 ["Which is the tallest mountain in the world?","Mt. Kilimanjaro","Mt. Everest","Mt. Fuji","Mt. Blanc",2],
 ["Kuala Lumpur is the capital of which country?","India","USA","Singapore","Malaysia",4]]

prize_money = [1000,2000,4000,10000,40000,100000,500000]

take_home_money =0      

current_winnings = 0

for i in range(0,len(questions)):
    question = questions[i]
    print(f"\n\nFor Rs. {prize_money[i]}")
    print(question[0])
    print(f"1. {question[1]}         2. {question[2]}")
    print(f"3. {question[3]}         4. {question[4]}")
    ans = int(input("Enter your Answer (1-4): "))
    if(ans == question[5]):
        print("Answer is Correct!!\n")
        print(f"You win Rs. {prize_money[i]}")
        current_winnings = current_winnings + prize_money[i]
        if(prize_money[i] == 2000):
            take_home_money = 2000
        if(prize_money[i] == 10000):
            take_home_money = 10000
        if(prize_money[i] == 100000):
            take_home_money = 100000
        print(f"Your current winnings are {current_winnings}\n")
        choice = int(input("Do you want to continue?  1-YES  2-NO "))
        if(choice == 2):
            print(f"You take home Rs. {current_winnings}")
            break
    else:
        print("Answer is Incorrect")
        print(f"Your Total Takehome money is {take_home_money}")
        break


