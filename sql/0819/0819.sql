-- SQLite
.table
.schema

SELECT * FROM albums 
ORDER BY Title DESC LIMIT 5;

SELECT count(*) as '고객 수' FROM customers;

SELECT FirstName as '이름', LastName AS '성'
FROM customers WHERE Country = 'USA'
ORDER BY FirstName DESC LIMIT 5;

SELECT * FROM invoices
WHERE `BillingState` = `NULL`
ORDER BY `InvoiceDate` DESC LIMIT 5;

SELECT count(*) FROM invoices
where InvoiceDate is '2013';

SELECT count(*) as '고객 수', Country as '나라' FROM customers
GROUP BY Country
ORDER by count(*) DESC LIMIT 5;

SELECT ArtistId, count(*) FROM albums
WHERE ArtistId = (SELECT count(*) FROM albums
ORDER BY albums ASC LIMIT 1 ;