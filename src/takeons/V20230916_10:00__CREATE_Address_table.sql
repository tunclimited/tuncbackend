CREATE TABLE TestProject.Address (
    id INT AUTO_INCREMENT PRIMARY KEY,
    street VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    zip VARCHAR(10)
);


-- Insert 1
INSERT INTO TestProject.Address (street, city, state, zip)
VALUES ('123 Main St', 'Los Angeles', 'CA', '90001');

-- Insert 2
INSERT INTO TestProject.Address (street, city, state, zip)
VALUES ('456 Elm St', 'New York', 'NY', '10001');

-- Insert 3
INSERT INTO TestProject.Address (street, city, state, zip)
VALUES ('789 Oak St', 'Chicago', 'IL', '60601');

-- Insert 4
INSERT INTO TestProject.Address (street, city, state, zip)
VALUES ('101 Pine St', 'Houston', 'TX', '77001');

-- Insert 5
INSERT INTO TestProject.Address (street, city, state, zip)
VALUES ('202 Cedar St', 'Miami', 'FL', '33101');