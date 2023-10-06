-- pass-test
.read data.sql


CREATE TABLE average_prices AS
  SELECT category, Avg(MSRP) as average_price from products group by category;


CREATE TABLE lowest_prices AS
  SELECT store, item, price from inventory group by item having price = Min(price);


CREATE TABLE best_deal AS
  SELECT name, MSRP / rating as cost from products group by category having cost = Min(cost);


CREATE TABLE shopping_list AS
  SELECT name, store from best_deal, lowest_prices where name = item;


CREATE TABLE total_bandwidth AS
  SELECT sum(Mbs) from shopping_list as a, stores as b where a.store = b.store;

