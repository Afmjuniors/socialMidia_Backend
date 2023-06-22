USE UserDB;

CREATE TABLE users (
    id serial primary key,
    type varchar(10) DEFAULT 'NORMAL',
    name varchar(100) not null,
    password varchar(255) not null
);

INSERT INTO users (type, name, password)
VALUES
    ('ADMIN', 'Alexandre', '1234'),
    ('NORMAL', 'Bernardo', '1234'),
    ('NORMAL', 'Camila', '1234');