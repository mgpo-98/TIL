--
SELECT age, count(*)
FROM users 
GROUP BY age
ORDER BY age LIMIT 1;

SELECT min(age)
FROM users;

SELECT count(*)
FROM users WHERE age =15;

SELECT count(*) FROM users
WHERE age = (SELECT min(age) FROM users);

SELECT avg(balance) FROM users;
SELECT count(*) FROM users WHERE balance > (SELECT avg(balabce) from users);

SELECT country FROM users where last_name = '유' and first_name = '은정';

SELECT count(*) from users where country = (SELECT country FROM users
where last_name ='유' and first_name = '은정');

SELECT count(*), avg(balance), avg(age)
FROM users;

SELECT (SELECT count(*) FROM users) as 총인원,
(SELECT avg(balance) FROM users) as 평균연봉;

SELECT country
FROM users
where last_name = '이' and  first_name = '은정';

SELECT count(*) FROM users
where country =(SELECT country
FROM users
where last_name = '이' and  first_name = '은정'
);

SELECT country, count(*)
FROM users GROUP by country;

SELECT count(*)
FROM users 
where country in( SELECT country FROM users
WHERE last_name = '이'
and first_name = '은정');

SELECT last_name, min(age)
FROM users GROUP by last_name;

SELECT last_name, first_name, age FROM users
where (last_name, age ) in (
SELECT last_name, min(age) FROM users GROUP by last_name)
ORDER by last_name;
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
SELECT ArtistId 
FROM artists
WHERE Name = 'Nirvana';

SELECT * 
FROM albums
WHERE ArtistId = (SELECT ArtistId 
FROM artists
WHERE Name = 'Nirvana');