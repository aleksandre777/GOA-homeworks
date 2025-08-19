#2) კომენტარების სახით თავიდან ახსენით რა არის conditional statement, რა დანიშუნლება გააჩნიათ და როგორი სახის განცხადებები გვაქვს.
# condational statements ნიშნავს პირობითი განცხადებები გვეხეხმარება განვასხვაოთ ინფორამციები ერთმანეთისგან

#3) for ციკლის მეშვეობით გამოიტანეთ "hello world" 50-ჯერ.
for i in range(51):
    print("hello world") 

#4) while ციკლის მეშვეობით გამოიტანეთ რიცხვები 3-დან 17-ის ჩათვლით.
num = 3
while num<= 15:
    print(num)
    num=1+num
    
#5) მომხმარებელს შემოატანინეთ პაროლი, შემდეგ კი შედეგი შეინახეთ ცვლადში. შექმენით პირობა თუ ის უდრის "1234"-ს დაბეჭდეთ "Password is correct", სხვა შემთხვევაში დაბეჭდეთ "Password is incorrect".

password = input("type your password") 
if password == "1234":
    print("password is correct")
else:
    print("access denied")
#6) შექმენით ცვლადი სადაც შეინახავთ მომხმარებლის მიერ შემოყვანილი ცხოველის სახეობას. თუ სახეობა უდრის "ძაღლი" დაბეჭდეთ "woaf! woaf!", სხვა შემთხვევაში "შენ არ გყავს ძაღლი"
specie = input("enter ur specie in")
if specie == "dog":
    print("woaf!woaf!")
else:
    print("u dont have a dog")