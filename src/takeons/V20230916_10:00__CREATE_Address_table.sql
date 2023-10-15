-- Create the Address table
CREATE TABLE Address (
    id INT IDENTITY(1,1) PRIMARY KEY,
    street VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    zip VARCHAR(10)
);

-- Insert data into the Address table
INSERT INTO Address (street, city, state, zip)
VALUES ('123 Main St', 'Los Angeles', 'CA', '90001');

INSERT INTO Address (street, city, state, zip)
VALUES ('456 Elm St', 'New York', 'NY', '10001');

INSERT INTO Address (street, city, state, zip)
VALUES ('789 Oak St', 'Chicago', 'IL', '60601');

INSERT INTO Address (street, city, state, zip)
VALUES ('101 Pine St', 'Houston', 'TX', '77001');

INSERT INTO Address (street, city, state, zip)
VALUES ('202 Cedar St', 'Miami', 'FL', '33101');
