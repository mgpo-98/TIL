-- SQLite
SELECT * FROM users INNER join role
    ON users.role_id = role.id;

SELECT users.name, role.title
FROM users INNER join role on users.role_id = role.id;

SELECT * from users INNER JOIN role
 on users.role_id = role.id
 ORDER by name DESC;

SELECT *
FROM users INNER JOIN role
    ON users.role_id = role.id
WHERE role.id = 2;

SELECT *
FROM articles LEFT OUTER JOIN users
    ON articles.user_id = user_id;

    SELECT * FROM  articles LEFT OUTER JOIN users
    on articles.user_id = user_id 
    where articles.user_id is NOT NULL;
SELECT * FROM articles FULL OUTER JOIN users
on articles.user_id = user_id ;

SELECT * FROM users cross JOIN role;

SELECT * 
FROM articles
    JOIN users
        ON articles.user_id = users.id
    JOIN role
        ON users.role_id = role.id;