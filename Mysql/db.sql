CREATE DATABASE SCHOOL;

use SCHOOL;

CREATE TABLE School_Unit (
Sname varchar(255) not null,
Address varchar(255) not null,
Town varchar(255) not null,
Telephone varchar(13) not null,
email varchar(255) not null,
Principal varchar(255) not null,
Handlerr varchar(255) not null,
PRIMARY KEY (Sname)
);


show tables;
show columns from School_Unit;

CREATE TABLE Books (
ISBN varchar(255) not null,
Title varchar(255) not null,
Author varchar(255) not null,
Publisher varchar(255) not null,
Npages int(10) not null,
Summary varchar(255) ,
Ncopies int(10) not null,
Acopies int(10) not null,
Image varchar(255),  
Theme varchar(255) not null,
Blanguage varchar(255),
word_keys varchar(255),
PRIMARY KEY (ISBN)
);


show columns from Books;

CREATE TABLE Main_Handler(
Username varchar(255),
Passwords int(10),
Firstn varchar(255),
Lastn varchar(255),
PRIMARY KEY (Username, Passwords)
);

show columns from Main_Handler;



CREATE TABLE Handlers(
Username varchar(255),
Passwords int(10),
Firstname varchar(255),
Lastname varchar(255),
PRIMARY KEY (Username, Passwords)
);



CREATE TABLE Users(
Username varchar(255),
Passwords int(10),
isteacher bool,
name varchar(255),
surname varchar(255),
PRIMARY KEY (Username, Passwords)
);


show tables;

CREATE TABLE Review(
Rtext varchar(255),
Climax int(10),
ISBN varchar(255),
Username varchar(255),
FOREIGN KEY (ISBN) references Books(ISBN),
FOREIGN KEY (Username) references Users(Username)
);
#isteacher
CREATE TABLE Rents(
StartD datetime,
Returnd datetime,
due_d datetime,
Users varchar(255),
ISBN varchar(255),
S_unit varchar(255),
FOREIGN KEY (Users) REFERENCES Users(Username),
FOREIGN KEY (ISBN) REFERENCES Books(ISBN),
foreign key(S_unit) references School_Unit(Sname)
);

CREATE TABLE Reservations(
Applications varchar(255),
SDay datetime,
Ddat datetime,
Usern varchar(255),
ISBN varchar(255),
foreign key (Usern) references Users(Username),
foreign key (ISBN) references Books(ISBN)
);


ALTER TABLE School_Unit 
ADD CONSTRAINT H_user
FOREIGN KEY (Handlerr) REFERENCES Handlers(Username);

ALTER TABLE School_Unit
ADD COLUMN MHuser varchar(255);

ALTER TABLE School_Unit
ADD CONSTRAINT FK_MH
FOREIGN KEY (MHuser) REFERENCES Main_Handler(Username);



ALTER TABLE Books
ADD COLUMN Sunit varchar(255);

ALTER TABLE Books
ADD CONSTRAINT FK_Sunit
FOREIGN KEY (Sunit) REFERENCES School_Unit(Sname);

ALTER TABLE Books 
ADD COLUMN Huser varchar(255);

ALTER TABLE Books 
ADD CONSTRAINT FK_Huser
FOREIGN KEY (Huser) REFERENCES Handlers(Username);


ALTER TABLE Handlers
ADD COLUMN Sname varchar(255);

ALTER TABLE Handlers
ADD CONSTRAINT Sname_users
FOREIGN KEY (Sname) REFERENCES School_Unit(Sname);


ALTER TABLE Handlers
ADD COLUMN Mhandler varchar(255);

ALTER TABLE Handlers
ADD CONSTRAINT FK_Mhandler
FOREIGN KEY (Mhandler) REFERENCES Main_Handler(Username);

alter table Users add index (isteacher);

alter table Users
add column S_unit varchar(255);

alter table Users
add constraint FK_S
foreign key (S_unit) references School_Unit(Sname);
