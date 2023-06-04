USE SCHOOL;

SHOW TABLES;
ALTER TABLE Handlers add constraint unique (Username);

ALTER TABLE Main_Handler add constraint unique (Username, Passwords);

ALTER TABLE Users add constraint unique (Username, Passwords);

#ALTER TABLE Books add constraint check (ISBN = 13);

ALTER TABLE Rents add constraint check(StartD < due_d);

ALTER TABLE School_Unit add constraint unique (Sname);

ALTER TABLE Review add constraint check (Climax < 10);

alter table Users add constraint check (
(isteacher = true AND Nrents <=1) or
(isteacher = false and Nrents <=2)
);

