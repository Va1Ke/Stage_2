CREATE TABLE clients(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    phone_number VARCHAR(30) NOT NULL
);

CREATE TABLE hotel(
    id INT PRIMARY KEY AUTO_INCREMENT,
    area INT NOT NULL,
    number_of_beds INT NOT NULL,
    price_for_a_night INT NOT NULL,
    busy BOOLEAN NOT NULL
);

CREATE TABLE orders(
    id INT PRIMARY KEY AUTO_INCREMENT,
    client_id INT NOT NULL,
    room_id INT NOT NULL,
    name VARCHAR(100),
    phone_number VARCHAR(30) NOT NULL,
    rented DATE NOT NULL,
    on_days INT,
    FOREIGN KEY (client_id) REFERENCES clients(id),
    FOREIGN KEY (room_id) REFERENCES hotel(id)
);

