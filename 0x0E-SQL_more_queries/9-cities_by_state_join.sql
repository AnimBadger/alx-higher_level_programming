-- database using inner join
SELECT c.id, c.name, s.name
    FROM cities AS c
    INNER JOIN states AS s
    ON c.id = s.id
ORDER BY c.id;