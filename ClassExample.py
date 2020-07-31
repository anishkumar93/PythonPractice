

class Dog:

    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{0} is {1} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{0} speaks {1}".format(self.name, sound)

def get_biggest_dog(*args):
    return max(args)


philo = Dog('philo', 5)
husky = Dog('husky', 6)
micky = Dog('micky', 7)


print("{0} is {1} and {2} is {3} and {4} is {5}".format(philo.name, philo.age,
                                                        husky.name, husky.age,
                                                        micky.name, micky.age))
print("{0} is a {1}!".format(philo.name, philo.species))

print("The oldest dog is {0} years old".format(get_biggest_dog(philo.age, husky.age, micky.age)))

print(philo.description())
print(philo.speak("Gruff Gruff"))

print(dir(Dog))
