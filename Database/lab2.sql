-- LOGISTICS MANAGEMENT SYSTEM

-- 1. Create a table packages
CREATE TABLE packages (
    package_id INTEGER PRIMARY KEY,
    package_name TEXT NOT NULL,
    description TEXT,
    weight INTEGER
);cd ..
git fetch origin
git rebase origin/main

-- 2. Add a rule so weight must be greater than 0
DROP TABLE packages;

CREATE TABLE packages (
    package_id INTEGER PRIMARY KEY,
    package_name TEXT NOT NULL,
    description TEXT,
    weight INTEGER CHECK (weight > 0)
);

-- 3. Add a tracking_number column
ALTER TABLE packages
ADD COLUMN tracking_number TEXT;

-- 4. Delete the packages table
DROP TABLE packages;

-- 5. Create a table shipment_reviews
CREATE TABLE shipment_reviews (
    review_id INTEGER PRIMARY KEY,
    shipment_id INTEGER,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    FOREIGN KEY (shipment_id)
        REFERENCES shipments(shipment_id)
);

-- 6. Test shipment_reviews
INSERT INTO shipment_reviews
(shipment_id, rating, comment)
VALUES (2, 6, 'Good');

-- Expected:
-- CHECK constraint failed

-- 7. Test shipment_reviews
INSERT INTO shipment_reviews
(shipment_id, rating, comment)
VALUES (50, 3, 'Average');

-- Expected:
-- FOREIGN KEY constraint failed

-- 8. Create shipments table
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    shipment_date TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending'
    CHECK (
        status IN (
            'pending',
            'in_transit',
            'delivered',
            'cancelled'
        )
    ),
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

-- 9. Create shipment_items table
CREATE TABLE shipment_items (
    shipment_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL
        CHECK (quantity > 0),
    unit_price REAL NOT NULL,

    PRIMARY KEY (shipment_id, product_id),

    FOREIGN KEY (shipment_id)
        REFERENCES shipments(shipment_id),

    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);
