#if berguna melakukan perintah jika kondisinya True
#else berguna jika kondisi if adalah False maka menjadikan else True

age = int(input("Enter your age: "))

if age >= 100:
    print("You are to old")
elif age >= 18:
    print("You signup!")
elif age < 0:
    print("You dont have age lol")
else:
    print("You can't make a credit card now")
