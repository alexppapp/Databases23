from flask import Flask, render_template,request, flash, abort, redirect , url_for
import mysql.connector 

cnx = mysql.connector.connect(
    host ="localhost",
    user = 'root',
    password = 'newpassword',
    database = 'SCHOOL'
)
cursor = cnx.cursor()

def check_credentials(username,password):   #an den einai tipota poulo
     q = f"""
     select * from Main_Handler
     where Username = '{username}' and Passwords = {password};
     """
     
     cursor.execute(q)
     results = cursor.fetchall()

     if results: return '/mainhandler'
     else :
          q = f"""
            select * from Handlers
            where Username = '{username}' and Passwords = {password};
            """
          cursor.execute(q)
          results = cursor.fetchall()
     if results: return '/handlers'
     else:
        global x 
        x = username
        q = f"""
            select * from Users
            where Username = '{username}' and Passwords = {password};
            """
        cursor.execute(q)
        results = cursor.fetchall()
     if results: return '/users'
     else:
         return '/'
          


app =Flask(__name__)

@app.route('/')
def login_form():
    return render_template('login.html')


@app.route("/login",methods = ['POST','GET'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        result =check_credentials(username,password)
        return redirect(result)



@app.route("/mainhandler")
def main_handler():
    return render_template('mainhandler.html')

@app.route('/backup')
def b():
    return render_template('backup.html')

@app.route('/backup', methods=['POST'])
def backup_database():
    db_config = {
    'user': 'root',
    'password': 'newpassword',
    'host': 'localhost',
    'database': 'SCHOOL',
}


    # Backup file path
    backup_file = 'database_backup.sql'

    # Command to execute database backup
    command = f'mysqldump -u {db_config["user"]} -p{db_config["password"]} -h {db_config["host"]} {db_config["database"]} > {backup_file}'

    try:
        # Execute the backup command
        subprocess.run(command, shell=True, check=True)
        return 'Database backup created successfully!'
    except subprocess.CalledProcessError as e:
        return f'An error occurred while creating the database backup: {str(e)}'

@app.route('/delete_table', methods=['GET', 'POST'])
def delete_table():
    if request.method == 'POST':
        table_name = request.form['table_name']

        # Execute the delete statement
        query = f"DELETE FROM {table_name};"
        cursor.execute(query)
        cnx.commit()

        return 'Table data deleted successfully!'

    return render_template('delete.html')


@app.route('/registerm', methods=['POST', 'GET'])
def regm():
    if request.method == 'POST':
        # Insert user into the database
        username = request.form.get('username')
        password = request.form.get('password')
        name = request.form.get('name')
        surname = request.form.get('surname')
        sname = request.form.get('sname')
        Mhandler = request.form.get('Mhandler')

        # Execute the query
        query = """
        INSERT INTO Users (Username, Passwords, Firstname, Lastname, Sname, Mhandler)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (username, password, name, surname, sname, Mhandler)
        cursor.execute(query, values)

        # Commit and close the connection
        cnx.commit()
        return 'Query executed successfully!'
    return render_template('registerhandlers.html')

@app.route('/totalrents')
def get_rent_list():
    return render_template('totalrents.html')

@app.route('/totalrentsout',methods=['POST'])
def get_res(): # q1
    year = request.form.get('year')
    month = request.form.get('month')
    q = f"""
    select S_unit, count(*)
    from Rents
    where year(StartD)={year} and month(StartD) = {month}
    group by S_unit;
    """
    cursor.execute(q)
    results = cursor.fetchall()
    
    #print(type(results[0]))
    return render_template('totalrents.html', results = results )

@app.route('/authors')
def authors():
    return render_template('author.html')

@app.route('/authors', methods=['POST'])
def get_aut():
    theme = request.form.get('Theme')
    q = f"""
    select Author 
    from Books
    where Theme= '{theme}';
    """
    cursor.execute(q)
    results = cursor.fetchall()
    return render_template('author.html', results = results)


@app.route('/teachers', methods=['GET'])
def teach():
    q = """
    SELECT Users.name, Users.username, COUNT(*) AS total_borrowed
    FROM Users
    JOIN Rents ON Users.Username = Rents.Users
    WHERE Users.isteacher = 1 AND Users.Age < 40
    GROUP BY Users.name, Users.username
    ORDER BY total_borrowed DESC
    LIMIT 1;
    """
    cursor.execute(q)
    results = cursor.fetchall()
    return render_template('teachers.html', results=results)

@app.route('/notrented',methods=['GET'])
def rout():
    q = """
    select distinct Author
    from Books join Rents on Books.ISBN<>Rents.ISBN;
    """
    cursor.execute(q)
    results=cursor.fetchall()
    return render_template('authorsnotrented.html',results=results)



@app.route('/handlersrented',methods=['POST','GET'])
def hands():
    q="""
    select Huser, count(*)
    from Books join Rents on Books.ISBN= Rents.ISBN
    where Rents.StartD >= '2023-01-01 00:00:00' and Rents.StartD <='2023-12-31 00:00:00'
    group by Books.Huser
    having count(*) >20;
    """
    cursor.execute(q)
    results=cursor.fetchall()
    return render_template('handlersrented.html',results=results)

@app.route('/themebooks',methods=['GET'])
def theme_books():
    q="""
    SELECT Theme1, Theme2, COUNT(*) AS TotalBorrowings
    FROM (   
    SELECT         SUBSTRING_INDEX(Theme, ',', 1) AS Theme1,           SUBSTRING_INDEX(Theme, ',', -1) AS Theme2,
    ISBN     FROM Books ) AS Subquery
    INNER JOIN Rents ON Rents.ISBN = Subquery.ISBN GROUP BY Theme1, Theme2
    HAVING Theme1 <> Theme2
    ORDER BY TotalBorrowings DESC LIMIT 3;
    """
    cursor.execute(q)
    results=cursor.fetchall()
    return render_template('themebooks.html',results=results)

@app.route('/about',methods=['GET'])
def aut():
    q="""
    SELECT Author, COUNT(*) AS TotalBooks
    FROM Books
    GROUP BY Author
    HAVING TotalBooks <= (
    SELECT MAX(CountBooks) - 5
    FROM (
        SELECT COUNT(*) AS CountBooks
        FROM Books
        GROUP BY Author
    ) AS Counts
    );
    """
    cursor.execute(q)
    results=cursor.fetchall()
    return render_template('about_authors.html',results=results)

@app.route('/handlers')
def hand():
    return render_template('handler.html')

@app.route('/books', methods=['GET', 'POST'])
def search_books():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        theme = request.form['theme']

        # Query construction
        query = "SELECT Title, Author, Theme, Ncopies FROM Books WHERE 1=1"
        params = []

        if title:
            query += " AND Title LIKE %s"
            params.append(f'%{title}%')

        if author:
            query += " AND Author LIKE %s"
            params.append(f'%{author}%')

        if theme:
            query += " AND Theme LIKE %s"
            params.append(f'%{theme}%')

        query += " ORDER BY Title"

        # Execute the query
        cursor.execute(query, tuple(params))
        results = cursor.fetchall()

        return render_template('books.html', results=results)

    return render_template('books.html', results=None)


@app.route('/inbook', methods=['POST','GET'])
def insert_books():
    if request.method == 'POST':
    # Insert book into the database
        isbn = request.form.get('isbn')
        title = request.form.get('title')
        author = request.form.get('author')
        publisher = request.form.get('publisher')
        npages = request.form.get('npages')
        summary = request.form.get('summary')
        ncopies = request.form.get('ncopies')
        acopies = request.form.get('acopies')
        image = request.form.get('image')
        theme = request.form.get('theme')
        blanguage = request.form.get('blanguage')
        word_keys = request.form.get('word_keys')
        s_unit = request.form.get('s_unit')
        huser = request.form.get('huser')



        # Execute the query
        query = """
        INSERT INTO Books (ISBN, Title, Author, Publisher, Npages, Summary, Ncopies, Acopies, Image, Theme, Blanguage, Word_Keys, Sunit, Huser)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (isbn, title, author, publisher, npages, summary, ncopies, acopies, image, theme, blanguage, word_keys, s_unit, huser)
        cursor.execute(query, values)

        # Commit and close the connection
        cnx.commit()
        return 'Query executed successfully!'
    return render_template('inbooks.html')

@app.route('/insrent',methods = ['POST','GET'])
def ins_rents():
    if request.method == 'POST':
    # Insert book into the database
        StartD = request.form.get('StartD')
        ReturnD = request.form.get('ReturnD')
        due_d = request.form.get('due_d')
        Users = request.form.get('Users')
        ISBN = request.form.get('ISBN')
        S_unit = request.form.get('S_unit')

        # Execute the query
        query = """
        INSERT INTO Rents (StartD, Returnd, due_d, Users, ISBN, S_unit)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (StartD, ReturnD, due_d, Users, ISBN, S_unit)
        cursor.execute(query, values)

        # Commit and close the connection
        cnx.commit()
        return 'Query executed successfully!'
    return render_template('inrents.html')

@app.route('/reserv',methods = ['POST','GET'])
def ins_reserv():
    if request.method == 'POST':
    # Insert book into the database
        Reserv = request.form.get('Reserv')
        SDay = request.form.get('SDay')
        Usern = request.form.get('Usern')
        ISBN = request.form.get('ISBN')

        # Execute the query
        query = """
        INSERT INTO Reservations (Applications, SDay, Ddat, Usern, ISBN)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (Reserv, SDay,  Usern, ISBN)
        cursor.execute(query, values)

        # Commit and close the connection
        cnx.commit()
        return 'Query executed successfully!'
    return render_template('inreserv.html')

@app.route('/rerent',methods = ['POST','GET'])
def ins_retur():
    if request.method == 'POST':
    # Insert book into the database
        Return = request.form.get('Return')
        ISBN = request.form.get('ISBN')
        # Execute the query
        query = f"""
        INSERT INTO Rents (due_d)
        VALUES (%s)
        WHERE ISBN = '{ISBN}';
        """
        values = (Return)
        cursor.execute(query, values)

        # Commit and close the connection
        cnx.commit()
        return 'Query executed successfully!'
    return render_template('rerents.html')

@app.route('/register', methods=['POST', 'GET'])
def reg():
    if request.method == 'POST':
        # Insert user into the database
        username = request.form.get('username')
        password = request.form.get('password')
        isteacher = bool(request.form.get('isteacher'))
        name = request.form.get('name')
        surname = request.form.get('surname')
        age = request.form.get('age')
        nrents = request.form.get('nrents')

        # Execute the query
        query = """
        INSERT INTO Users (Username, Passwords, isteacher, name, surname, Age, nrents)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (username, password, isteacher, name, surname, age, nrents)
        cursor.execute(query, values)

        # Commit and close the connection
        cnx.commit()
        return 'Query executed successfully!'
    return render_template('registeruser.html')



@app.route('/update_book', methods=['GET', 'POST'])
def update_book():
    if request.method == 'POST':
        isbn = request.form.get('isbn')
        attributes = request.form.getlist('attribute')
        new_values = request.form.getlist('new_value')

        # Check if the lists of attributes and values have the same length
        if len(attributes) != len(new_values):
            return 'Invalid input'

        # Construct the SET clause for the UPDATE statement
        set_clause = ', '.join(f"{attribute} = %s" for attribute in attributes)

        # Execute the query
        query = f"""
        UPDATE Books
        SET {set_clause}
        WHERE ISBN = %s
        """
        values = new_values + [isbn]
        cursor.execute(query, values)

        # Commit and close the connection
        cnx.commit()
        return 'Book updated successfully!'

    return render_template('update_book.html')



@app.route('/rentsusers', methods=['POST','GET'])
def show_users():
    # Query to retrieve users with delay days
    query = """
    SELECT name, surname, DATEDIFF(CURDATE(), Returnd) AS DelayDays
    FROM Users 
    INNER JOIN Rents ON Users.Username = Rents.Users
    WHERE Returnd < CURDATE()
    """
    cursor.execute(query)
    results = cursor.fetchall()

    return render_template('users.html', results=results)

@app.route('/reviews', methods=['POST','GET'])
def avg() :
    username = request.form.get('username')
    theme = request.form.get('theme')
    q = f"""
    SELECT Users.Username, Books.Theme, AVG(Review.Climax) as Avgrating
    FROM Review
    JOIN Books ON Review.ISBN = Books.ISBN
    JOIN Users ON Review.Username = Users.Username
    WHERE Review.Username = '{username}' AND Books.Theme = '{theme}'
    GROUP BY Review.Username, Books.Theme;
    """
    cursor.execute(q)
    results = cursor.fetchall()
    return render_template('review.html', results = results)


@app.route('/users')
def u():
    return render_template('usermain.html')

@app.route('/booksu',methods=['POST','GET'])
def search_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        theme = request.form['theme']

        # Query construction
        query = "SELECT Title, Author, Theme, Ncopies FROM Books WHERE 1=1"
        params = []

        if title:
            query += " AND Title LIKE %s"
            params.append(f'%{title}%')

        if author:
            query += " AND Author LIKE %s"
            params.append(f'%{author}%')

        if theme:
            query += " AND Theme LIKE %s"
            params.append(f'%{theme}%')

        query += " ORDER BY Title"

        # Execute the query
        cursor.execute(query, tuple(params))
        results = cursor.fetchall()

        return render_template('booksu.html', results=results)

    return render_template('booksu.html', results=None)

@app.route('/rentsuser',methods=['POST','GET'])
def r():
    #print(x)
    #username='User1'
    # username = request.form.get('username')
    q = f"""
    select Books.Title, Books.Theme, Books.Author
    from Books
    join Rents on Books.ISBN=Rents.ISBN
    where Rents.Users = '{x}';
    """
    cursor.execute(q)
    results = cursor.fetchall()
    return render_template('rentsbyuser.html',results=results)
