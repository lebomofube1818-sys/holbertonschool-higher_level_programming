-- 0. List all databases of your MySQL server
-- This script lists all databases currently present, sorted alphabetically
SELECT SCHEMA_NAME AS `Database`
FROM INFORMATION_SCHEMA.SCHEMATA
ORDER BY SCHEMA_NAME ASC;

