// kegunaan userinput adalah pengguna bisa mengisi data dari variabel tersebut 
// default dari input ini adalah str() atau string(), jadi kita perlu casting jika ingin mengubahnya seperti variabel age

user = input("What is your name?: ")
age = int(input("What is your age?: "))

print(f"Hallo {user}")
print(f"Your age is {age}")
