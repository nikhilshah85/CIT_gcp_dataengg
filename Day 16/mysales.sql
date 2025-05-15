CREATE TABLE Sales (
  salesId INT PRIMARY KEY AUTO_INCREMENT,
  product VARCHAR(255) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  category VARCHAR(255) NOT NULL,
  qtySold INT NOT NULL,
  amount DECIMAL(10, 2) NOT NULL
);

ALTER TABLE Sales AUTO_INCREMENT = 101;

INSERT INTO Sales (product, price, category, qtySold, amount)
VALUES
  ('Product A', 10.99, 'Electronics', 5, 54.95),
  ('Product B', 7.99, 'Toys', 3, 23.97),
  ('Product C', 12.99, 'Clothing', 2, 25.98),
  ('Product D', 9.99, 'Home Goods', 4, 39.96),
  ('Product E', 14.99, 'Sports', 1, 14.99),
  ('Product F', 8.99, 'Books', 6, 53.94),
  ('Product G', 11.99, 'Music', 3, 35.97),
  ('Product H', 6.99, 'Movies', 2, 13.98),
  ('Product I', 15.99, 'Games', 1, 15.99),
  ('Product J', 10.99, 'Electronics', 4, 43.96),
  ('Product K', 7.99, 'Toys', 5, 39.95),
  ('Product L', 12.99, 'Clothing', 3, 38.97),
  ('Product M', 9.99, 'Home Goods', 2, 19.98),
  ('Product N', 14.99, 'Sports', 1, 14.99),
  ('Product O', 8.99, 'Books', 4, 35.96),
  ('Product P', 11.99, 'Music', 2, 23.98),
  ('Product Q', 6.99, 'Movies', 3, 20.97),
  ('Product R', 15.99, 'Games', 1, 15.99),
  ('Product S', 10.99, 'Electronics', 5, 54.95),
  ('Product T', 7.99, 'Toys', 2, 15.98);

CREATE PROCEDURE sp_InsertSalesRecord
  @product VARCHAR(255),
  @price DECIMAL(10, 2),
  @category VARCHAR(255),
  @qtySold INT,
  @amount DECIMAL(10, 2)
AS
BEGIN
  INSERT INTO Sales (product, price, category, qtySold, amount)
  VALUES (@product, @price, @category, @qtySold, @amount)
END


CREATE PROCEDURE sp_UpdateElectronicsPrice
AS
BEGIN
  UPDATE Sales
  SET price = price * 1.10
  WHERE category = 'Electronics'
END











