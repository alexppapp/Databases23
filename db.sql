CREATE DATABASE SCHOOL;

use SCHOOL;

CREATE TABLE School_Unit (
Sname varchar(255),
Address varchar(255),
Town varchar(255),
Telephone int(10),
email varchar(255),
Principal varchar(255),
Handlerr varchar(255),
PRIMARY KEY (Sname)
);

ALTER TABLE School_Unit
ADD COLUMN MHuser varchar(255);

ALTER TABLE School_Unit
ADD CONSTRAINT FK_MH
FOREIGN KEY (MHuser) REFERENCES Main_Handler(Username);

show tables;
show columns from School_Unit;

CREATE TABLE Books (
ISBN int(10),
Title varchar(255),
Author varchar(255),
Publisher varchar(255),
Npages int(10),
Summary varchar(255),
Ncopies int(10),
Acopies int(10),
Image varchar(255),
Theme varchar(255),
Blanguage varchar(255),
word_keys varchar(255),
PRIMARY KEY (ISBN)
);

ALTER TABLE Books
ADD COLUMN Sunit varchar(255);

ALTER TABLE Books
ADD CONSTRAINT FK_Sunit
FOREIGN KEY (Sunit) REFERENCES School_Unit(Sname);

ALTER TABLE Books 
ADD COLUMN Huser varchar(255);

ALTER TABLE BOOKS 
ADD CONSTRAINT FK_Huser
FOREIGN KEY (Huser) REFERENCES Handlers(Username);

show columns from Books;

CREATE TABLE Main_Handler(
Username varchar(255),
Passwords int(10),
PRIMARY KEY (Username, Passwords)
);

ALTER TABLE Main_Handler 
ADD COLUMN Sname varchar(255);

show columns from Main_Handler;



CREATE TABLE Handlers(
Username varchar(255),
Passwords int(10),
PRIMARY KEY (Username, Passwords)
);

ALTER TABLE Handlers
ADD COLUMN Mhandler varchar(255);


ALTER TABLE Handlers
ADD CONSTRAINT FK_Mhandler
FOREIGN KEY (Mhandler) REFERENCES Main_Handler(Username);


CREATE TABLE Users(
Username varchar(255),
Passwords int(10),
Identity varchar(255),
PRIMARY KEY (Username, Passwords)
);

show tables;

CREATE TABLE Review(
Rtext varchar(255),
Climax int(10),
ISBN int(10),
Username varchar(255),
FOREIGN KEY (ISBN) references Books(ISBN),
FOREIGN KEY (Username) references Users(Username)
);

CREATE TABLE Rents(
Dates varchar(255),
Nrents int(255),
Aplies varchar(255),
Users varchar(255),
ISBN int(10),
FOREIGN KEY (Users) REFERENCES Users(Username),
FOREIGN KEY (ISBN) REFERENCES Books(ISBN)
);

CREATE TABLE Reservations(
Applications varchar(255),
Dates varchar(255),
Users varchar(255),
ISBN int(10),
foreign key (Users) references Users(Username),
foreign key (ISBN) references Books(ISBN)
);
