CREATE TABLE Theme(

theme_id INTEGER PRIMARY KEY,

theme_name VARCHAR(50),

description VARCHAR(200)

);

CREATE TABLE Stock(

stock_code VARCHAR(10),

stock_name VARCHAR(50),

theme_id INTEGER,

current_price INTEGER

);

CREATE TABLE Financials(

stock_code VARCHAR(10),

revenue BIGINT,

operating_profit BIGINT,

debt_ratio DOUBLE

);

CREATE TABLE Portfolio(

p_id INTEGER,

stock_code VARCHAR(10),

purchase_price INTEGER,

quantity INTEGER,

trade_date DATE

);