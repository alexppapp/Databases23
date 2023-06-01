import random
print("INSERT INTO Users (Username,Passwords,isteacher) VALUES")
USERS=[]
for i in range(1, 31):
    User = 'User' + str(i)
    USERS.append(User)
    passwords=random.randint(1000000000,9999999999)
    isteacher=0

    insert_statement = "('{}', {}, '{}'),".format(
        User, passwords, isteacher
    )
    print(insert_statement)
print(";")
print()
print("INSERT INTO Users (Username,Passwords,isteacher) VALUES")
for i in range(31, 41):
    User = 'User' + str(i)
    USERS.append(User)
    passwords=random.randint(1000000000,9999999999)
    isteacher=1

    insert_statement = "('{}', {}, '{}'),".format(
        User, passwords, isteacher
    )
    print(insert_statement)
print(";")
print(USERS)
