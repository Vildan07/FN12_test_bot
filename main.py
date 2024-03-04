# class Employees:
#     def __init__(self, id, name, lastname, age, email):
#         self.id = id
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.email = email
#
# employees = [
#     (1, "Toxir", "Toxirov", 23, "yoxir@gmail.com"),
#     (2, "Jerry", "Jerry", 24, "jerry@gmail.com")
# ]
#
# for employee in employees:
#     em = Employees(*employee)
#     em.name = "Jalil"
#     print(em.id, em.name, em.lastname, em.age, em.email)
#
# # --------------------------------------------------------------------------
# # namedtuple
#
# from collections import namedtuple
#
# Employee = namedtuple("Employee", "id name lastname age email")
#
# employees = [
#     (1, "Toxir", "Toxirov", 23, "yoxir@gmail.com"),
#     (2, "Jerry", "Jerry", 24, "jerry@gmail.com")
# ]
#
# for employee in employees:
#     em = Employee(*employee)
#     print(em.id, em.name, em.lastname, em.age, em.email)


# --------------------------------------------------------------------------

# from collections import namedtuple
#
# Car = namedtuple("Car", "id model color speed price")
#
# cars = [
#     (1, "Audi", "red", 300, 10000),
#     (2, "Skoda", "blue", 210, 7000),
#     (3, "BMW", "green", 220, 3000)
# ]
# print("|", "id", "|", "model", "|", "color", "|", "speed", "|", "price")
# for car in cars:
#     car1 = Car(*car)
#     print(car1.id, car1.model, car1.color, car1.speed, car1.price)

# ----------------------------------------------------------------------------

























