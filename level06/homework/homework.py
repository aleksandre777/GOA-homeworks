# 1)მომხმარებელს შემოატანინეთ ორი რიცხვი,შეადარეთ ეს ორი რიცხვი ერთმანეთს(გამოიყენეთ შედარების ოპერატორები(>, <, ==)

num1=int(input("enter your number")) 
num2=int(input("enter your number")) 
print(num1>num2) 
print(num1<num2) 
print(num1==num2) 

# 2)შექმენით 5 ცვლადი,3 ცვლადში შეინახეთ რიცხვები რომლებიც იქნებაინ სტრინგის ტიპის,დანარჩენ 2 ცვლადში შეინახეთ ჩვეულებრიბი ინტეჯერები,შენი დავალებაა იპოვო ამ ხუთი რიცხვის ნამრავლი,შემდეგ ეს ნამრავლი გაყავი რიცხვების რაოდენობაზე და დაპრინტე საბოლოო შედეგი,გამოიყენე შეაბამისი ფუნქცია რომ გადააქციო სტრინგი რიცხვები ინტეჯერად

num1=int("90") 
num2=int("80")
num3=int("40")
num4=50
num5=4 
print((num1*num2*num3*num4*num5)/5) 

# 3)მომხმარებელს შემოატანინეთ სამი სტრინგ ტიპის მნიშვნელობა ასევე შემოატანინეთ ერთი ინტეჯერი,თქენი დავალებაა მომხმარებლის მიერ შემოყვანილ სამ სტრინგზე მოახდინოთ კონკატინაცია და შეინახოთ ცალკე ცვლადში ეს სამი გადაბმული სტრინგი,კონკატინაციის შემდეგ კი გაამრავლეთეს ეს მთლიანი სტრინგი მომხმარებლის მიერ შემოყვანილ რიცხვზე

num1=input("enter your number")
num2=input("enter your number")
num3=input("enter your number")
num4=int(input("enter your number")) 
print(num1+num2+num3) 

num5=908070
print(num5*num4) 

# ჩვენ ვისწავლეთ ორი სახის ოპერატორი and , or 
# or ის გამოყენების უპრიატესობა true ს ენიჭება 
# and ის გამოყენებისას false ს

# 5)გვერდით მიუწერეთ რას გამოიტანს შემეგი ოპერაციები
#    (and)                             (or)
# True and True --true         True or True -- true           
# True and False -- false     |   True or False -- true
# False and True -- false     |   False or True -- true
# False and False -- false    |   False or False -- false  


# 6)მოიყვანე მაგალითები and და or ოპერატორებზე,დაპრინტე და გაუშვით ტერმინალში 


             
True and True -- True                
True and False -- False   |   True or False -- True
False and True -- False |   False or True -- True
False and False -- False   |   False or False -- False

# 7)შექმენი 4 ცვლადი სადაც შეინახავთ სხვადასხვა მონაცემთა ტიპებს და შენი დავალებაა რომ გაიგო ამ ცვლადებში შენახული მონაცემების ტიპები(გამოიყენეთ შესაბამისი ფუნქცია)

school = "Greenschool"
height = 163 
plane_ticket = 250.12 
honesty= True
print(type(school))
print(type(height))
print(type(plane_ticket))
print(type(honesty))

# 8)მომხმარებელს შემოატანინე 3 მნიშნველობა,ერთის ტიპი იყოს float ერთის integer ერთის string და დაპრინტეთ ისინი(გამოიყენეთ შესაბამისი ფუნქციები რომ შემოყვანილ მნიშვნელობებს ქონდეთ შესაბამისი ტიპი(note:მომხმარებელს რომ შემოყავს მნიშვნელობა თავიდან ყოველთვის არის სტრინგი),თუ ფლოათს
#  შემოიყვანს მომხმარებელი გახადეთ ინფუთი floaT ტიპის თუ ინტეჯერს შემოიყვანს გახადეთ ინფუთი ინტეჯერ ტიპის
 







