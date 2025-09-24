%sql
WITH distances AS (
    SELECT
        A.CITY AS city_a,
        B.CITY AS city_b,
        ROUND(ABS(A.LAT_N - B.LAT_N) + ABS(A.LONG_W - B.LONG_W), 4) AS distance
    FROM STATION A
    CROSS JOIN STATION B
)
SELECT city_a, city_b, distance
FROM distances
ORDER BY city_a, city_b;
