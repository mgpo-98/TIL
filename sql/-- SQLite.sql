-- SQLite
SELECT COUNT(*) FROM healthcare;

SELECT max(age), min(age) FROM healthcare;

SELECT COUNT(*) FROM healthcare 
WHERE height >= 160 and height <= 170;

SELECT max(height), min(height) FROM healthcare;


SELECT * FROM healthcare WHERE is_drinking like 1 
ORDER by waist DESC LIMIT 5;


SELECT count(*) FROM healthcare WHERE va_left >= 1.5 AND
va_right >=1.5 AND is_drinking = 1;

SELECT count(*) FROM healthcare WHERE blood_pressure <120;

SELECT avg(waist) FROM healthcare WHERE blood_pressure > 140;


SELECT avg(height), avg(weight) FROM healthcare WHERE gender like 1 ;

SELECT id, height, weight FROM healthcare WHERE height = 195 AND
weight = 110 ;

SELECT COUNT(*) FROM healthcare WHERE (weight*10000)/(height*height) >= 30;

SELECT id, (weight*10000)/(height*height) FROM healthcare WHERE smoking = 3 
ORDER BY (weight*10000)/(height*height) DESC LIMIT 5 ;


SELECT weight, height FROM healthcare WHERE weight > 90 and height >190 ;

SELECT avg(weight), avg(age), avg(height) FROM healthcare;

SELECT count(*) FROM healthcare WHERE smoking = 1;