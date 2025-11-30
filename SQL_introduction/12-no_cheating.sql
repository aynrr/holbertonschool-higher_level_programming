-- a script that display records
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name !='' AND name != 'Bob' ORDER BY score DESC;
