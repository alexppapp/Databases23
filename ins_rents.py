import random
from datetime import datetime, timedelta

# Function to generate a random datetime within a specific range
def random_datetime(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    random_seconds = random.randint(0, 59)
    random_microseconds = random.randint(0, 999999)
    random_timedelta = timedelta(days=random_days, hours=random_hours, minutes=random_minutes, seconds=random_seconds, microseconds=random_microseconds)
    return start_date + random_timedelta

start_date = datetime(2023, 1, 1)  # Start date for generating random datetime
end_date = datetime(2023, 12, 31)  # End date for generating random datetime

USERS=['User1', 'User2', 'User3', 'User4', 'User5', 'User6', 'User7', 'User8', 'User9', 'User10', 'User11', 'User12', 'User13', 'User14', 'User15', 'User16', 'User17', 'User18', 'User19', 'User20', 'User21', 'User22', 'User23', 'User24', 'User25', 'User26', 'User27', 'User28', 'User29', 'User30', 'User31', 'User32', 'User33', 'User34', 'User35', 'User36', 'User37', 'User38', 'User39', 'User40']
ISBNS=['8780123456751', '8780123456752', '8780123456753', '8780123456754', '8780123456755', '8780123456756', '8780123456757', '8780123456758', '8780123456759', '8780123456760', '8780123456761', '8780123456762', '8780123456763', '8780123456764', '8780123456765', '8780123456766', '8780123456767', '8780123456768', '8780123456769', '8780123456770', '8780123456771', '8780123456772', '8780123456773', '8780123456774', '8780123456775', '8780123456776', '8780123456777', '8780123456778', '8780123456779', '8780123456780', '8780123456781', '8780123456782', '8780123456783', '8780123456784', '8780123456785', '8780123456786', '8780123456787', '8780123456788', '8780123456789', '8780123456790', '8780123456791', '8780123456792', '8780123456793', '8780123456794', '8780123456795', '8780123456796', '8780123456797', '8780123456798', '8780123456799', '87801234567100']
print("INSERT INTO Rents (StartD, Returnd, Users, ISBN) VALUES")
for i in range(1,41):
    #Nrents  
    StartD = random_datetime(start_date, datetime(2023,5,31)).strftime('%Y-%m-%d %H:%M:%S')  # Random datetime formatted as string
    Returnd = random_datetime(datetime(2023,6,1), end_date).strftime('%Y-%m-%d %H:%M:%S')  # Random datetime formatted as string
    Users = USERS[i-1]  # Random value between 1 and 100
    ISBN = ISBNS[i-1]  # Random 13-digit ISBN

    insert_statement = " ('{}', '{}', '{}', '{}'),".format(
        StartD, Returnd, Users, ISBN
    )
    print(insert_statement)
for i in range(41,51):
    #Nrents  
    StartD = random_datetime(start_date, datetime(2023,5,31)).strftime('%Y-%m-%d %H:%M:%S')  # Random datetime formatted as string
    Returnd = random_datetime(datetime(2023,6,1), end_date).strftime('%Y-%m-%d %H:%M:%S')  # Random datetime formatted as string
    Users = USERS[i-35]  # Random value between 1 and 100
    ISBN = ISBNS[i-1]  # Random 13-digit ISBN

    insert_statement = " ('{}', '{}', '{}', '{}'),".format(
        StartD, Returnd, Users, ISBN
    )
    print(insert_statement)
print(";")
