class Student:
    def __init__(self, name=None, score=None):
        self.name = name
        self.score = score

    # Getter Method Declaration
    def getName(self):
        return self.name

    def getScore(self):
        return self.score

    # Setter Method Declaration
    def setName(self, name):
        self.name = name

    def setScore(self, score):
        self.score = score


student1 = Student()

while True:
    print("\n===== OOP Program =====")
    print("1. Declare Object")
    print("2. Display Object")
    print("3. Change Object Value")
    print("4. Delete Object")
    print("5. Exit Program")
    choice = input("Enter Your Choice (1/2/3/4/5): ")

    if choice == "1":
        name = input("Enter Your Name: ")
        score = input("Enter Your Score: ")
        student1.setName(name)
        student1.setScore(score)
        print("Data Successfully Added")

    elif choice == "2":
        print("\nName:", student1.getName())
        print("Score:", student1.getScore())

    elif choice == "3":
        change = input("What would you like to change (Name/Score): ")
        if change == "Name":
            newName = input("Enter New Name: ")
            student1.setName(newName)
            print("Name Data Successfully Changed")
        elif change == "Score":
            newScore = input("Enter New Score: ")
            student1.setScore(newScore)
            print("Score Data Successfully Changed")

    elif choice == "4":
        student1.setName(None)
        student1.setScore(None)
        print("Data Successfully Deleted")

    elif choice == "5":
        print("Thank you for using my program.")
        break