CREATE DATABASE Bankmanagement;
USE Bankmanagement;
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL, 
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(10),
    city VARCHAR(100),
    state VARCHAR(100)
    
);
INSERT INTO Customers (username, password_hash, first_name, last_name, email, phone_number, city, state)
VALUES 
('arindam_biswas', '1248vghfy566', 'Arindam', 'Biswas', 'arindambiswas260@gmail.com', '9734756233', 'Krishnagar', 'West Bengal'),
('alik_saha', 'dd@GFff12152g12', 'Alik', 'Saha', 'aliksaha457@gmail.com', '8759147630', 'Dum Dum', 'West Bengal'),
('srimanta_bose', 'sd@Fff1fy58712', 'Srimanta', 'Bose', 'srimantabosejr78@gmail.com', '8240151878', 'Barasat', 'West Bengal'),
('anurag_sarkar', 'dd@G7f1dfd2g12', 'Anurag', 'Sarkar', 'sarkaranurag47@gmail.com', '7063136161', 'Phulia', 'West Bengal'),
('trithi_sen', 'arer75@fdff12', 'Trithi', 'Sen', 'trithisar474@gmail.com', '9065147630', 'Indore', 'Madhyapradesh'),
('souvik_mondal', '*Pf9DG&2yu', 'Souvik', 'Mondal', 'souvikmondalsm006@gmail.com', '7501232915', 'Bhagalpur', 'Bihar'),
('arpita_biswas', 'E5U%gCE9dV', 'Arpita', 'Biswas', 'arpitabi455@gmail.com', '781467630', 'Kolkata', 'West Bengal'),
('baishakhi_mondal', '#92^LNf*g6', 'Baishakhi', 'Mondal', 'baishakhimondal75@gmail.com', '8759148702', 'Siliguri', 'West Bengal'),
('priyanka_chowdhury', '$qTQ6$^qLR', 'Priyanka', 'Chowdhury', 'priyankachow046@gmail.com', '9933347630', 'Salt Lake', 'West Bengal'),
('tamashi_majumder', 'Up%g8B%MSv', 'Tamashi', 'Majumder', 'tamamaj694@gmail.com', '9759873630', 'Prayagraj', 'Uttar Pradesh');
CREATE TABLE Accounts (
    account_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    branch VARCHAR(50),
	account_type ENUM('Savings', 'Current') NOT NULL,
    balance DECIMAL(50, 2) NOT NULL DEFAULT 0,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

INSERT INTO Accounts (customer_id, branch, account_type, balance)
VALUES 
(1, 'KNG-1', 'Savings', 457800),
(2, 'DD-2', 'Current', 4708708.87),
(3, 'BT-1', 'Savings', 82416.50),
(4, 'PA-1', 'Savings', 870444.65),
(5, 'INR-3','Savings', 6879.14),
(6, 'BGL-2','Current', 14541247),
(7, 'KOL-8', 'Current', 788755554.45),
(8, 'SG-4','Savings', 478787.87),
(9, 'SL-3', 'Savings', 77858772.45), 
(10, 'PRG-5', 'Savings', 8445457);


CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    account_id INT,
    transaction_type ENUM('credit', 'debit') NOT NULL,
    amount DECIMAL(50, 2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);
INSERT INTO Transactions (account_id, transaction_type, amount)
VALUES
(1, 'credit', 47110),
(1, 'debit', 7441.84),
(4, 'credit', 6510),
(2, 'credit', 744787),
(5, 'credit', 736910),
(8, 'debit', 7497),
(3, 'credit', 98524),
(7, 'debit', 87745),
(9, 'credit', 9610),
(10, 'credit', 6887);

-- Trigger to change the total amount after trasaction record add
DELIMITER //

CREATE TRIGGER update_balance
AFTER INSERT ON Transactions
FOR EACH ROW
BEGIN
    DECLARE new_balance DECIMAL(10, 2);

    IF NEW.transaction_type = 'credit' THEN
        SET new_balance = (SELECT balance + NEW.amount FROM Accounts WHERE account_id = NEW.account_id);
    ELSE
        SET new_balance = (SELECT balance - NEW.amount FROM Accounts WHERE account_id = NEW.account_id);
    END IF;

    UPDATE Accounts SET balance = new_balance WHERE account_id = NEW.account_id;
END;

//

DELIMITER ;
