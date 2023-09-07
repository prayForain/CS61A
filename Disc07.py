#Disc 7 Object_Oriented Programming 
#pass-test

#1.1

"""
>>> callahan = Professor("Callahan")
>>> elle = Student("Elle", callahan)
There are now 1 students

>>> elle.visit_office_hours(callahan)
Thanks, Callahan

>>> elle.visit_office_hours(Professor("Paulette"))
Thanks, Paulette

>>> elle.understanding
2

>>> [name for name in callahan.students]
['Elle']

>>> x = Student("Vivian", Professor("Stromwell")).name
There are now 2 students

>>> x
'Vivian'

>>> [name for name in callahan.students]
['Elle']
"""
class Student:
    students = 0
    def __init__(self, name, staff):
        self.name = name
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        staff.add_student(self)
    
    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)


class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1


#1.2

"""
>>> m = Minlist()
>>> m.append(4)
>>> m.append(2)
>>> m.size
2
>>> m = Minlist()
>>> m.append(4)
>>> m.append(1)
>>> m.append(5)
>>> m.pop()
1
>>> m.size
2
"""

class Minlist:
    def __init__(self):
        self.items = []
        self.size = 0

    def append(self, item):
        self.items.append(item)
        self.size += 1

    def pop(self):
        copy = self.items[:]
        smallest = min(copy)
        self.items.remove(smallest)
        self.size -=1
        return smallest
    

#1.3

"""
>>> server = Server()
>>> P = Client(server, 'Peng')
>>> Q = Client(server, 'Qi')
>>> server.register_client(P, 'Peng')
>>> server.register_client(Q, 'Qi')
>>> P.compose("Hello Qi !", 'Qi')
>>> Q.inbox
['Hello Qi !']
"""
class Email:
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Server:
    def __init__(self):
        self.clients = {}

    def send(self, email):
        self.clients[email.recipient_name].receive(email)

    def register_client(self, client, client_name):
        self.clients[client_name] = client


class Client:
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name

    def compose(self, msg, recipient_name):
        self.server.send(Email(msg, self.name, recipient_name))

    def receive(self, email):
        self.inbox.append(email.msg)


#2.1

"""
>>> thomas = Cat('Thomas', 'Tammy')
>>> thomas.talk()
Thomas syas meow!
>>> thomas.lose_life()
>>> for _ in range(8):
...     thomas.lose_life()
>>> thomas.lose_life()
The cat has no more lives to lose.

>>> magic = NoisyCat('Magic', 'James')
>>> magic.talk()
Magic syas meow!
Magic syas meow!

>>> muffin = NoisyCat('Muffin', 'Catherine')
>>> repr(muffin)
"NoisyCat('Muffin', 'Catherine')"
>>> muffin
NoisyCat('Muffin', 'Catherine')
"""
class Pet():
    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name 
        self.owner = owner
    
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)


class Dog(Pet):
    def talk(self):
        print(self.name + ' says woof!')


class Cat(Pet):
    def __init__(self, name, owner, lives = 9):
        super().__init__(name, owner)
        self.lives = lives

    def talk(self):
        print(str(self.name) + " syas meow!")

    def lose_life(self):
        if self.lives == 0:
            print("The cat has no more lives to lose.")
        else:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False


#2.2

class NoisyCat(Cat):
    def talk(self):
        super().talk()
        super().talk()

    def __repr__(self):
        return "NoisyCat('{}', '{}')".format(self.name, self.owner)