class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Age must be positive!")

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.__age} years old.")

# Create an instance of Student



student1 = Student("Alice", 20)

# Set a new age



student1.set_age(21)

# Print introduction



student1.introduce()