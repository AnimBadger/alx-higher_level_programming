-- database that uses subqueries
SELECT id, name
FROM cities
WHERE state_id in (
    SELECT id FROM states
    WHERE name = 'Califonia'
)
order by id;
