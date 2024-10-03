CREATE DATABASE IF NOT EXISTS `stock-manager`;

CREATE TABLE IF NOT EXISTS product(
  id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  name VARCHAR(255) NOT NULL,
  reference VARCHAR(255) NOT NULL UNIQUE,
  quantity INT NOT NULL
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS stock (
    stock_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    category VARCHAR(255) NOT NULL,
    incoming_quantity INT NOT NULL,
    outgoing_quantity INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    alert BOOLEAN NOT NULL,
    product_id INT,
    CONSTRAINT fk_product
        FOREIGN KEY (product_id) REFERENCES product(id)
        ON DELETE CASCADE
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS user (
    user_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    reference_employee VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    role VARCHAR(50) NOT NULL
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS user_stock (
    user_id INT NOT NULL,
    stock_id INT NOT NULL,
    PRIMARY KEY(user_id, stock_id),
    CONSTRAINT fk_user
        FOREIGN KEY (user_id) REFERENCES user(user_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_stock
        FOREIGN KEY (stock_id) REFERENCES stock(stock_id)
        ON DELETE CASCADE
) ENGINE=INNODB;

INSERT INTO `product`(`id`, `name`, `reference`, `quantity`) VALUES ('[value-1]','[value-2]','[value-3]','[value-4]')