import random
from datetime import datetime, timedelta

# Function to generate a random datetime within a specific range
def random_datetime():
    start_date = datetime(2023, 1, 1)  # Start date
    end_date = datetime(2023, 12, 31)  # End date
    days_diff = (end_date - start_date).days
    random_days = random.randint(0, days_diff)
    random_date = start_date + timedelta(days=random_days)
    return random_date.date()

start_date = datetime(2023, 1, 1)  # Start date for generating random datetime
end_date = datetime(2023, 12, 31)  # End date for generating random datetime

USERS=['User1', 'User2', 'User3', 'User4', 'User5', 'User6', 'User7', 'User8', 'User9', 'User10', 'User11', 'User12', 'User13', 'User14', 'User15', 'User16', 'User17', 'User18', 'User19', 'User20', 'User21', 'User22', 'User23', 'User24', 'User25', 'User26', 'User27', 'User28', 'User29', 'User30', 'User31', 'User32', 'User33', 'User34', 'User35', 'User36', 'User37', 'User38', 'User39', 'User40']
ISBNS=['978012345671', '978012345672', '978012345673', '978012345674', '978012345675', '978012345676', '978012345677', '978012345678', '978012345679', '9780123456710', '9780123456711', '9780123456712', '9780123456713', '9780123456714', '9780123456715', '9780123456716', '9780123456717', '9780123456718', '9780123456719', '9780123456720', '9780123456721', '9780123456722', '9780123456723', '9780123456724', '9780123456725', '9780123456726', '9780123456727', '9780123456728', '9780123456729', '9780123456730', '9780123456731', '9780123456732', '9780123456733', '9780123456734', '9780123456735', '9780123456736', '9780123456737', '9780123456738', '9780123456739', '9780123456740', '9780123456741', '9780123456742', '9780123456743', '9780123456744', '9780123456745', '9780123456746', '9780123456747', '9780123456748', '9780123456749', '9780123456750', '9780123456751', '9780123456752', '9780123456753', '9780123456754', '9780123456755', '9780123456756', '9780123456757', '9780123456758', '9780123456759', '9780123456760', '9780123456761', '9780123456762', '9780123456763', '9780123456764', '9780123456765', '9780123456766', '9780123456767', '9780123456768', '9780123456769', '9780123456770', '9780123456771', '9780123456772', '9780123456773', '9780123456774', '9780123456775', '9780123456776', '9780123456777', '9780123456778', '9780123456779', '9780123456780', '9780123456781', '9780123456782', '9780123456783', '9780123456784', '9780123456785', '9780123456786', '9780123456787', '9780123456788', '9780123456789', '9780123456790', '9780123456791', '9780123456792', '9780123456793', '9780123456794', '9780123456795', '9780123456796', '9780123456797', '9780123456798', '9780123456799', '97801234567100']
Schools=['ΓΕΛ ΝΑΞΟΥ', 'ΓΕΛ Μεσολλογίου', '1ο ΓΕΛ Ζωγράφου', '1ο ΓΕΛ Ζωγράφου', '1ο ΓΕΛ Ζωγράφου', '1ο ΓΕΛ Ζωγράφου', '1ο ΓΕΛ Ζωγράφου', 'ΓΕΛ ΝΑΞΟΥ', '1ο ΓΕΛ Ζωγράφου', 'ΓΕΛ ΝΑΞΟΥ', 'ΓΕΛ Μεσολλογίου', 'ΓΕΛ Μεσολλογίου', '1ο ΓΕΛ Ζωγράφου', 'ΓΕΛ Μεσολλογίου', 'ΓΕΛ ΝΑΞΟΥ', 'ΓΕΛ ΝΑΞΟΥ', 'ΓΕΛ ΝΑΞΟΥ', '1ο ΓΕΛ Ζωγράφου', 'ΓΕΛ ΝΑΞΟΥ', '1ο ΓΕΛ Ζωγράφου', '1ο ΓΕΛ Ζωγράφου', 'ΓΕΛ Μεσολλογίου', 'ΓΕΛ Μεσολλογίου', 'ΓΕΛ ΝΑΞΟΥ', '1ο ΓΕΛ Ζωγράφου', '1ο ΓΕΛ Ζωγράφου', 'ΓΕΛ Μεσολλογίου', '1ο ΓΕΛ Ζωγράφου', 'ΓΕΛ ΝΑΞΟΥ', 'ΓΕΛ Μεσολλογίου', 'ΓΕΛ Μεσολλογίου', 'ΓΕΛ ΝΑΞΟΥ', 'ΓΕΛ Μεσολλογίου', '1ο ΓΕΛ Ζωγράφου', '1ο ΓΕΛ Ζωγράφου', 'ΓΕΛ Μεσολλογίου', 'ΓΕΛ ΝΑΞΟΥ', 'ΓΕΛ ΝΑΞΟΥ', '1ο ΓΕΛ Ζωγράφου', 'ΓΕΛ ΝΑΞΟΥ']

Themes=['Romance', 'Poetry', 'Romance', 'Philosophy', 'Non-fiction', 'Science', 'Science fiction', 'Business', 'Poetry', 'Fiction', 'Philosophy', 'Biography', 'Fiction', 'Romance', 'Business', 'Philosophy', 'Thriller', 'Romance', 'Fantasy', 'Thriller', 'Fantasy', 'Science', 'Business', 'Historical fiction', 'Historical fiction', 'Fantasy', 'Biography', 'Science', 'Romance', 'Travel', 'Science', 'Mystery', 'Fantasy', 'Business', 'Romance', 'Historical fiction', 'Mystery', 'Science', 'Mystery', 'Biography', 'Thriller', 'Romance', 'Romance', 'Science', 'Fantasy', 'Thriller', 'Business', 'Biography', 'Biography', 'Science fiction', 'Fantasy', 'Mystery', 'Non-fiction', 'Fantasy', 'Personal Development', 'Fiction', 'Personal Development', 'Non-fiction', 'Mystery', 'Romance', 'Philosophy', 'Fantasy', 'Thriller', 'Science fiction', 'Romance', 'Biography', 'Non-fiction', 'Biography', 'Mystery', 'Travel', 'Biography', 'Personal Development', 'Romance', 'Romance', 'Romance', 'Science', 'Mystery', 'Science fiction', 'Personal Development', 'Romance', 'Personal Development', 'Romance', 'Science fiction', 'Mystery', 'Non-fiction', 'Thriller', 'Science fiction', 'Fiction', 'Non-fiction', 'Mystery', 'Fiction', 'Fantasy', 'Fiction', 'Philosophy', 'Travel', 'Romance', 'Business', 'Personal Development', 'Mystery', 'Business']

print("INSERT INTO Rents (StartD,due_d,Returnd, Users,School_Unit, ISBN,Theme) VALUES")
for i in range(1,51):
    StartD = random_datetime()  # Random datetime formatted as string
    due_d = StartD + timedelta(days=7, hours=0, minutes=0, seconds=0)
    Returnd=random_datetime()
    while Returnd<StartD:
    	Returnd=random_datetime()
    n_user=random.randint(0,39)
    Users = USERS[n_user]  # Random value between 1 and 100
    School_Unit=Schools[n_user]
    n_isbn=random.randint(0,99)
    ISBN = ISBNS[n_isbn]
    Theme=Themes[n_isbn]
    insert_statement = " ('{}','{}', '{}', '{}','{}', '{}','{}'),".format(
        StartD, due_d,Returnd, Users,School_Unit, ISBN,Theme
    )
    print(insert_statement)
print(";")
