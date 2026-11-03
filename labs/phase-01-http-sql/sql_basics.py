#!/usr/bin/env python3
"""Run safe SQL learning examples against an in-memory SQLite database."""

import sqlite3


def main() -> None:
    connection = sqlite3.connect(":memory:")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.executescript("""
        CREATE TABLE categories (
            category_id INTEGER PRIMARY KEY,
            category_name TEXT NOT NULL
        );
        CREATE TABLE products (
            product_id TEXT PRIMARY KEY,
            product_name TEXT NOT NULL,
            category_id INTEGER NOT NULL,
            price REAL NOT NULL CHECK (price > 0),
            FOREIGN KEY (category_id) REFERENCES categories(category_id)
        );
        CREATE TABLE offers (
            offer_id INTEGER PRIMARY KEY,
            product_id TEXT NOT NULL,
            store_id TEXT NOT NULL,
            observed_at TEXT NOT NULL,
            price REAL NOT NULL CHECK (price > 0),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        );

        INSERT INTO categories VALUES
            (1, 'Tablets'), (2, 'Accessories');
        INSERT INTO products VALUES
            ('P-100', 'Sample tablet', 1, 125.50),
            ('P-101', 'Protective case', 2, 18.00),
            ('P-102', 'Sample keyboard', 2, 35.00);
        INSERT INTO offers VALUES
            (1, 'P-100', 'S-01', '2026-10-01T10:00:00Z', 125.50),
            (2, 'P-100', 'S-02', '2026-10-01T10:05:00Z', 119.99),
            (3, 'P-101', 'S-01', '2026-10-01T10:10:00Z', 18.00),
            (4, 'P-102', 'S-02', '2026-10-01T10:15:00Z', 35.00);
    """)

    examples = [
        ("Products above 30", """
            SELECT product_id, product_name, price
            FROM products
            WHERE price > ?
            ORDER BY price DESC;
        """, (30,)),
        ("Products with category", """
            SELECT p.product_name, c.category_name
            FROM products AS p
            JOIN categories AS c ON c.category_id = p.category_id
            ORDER BY c.category_name, p.product_name;
        """, ()),
        ("Minimum offer by product and store", """
            SELECT product_id, store_id, MIN(price) AS min_price
            FROM offers
            GROUP BY product_id, store_id
            ORDER BY product_id, store_id;
        """, ()),
    ]

    for title, query, parameters in examples:
        print(f"\n## {title}")
        for row in cursor.execute(query, parameters):
            print(dict(row))

    # Always bind user-provided values as parameters.
    selected_product = "P-100"
    print("\n## Parameterized lookup")
    for row in cursor.execute(
        "SELECT product_id, product_name, price FROM products WHERE product_id = ?",
        (selected_product,),
    ):
        print(dict(row))

    connection.close()


if __name__ == "__main__":
    main()
