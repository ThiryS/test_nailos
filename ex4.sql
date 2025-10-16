CREATE TABLE Product (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    creation_date DATE NOT NULL
);
CREATE TABLE Category (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    is_private BOOLEAN NOT NULL
);
CREATE TABLE ProductCategory (
    product_id INT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (product_id, category_id),
    FOREIGN KEY (product_id) REFERENCES Product(id),
    FOREIGN KEY (category_id) REFERENCES Category(id)
);
-- the query:
--
-- SELECT p.id, p.name
-- FROM Product p
-- JOIN ProductCategory pc ON p.id = pc.product_id
-- JOIN Category c ON pc.category_id = c.id
-- WHERE c.is_private = FALSE
-- GROUP BY p.id, p.name
-- HAVING COUNT(c.id) > 5;