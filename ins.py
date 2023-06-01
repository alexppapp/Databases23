import random
print("INSERT INTO Books (ISBN, Title, Author, Publisher, Npages, Summary, Ncopies, Acopies, Image, Theme, Blanguage, word_keys, Sunit, Huser) VALUES")
ISBNS=[]
for i in range(51, 101):
    ISBN = '97801234567' + str(i)
    ISBNS.append(ISBN)
    Title = 'Book ' + str(i)
    Author = 'Author ' + str(i)
    Publisher = 'Publisher ' + str(i)
    Npages = random.randint(100, 599)
    Summary = 'Summary ' + str(i)
    Ncopies = random.randint(1, 20)
    Acopies = random.randint(1, Ncopies)
    Image = 'https://example.com/book_image_' + str(i) + '.jpg'
    Theme = 'Theme ' + str(i)
    Blanguage = 'Language ' + str(i)
    word_keys = 'key' + str(i) + '_1, key' + str(i) + '_2, key' + str(i) + '_3'
    Sunit = 'New School' 
    Huser = 'Papadopoulos'

    insert_statement = "('{}', '{}', '{}', '{}', {}, '{}', {}, {}, '{}', '{}', '{}', '{}', '{}', '{}'),".format(
        ISBN, Title, Author, Publisher, Npages, Summary, Ncopies, Acopies, Image, Theme, Blanguage, word_keys, Sunit, Huser
    )

    print(insert_statement)
print(";")
print(ISBNS)
