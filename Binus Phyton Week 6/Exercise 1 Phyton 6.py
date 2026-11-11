class Student:
    "Class biodata mahasiswa"

    def __init__(self, name="-", npm="-", major="-", age=0, address="-"):
        self.name = name
        self.npm = npm
        self.major = major
        self.age = age
        self.address = address

    def displayBiodata(self):
        print("\n===== Biodata Mahasiswa =====")
        print("Nama    :", self.name)
        print("NPM     :", self.npm)
        print("Jurusan :", self.major)
        print("Umur    :", self.age)
        print("Alamat  :", self.address)


# Input
print("===== Input Biodata Mahasiswa =====")
name = input("Masukkan Nama    : ")
npm = input("Masukkan NPM     : ")
major = input("Masukkan Jurusan : ")
age = int(input("Masukkan Umur    : "))
address = input("Masukkan Alamat  : ")


student1 = Student(name, npm, major, age, address)


student1.displayBiodata()