SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE LEFT(AGE, 1) = '2' AND LEFT(JOINED, 4) = '2021'