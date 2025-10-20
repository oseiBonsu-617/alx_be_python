DROP DATABASE IF EXISTS alx_book_store;
CREATE DATABASE alx_book_store;
USE alx_book_store;


CREATE TABLE `author` (
	`author_id` INT PRIMARY KEY NOT NULL,
    `author_name` VARCHAR(215)
);


CREATE TABLE `books` (
	`book_id` INT PRIMARY KEY NOT NULL,
    `title` VARCHAR(130),
    `author_id` INT NOT NULL,
    `price` DOUBLE,
    `publication_date` DATE,
    KEY `fk_books_author_idx` (`author_id`),
    CONSTRAINT `fk_books_author` FOREIGN KEY (`author_id`) REFERENCES `author` (`author_id`) ON UPDATE CASCADE
);

CREATE TABLE `customers` (
	`customer_id` INT PRIMARY KEY NOT NULL,
    `customer_name` VARCHAR(215),
    `email` VARCHAR(215),
    `address` TEXT
);

CREATE TABLE `orders` (
	`order_id` INT PRIMARY KEY,
    `customer_id` INT NOT NULL,
    `order_date` DATE,
    KEY `fk_orders_customer_idx` (`customer_id`),
    CONSTRAINT `fk_orders_customer` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`) ON UPDATE CASCADE
);


CREATE TABLE `order_details` (
	`order_id` INT NOT NULL,
    `book_id` INT NOT NULL,
    `quantity` DOUBLE,
    KEY `fk_order_details_order_idx` (`order_id`),
    KEY `fk_order_details_book_idx` (`book_id`),
    CONSTRAINT `fk_order_details_order` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`) ON UPDATE CASCADE,
    CONSTRAINT `fk_order_details_book` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`) ON UPDATE CASCADE
);