# making a  bank

#how much money does he have in bank

money = int(input("how much money do you have on balance: "))

#what does user  want to do

choice = input("do you want to deposit or withdraw: ")

#making withdraw machine



if(choice == "withdraw"):
    withdraw = int(input("how much money do you want to withdraw:"))
    balance = (money - withdraw)
    print("you have withdrawen " + str(withdraw) + " now you have " + str(balance) + " on your account")
else:
    deposit = int(input("how much money do you want to deposit: "))
    money2 = deposit + money
    print("coonngrats you have deposited " + str(deposit) + " now you have " + str(money2))