SELECT DISTINCT(H.CAR_ID)
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
INNER JOIN CAR_RENTAL_COMPANY_CAR AS C
ON H.CAR_ID = C.CAR_ID
WHERE C.CAR_TYPE = '세단' AND MID(H.START_DATE, 6, 2) = '10'
ORDER BY H.CAR_ID DESC
