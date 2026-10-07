------------------LAB1-----------------------
SELECT first_name, email FROM customers;

SELECT * FROM products WHERE category = 'Shoes';

SELECT * FROM customers WHERE city = 'Uppsala';

SELECT * FROM products WHERE price = 199.0;

SELECT * FROM products ORDER BY name;

SELECT * FROM customers ORDER BY joined_date;

SELECT * FROM products WHERE stock =0;

SELECT * FROM customers ORDER BY joined_date DESC LIMIT 3;

SELECT * FROM customers WHERE city in ('Stockholm','Göteborg');

SELECT name AS product,price AS price_sek FROM products;


-------------------- BONUS QUESTIONS--------------------------
SELECT * FROM products WHERE category in ('Clothing','Shoes') AND price > 1000;


SELECT name, price, stock, price * stock AS stock_value  FROM products WHERE stock > 0 ORDER BY stock_value DESC;

SELECT * FROM customers WHERE first_name LIKE '____';

SELECT * FROM products  ORDER BY price LIMIT 5 OFFSET 5;

SELECT * FROM customers WHERE joined_date < '2025-01-01' AND city != 'Uppsala' ORDER BY city, last_name;