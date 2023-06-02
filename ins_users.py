import random
print("INSERT INTO Users (Username,Passwords,name,surname,age,School_Unit,nrents,isteacher) VALUES")
USERS=[]
names=['Γιώργος', 'Γιάννης','Κώστας','Νίκος', 'Στάθης','Γεράσιμος','Μανώλης','Αλέξανδρος','Οδυσσέας']
surnames=['Γεωργίου','Παπαδόπουλος','Παπανικολάου','Σωτηρίου','Καραγιάννης','Ιωάννου','Παναγιωτόπουλος','Κατσαρός','Χρήστου']
Schools=['ΓΕΛ Μεσολλογίου','1ο ΓΕΛ Ζωγράφου' ,'ΓΕΛ ΝΑΞΟΥ']
return_array=[]
for i in range(1, 31):
    User = 'User' + str(i)
    USERS.append(User)
    passwords=random.randint(1000000000,9999999999)
    n_names=random.randint(0,len(names)-1)
    name=names[n_names]
    n_surname=random.randint(0,len(surnames)-1)
    surname=surnames[n_surname]
    age=random.randint(6,64)
    nrents=0
    isteacher=0
    n_school=random.randint(0,2)
    School=Schools[n_school]
    return_array.append(School)
    insert_statement = "('{}', {},'{}','{}', {} ,'{}', {}, '{}'),".format(
        User, passwords,name,surname,age,School,nrents,isteacher
    )
    
    print(insert_statement)
print()
print("INSERT INTO Users (Username,Passwords,isteacher) VALUES")
for i in range(31, 41):
    User = 'User' + str(i)
    USERS.append(User)
    passwords=random.randint(1000000000,9999999999)
    n_names=random.randint(0,len(names)-1)
    name=names[n_names]
    n_surname=random.randint(0,len(surnames)-1)
    surname=surnames[n_surname]
    age=random.randint(6,64)
    nrents=0
    isteacher=1
    n_school=random.randint(0,2)
    School=Schools[n_school]
    return_array.append(School)
    insert_statement = "('{}', {},'{}','{}', {} ,'{}', {}, '{}'),".format(
        User, passwords,name,surname,age,School,nrents,isteacher
    )
    print(insert_statement)
print(";")
print(return_array)#o pinakas pou paragete mpainei os eisodos ston pinaka Schools sto arxeio ins_rents
