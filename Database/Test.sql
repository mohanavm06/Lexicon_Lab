INSERT INTO customers (customer_id, first_name, last_name, city, email, joined_date)
	VALUES (11, 'Mohana', 'Muruganandha', 'Chennai', 'mohana.muruganandha@example.com', 2026-10-07);
	
INSERT INTO products (name, category, price, stock)
	VALUES  ('Laptop', 'Accessories', 2000, 3),
						('SSD', 'Accessories', 3000, 10);
		
INSERT INTO orders (order_id, customer_id, order_date)
	VALUES (16, 7, DATE('now'));

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
	VALUES (16, 10, 2, 179);
	
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
	VALUES (16, 10, 0, 179);
-- Result: CHECK constraint failed: quantity > 0

UPDATE orders SET status = 'shipped' WHERE order_id = 12;

UPDATE products SET stock = 50 WHERE product_id = 5;

UPDATE products SET price = ROUND(price * 1.1, 2) WHERE category = 'Accessories';

DELETE FROM order_items WHERE order_id = 12;
DELETE FROM orders WHERE order_id = 12;
-- items first since their FOREIGN KEY point to the order and stops deletion.