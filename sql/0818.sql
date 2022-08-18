-- SQLite
SELECT smoking, COUNT(*) FROM healthcare GROUP BY smoking;

SELECT is_drinking, count(*) FROM healthcare GROUP by is_drinking;

SELECT is_drinking, count(blood_pressure) FROM healthcare GROUP by is_drinking
HAVING count(blood_pressure) >=200;

SELECT sido, count(sido) FROM healthcare
GROUP BY sido
HAVING count(sido)>=50000;

SELECT height, count(*) FROM healthcare 
GROUP BY height;

SELECT height, weight, count(*) FROM healthcare 
GROUP BY height, weight
ORDER by count(*) DESC LIMIT 5;

SELECT waist, count(*) FROM healthcare
GROUP by is_drinking;

SELECT gender,avg(va_left), avg(va_right) FROM healthcare
GROUP by gender;

SELECT age, avg(height), avg(weight) FROM healthcare
GROUP BY age
ALTER TABLE avg(height) RENAME COLUMN TO 평균 키 AND
ALTER TABLE avg(weight) RENAME COLUMN TO 평균 몸무게
HAVING 평균 키 >=160;

SELECT is_drinking, smoking, avg(weight/(height*0.01)*(height*0.01)) AS BMI FROM healthcare
GROUP by is_drinking, smoking 
HAVING smoking != '';

SELECT height, count(*) FROM healthcare 
GROUP BY height
ORDER BY COUNT(*) DESC  LIMIT 5;

SELECT gender,ROUND(avg(va_left),2), ROUND(avg(va_right),2) FROM healthcare
GROUP by gender;

SELECT age, avg(height) AS '평균 키' , avg(weight) '평균 몸무게' FROM healthcare
GROUP BY age
HAVING avg(height)>=160 AND avg(weight) >=60;

SELECT gender,ROUND(avg(va_left),2) AS '평균 왼쪽 시력', ROUND(avg(va_right),2) AS '평균 오른쪽 시력' FROM healthcare
GROUP by gender;