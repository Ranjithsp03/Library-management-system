create database lib;
use lib;
CREATE TABLE books (
    Book_id INT PRIMARY KEY,
    Book_name VARCHAR(255),
    Edition VARCHAR(50),
    Author_name VARCHAR(255),
    Volumes INT,
    Availability VARCHAR(50),
    Quantity INT
);
CREATE TABLE users (
    User_id INT PRIMARY KEY,
    User_name VARCHAR(255),
    Dept VARCHAR(100),
    Designation VARCHAR(100),
    Password VARCHAR(255)
);
CREATE TABLE borrows (
    Borrow_date DATE,
    Due_date DATE,
    Borrower_id INT,
    Book_id INT,
    Fine DECIMAL(8,2),
    FOREIGN KEY (Borrower_id) REFERENCES users(user_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);
INSERT INTO books (Book_ID, Book_Name, Edition, Author_Name, Volumes, Availability, Quantity)
VALUES
  (1, 'The Catcher in the Rye', '1st', 'J.D. Salinger', 1, 1, 5),
  (2, 'To Kill a Mockingbird', '50th Anniversary', 'Harper Lee', 1, 1, 3),
  (3, 'The Great Gatsby', '2nd', 'F. Scott Fitzgerald', 1, 0, 0),
  (4, '1984', 'Revised and Updated', 'George Orwell', 1, 1, 7),
  (5, 'Brave New World', '1st', 'Aldous Huxley', 1, 1, 4),
  (6, 'The Lord of the Rings', '3rd', 'J.R.R. Tolkien', 3, 1, 2),
  (7, 'Animal Farm', 'Revised Edition', 'George Orwell', 1, 1, 1),
  (8, 'The Hobbit', 'Revised Edition', 'J.R.R. Tolkien', 1, 1, 6),
  (9, 'Pride and Prejudice', '1st', 'Jane Austen', 1, 0, 0),
  (10, 'Jane Eyre', 'Revised Edition', 'Charlotte Bronte', 1, 1, 3);
select * from books;
INSERT INTO users (User_ID, User_Name, Dept, Designation, Password)
VALUES
  (1, 'Rajesh', 'Computer Science', 'Student', 'password1'),
  (2, 'Suresh', 'Mechanical Engineering', 'Staff', 'password2'),
  (3, 'Arjun', 'Electrical and Electronics Engineering', 'Student', 'password3'),
  (4, 'Deepika', 'Civil Engineering', 'Student', 'password4'),
  (5, 'Keerthi', 'Computer Science', 'Student', 'password5'),
  (6, 'Vishal', 'Mechanical Engineering', 'Student', 'password6'),
  (7, 'Divya', 'Electrical and Electronics Engineering', 'Professor', 'password7'),
  (8, 'Kishore', 'Civil Engineering', 'Student', 'password8'),
  (9, 'Dinesh', 'Computer Science', 'HOD', 'password9'),
  (10, 'Aishwarya', 'Mechanical Engineering', 'Student', 'password10');
  select * from users;
  INSERT INTO borrows (borrow_date, due_date, borrower_id, book_id, Fine)
VALUES
    ('2023-05-01', '2023-05-15', 1, 3, NULL),
    ('2023-04-28', '2023-05-12', 2, 5, 0.50),
    ('2023-05-02', '2023-05-16', 3, 2, NULL),
    ('2023-05-04', '2023-05-18', 4, 7, NULL),
    ('2023-05-06', '2023-05-20', 2, 1, NULL),
    ('2023-05-07', '2023-05-21', 1, 6, 1.25),
    ('2023-05-08', '2023-05-22', 5, 4, NULL),
    ('2023-05-09', '2023-05-23', 3, 8, NULL),
    ('2023-05-03', '2023-05-17', 6, 1, NULL),
    ('2023-05-05', '2023-05-19', 7, 9, NULL);
    select * from borrows;
Select Book_Name from books Where Availability = 1;
Select User_Name From users Where Designation = 'HOD';
Select User_Name From users Where Dept = 'Computer Science';
Select Due_Date from borrows where Borrower_ID = 1 and Book_ID =6;
Select SUM(Fine) 
FROM borrows
Where Borrower_ID = 1;
Update books
Set Availability = 0
Where Book_ID = 3;
Update books
Set Quantity = Quantity +3
Where Book_ID = 7;
Select User_Name
From users
Where Designation = 'Student' AND Dept = 'Computer Science';
Select Book_Name, Quantity
From books
Where Quantity = (Select MAX(Quantity) From books);
Select book_name, Edition, Quantity
From books
Natural join borrows
Where Availability = 1;
Select borrow_date, due_date, book_name From borrows Natural Join books;
Select book_name
From books
Where book_id IN (Select book_id From borrows) and Availability =1 ;
Select user_name
From users
Join borrows on users.user_id = borrows.borrower_id
Where borrows.due_date between '2023-05-01' and '2023-05-30';
Select book_name
From books
Join borrows on books.book_id = borrows.book_id
Join users on users.user_id = borrows.borrower_id
where Designation = 'Student';
Select user_name
From users
Join borrows on users.user_id = borrows.borrower_id
Group by users.user_name
Having COUNT(distinct borrows.book_id) = (Select COUNT(distinct book_id)
    from borrows
    group by borrower_id
    order by COUNT(distinct book_id) desc
    limit 1
);

