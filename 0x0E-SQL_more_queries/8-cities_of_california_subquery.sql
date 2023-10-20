-- lists all the cities of California that can be found in the database hbtn_0d_usa
-- sorted result results
SELECT id, name FROM cities
WHERE id = (
    SELECT id FROM states WHERE name = 'California'
    ) ORDER BY id ASC