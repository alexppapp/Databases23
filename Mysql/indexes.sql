use SCHOOL;

create index idx_name1
on Main_Handler(Username);

create index idx_name2
on Users(Username);

create index idx_age
on Users(Age);

create index idx_name3
on Handlers(Username);

create index idx_isbn
on Books(ISBN);

create index idx_theme
on Books(Theme);

create index idx_author
on Books(Author);


