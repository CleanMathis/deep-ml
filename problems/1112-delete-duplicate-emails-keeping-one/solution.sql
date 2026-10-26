
SELECT id, email
FROM (
  SELECT id, email,
         ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
  FROM person
) t
WHERE rn = 1
ORDER BY id;