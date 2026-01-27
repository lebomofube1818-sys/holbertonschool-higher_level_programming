-- Lists all records of second_table with score >= 10
-- Displays score first, then name
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
