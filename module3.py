def greet(name):
    print(f"Hello, {name}!")
    print(f"Nice to meet you, {name}.")
    print(f"I hope you have a wonderful day, {name}!")
def fullname(firstname, lastname):
    fullname = f"{firstname} {lastname}"
    print(f"Hello, {fullname}.")
people = ["Toan Nguyen", "Mai Duong", "Tran Nguyen"]
for person in people:
    greet(person)
    print()  
fullname("Toan", "Nguyen")
fullname("Mai", "Duong")
fullname("Tran", "Nguyen")