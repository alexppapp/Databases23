import random
print("INSERT INTO Books (ISBN, Title, Author, Publisher, Npages, Summary, Ncopies, Acopies, Image, Theme, Blanguage, word_keys, Sunit, Huser) VALUES")
ISBNS=[]
Themes=['Fiction','Non-fiction','Science fiction','Fantasy','Mystery','Thriller','Romance','Historical fiction','Biography','Personal Development','Science','Philosophy','Business','Travel','Poetry']
Authors=['Steven Hawking','Carl Sagan','Friedrich Nietzsche','Robert Frost','J.R.R. Tolkien','Bill Bryson']
return_values=[]
for i in range(1, 41):
    ISBN = '97801234567' + str(i)
    ISBNS.append(ISBN)
    Title = 'Book ' + str(i)
    n_authors=random.randint(0,len(Authors)-1)
    Author = Authors[n_authors]
    Publisher = 'Publisher ' + str(i)
    Npages = random.randint(100, 599)
    Summary = 'Summary ' + str(i)
    Ncopies = random.randint(1, 20)
    Acopies = Ncopies
    Image = 'https://example.com/book_image_' + str(i) + '.jpg'
    n_theme = random.randint(0,len(Themes)-1)
    Theme=Themes[n_theme]
    Blanguage = 'Language ' + str(i)
    word_keys = 'key' + str(i) + '_1, key' + str(i) + '_2, key' + str(i) + '_3'
    Sunit = 'ΓΕΛ ΝΑΞΟΥ' 
    Huser = 'Βιτζηλαίος'
    return_values.append(Theme)
    insert_statement = "('{}', '{}', '{}', '{}', {}, '{}', {}, {}, '{}', '{}', '{}', '{}', '{}', '{}'),".format(
        ISBN, Title, Author, Publisher, Npages, Summary, Ncopies, Acopies, Image, Theme, Blanguage, word_keys, Sunit, Huser
    )

    print(insert_statement)
    
for i in range(41, 71):
    ISBN = '97801234567' + str(i)
    ISBNS.append(ISBN)
    Title = 'Book ' + str(i)
    n_authors=random.randint(0,len(Authors)-1)
    Author = Authors[n_authors]
    Publisher = 'Publisher ' + str(i)
    Npages = random.randint(100, 599)
    Summary = 'Summary ' + str(i)
    Ncopies = random.randint(1, 20)
    Acopies = Ncopies
    Image = 'https://example.com/book_image_' + str(i) + '.jpg'
    n_theme = random.randint(0,len(Themes)-1)
    Theme=Themes[n_theme]
    Blanguage = 'Language ' + str(i)
    word_keys = 'key' + str(i) + '_1, key' + str(i) + '_2, key' + str(i) + '_3'
    Sunit = 'ΓΕΛ Μεσολλογίου' 
    Huser = 'Παπαδάκος'
    return_values.append(Theme)
    insert_statement = "('{}', '{}', '{}', '{}', {}, '{}', {}, {}, '{}', '{}', '{}', '{}', '{}', '{}'),".format(
        ISBN, Title, Author, Publisher, Npages, Summary, Ncopies, Acopies, Image, Theme, Blanguage, word_keys, Sunit, Huser
    )

    print(insert_statement)
    
for i in range(71, 101):
    ISBN = '97801234567' + str(i)
    ISBNS.append(ISBN)
    Title = 'Book ' + str(i)
    n_authors=random.randint(0,len(Authors)-1)
    Author = Authors[n_authors]
    Publisher = 'Publisher ' + str(i)
    Npages = random.randint(100, 599)
    Summary = 'Summary ' + str(i)
    Ncopies = random.randint(1, 20)
    Acopies = Ncopies
    Image = 'https://example.com/book_image_' + str(i) + '.jpg'
    n_theme = random.randint(0,len(Themes)-1)
    Theme=Themes[n_theme]
    Blanguage = 'Language ' + str(i)
    word_keys = 'key' + str(i) + '_1, key' + str(i) + '_2, key' + str(i) + '_3'
    Sunit = '1ο ΓΕΛ Ζωγράφου' 
    Huser = 'Μούσχουρου'
    return_values.append(Theme)
    insert_statement = "('{}', '{}', '{}', '{}', {}, '{}', {}, {}, '{}', '{}', '{}', '{}', '{}', '{}'),".format(
        ISBN, Title, Author, Publisher, Npages, Summary, Ncopies, Acopies, Image, Theme, Blanguage, word_keys, Sunit, Huser
    )

    print(insert_statement)
print(";")
print(ISBNS)
print()
print(return_values)# o pinakas pou paragete mpainei sthn lista theme sto arxeio ins_rents
