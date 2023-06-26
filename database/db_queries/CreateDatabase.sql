USE UserDB;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  type VARCHAR(255),
  name VARCHAR(255),
  email VARCHAR(255),
  date_birth DATE,
  created_date DATE,
  password VARCHAR(255)
);


INSERT INTO users (type, name, email, date_birth, created_date, password)
VALUES
  ('ADMIN', 'John Doe', 'johndoe@example.com', '1990-01-01', '2023-06-01', 'password1'),
  ('NORMAL', 'Jane Smith', 'janesmith@example.com', '1995-02-15', '2023-06-02', 'password2'),
  ('NORMAL', 'Mike Johnson', 'mikejohnson@example.com', '1988-07-10', '2023-06-03', 'password3'),
  ('NORMAL', 'Sarah Brown', 'sarahbrown@example.com', '1992-04-20', '2023-06-04', 'password4'),
  ('NORMAL', 'Emily Davis', 'emilydavis@example.com', '1998-09-30', '2023-06-05', 'password5');
