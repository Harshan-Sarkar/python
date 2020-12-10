class Atm:
    machine = "money Transfer machine"
    def add(self):
        bankbalance[self.b] = bankbalance[self.b] + self.plus
        print(f"Your Current Balance is {bankbalance[self.b]}")
    def diff(self):
        bankbalance[self.b] = bankbalance[self.b] - self.plus
        print(f"Your Current Balance is {bankbalance[self.b]}")
    def balance(self):
        print(f"Your Current Balance is {bankbalance[self.b]}")
data = {
    "Anuj" : "9578",
    "Anup" : "1567"
}
bankbalance = {
    "9578":7000,
    "1567":2000
}
atm = Atm()
atm.a = input("Enter your name: ")
atm.b = None
if data[atm.a] == False:
    print("You dont have a account in this bank")
else :
    while atm.b != data[atm.a]:
        atm.b = input("Enter your password: ")
        if atm.b == data[atm.a]:
            print("Welcome to ATM")
            break
        else:
            print("Your Password is incorrect. Please renter your password")
atm.c = None
while atm.c == None:
    atm.c = input('''Press 1 For Credit
Press 2 For Withdrawl
Press 3 For Balance Enquiry\n''')
    if atm.c == "1":
        atm.plus = int(input("Enter the balance of input: "))
        atm.add()
    if atm.c == "2":
        atm.plus = int(input("Enter the balance you want to take: "))
        atm.diff()
    if atm.c == "3":
       atm.balance()
print("-----Thank you for visiting us-----")
