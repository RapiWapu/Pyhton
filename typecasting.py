#typecasting itu proses mengubah nilai dari sebuah tipe variabel ke tipe variabel yang lain
#menggunakan str(), int(),float(),bool()

my_name = "Raffi"
my_age = 16
my_gpa = 89.78
iam_student = True

#jadi diatas ada beberapa variabel bisa kita ganti sesuka hati

my_name = bool(my_name)
my_age = str(my_age)
my_gpa = int(my_gpa)

#kita bisa mnggunakan perintah type untuk mengetahui tipe variabel yang telah di ubah tersebut

print(type(my_age))
print(my_age)

print(type(my_gpa))
print(my_gpa)

#jika di dalam variabel my_name ada isinya yaitu "Raffi" maka hasil di output adalah True karena ada isinya
#sebaliknya jika di dalam variabel my_name kosong "" maka hasilnya akan False karena tidak ada isinya

print(type(my_name))
print(my_name)
