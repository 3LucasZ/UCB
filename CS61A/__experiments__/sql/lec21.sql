--Initialize db
CREATE TABLE pop_area_2010 AS
    SELECT "Berkeley" AS city, "Alameda" AS county, "CA" AS state, 112580 AS pop_2010, 10.43 AS land_area_sq_miles UNION
    SELECT "San Francisco", "San Francisco", "CA", 805235, 46.9 UNION
    SELECT "Oakland", "Alameda", "CA", 390724, 55.93 UNION
    SELECT "San Jose", "Santa Clara", "CA", 945942, 178.24 UNION
    SELECT "Fremont", "Alameda", "CA", 214089, 78.31 UNION
    SELECT "Santa Rosa", "Sonoma", "CA", 167815, 42.52 UNION
    SELECT "Hayward", "Alameda", "CA", 144186, 45.77 UNION
    SELECT "Sunnyvale", "Santa Clara", "CA", 140081, 22.06 UNION
    SELECT "Santa Clara", "Santa Clara", "CA", 116468, 18.28 UNION
    SELECT "Vallejo", "Solano", "CA", 115942, 30.50 UNION
    SELECT "Concord", "Contra Costa", "CA", 122067, 30.55 UNION
    SELECT "Fairfield", "Solano", "CA", 105321, 41.14 UNION
    SELECT "Richmond", "Contra Costa", "CA", 103701, 30.05 UNION
    SELECT "Antioch", "Contra Costa", "CA", 102372, 29.17 UNION
    SELECT "San Mateo", "San Mateo", "CA", 97207, 12.13 UNION
    SELECT "Daly City", "San Mateo", "CA", 101123, 7.64 UNION
    SELECT "Vacaville", "Solano", "CA", 92428, 29.19 UNION
    SELECT "Los Angeles", "Los Angeles", "CA", 3792621, 469.49 UNION
    SELECT "Palatine", "Cook", "IL", 68557, 14.11 UNION
    SELECT "Berkeley", "Cook", "IL", 5209, 1.40 UNION
    SELECT "Berkeley", "St Louis", "MO", 8978, 4.96 UNION 
    SELECT "Berkeley", "Ocean", "NJ", 41255, 42.72 UNION
    SELECT "Springfield", "Baca", "CO", 1451, 1.13 UNION
    SELECT "Springfield", "Bay", "FL", 8903, 4.18 UNION
    SELECT "Springfield", "Effingham", "GA", 2852, 3.25 UNION
    SELECT "Springfield", "Sangamon", "IL", 116250, 6.16;


CREATE TABLE cities AS
    SELECT "Berkeley" AS city, "Alameda" AS county, "CA" AS state, 124321 AS pop_2020 UNION
    SELECT "San Francisco", "San Francisco", "CA", 873959 UNION
    SELECT "Oakland", "Alameda", "CA", 440646 UNION
    SELECT "San Jose", "Santa Clara", "CA", 1013240 UNION
    SELECT "Fremont", "Alameda", "CA", 230504 UNION
    SELECT "Santa Rosa", "Sonoma", "CA", 178127 UNION
    SELECT "Hayward", "Alameda", "CA", 162954 UNION
    SELECT "Sunnyvale", "Santa Clara", "CA", 155805 UNION
    SELECT "Santa Clara", "Santa Clara", "CA", 127647 UNION
    SELECT "Vallejo", "Solano", "CA", 126090 UNION
    SELECT "Concord", "Contra Costa", "CA", 125410 UNION
    SELECT "Fairfield", "Solano", "CA", 119881 UNION
    SELECT "Richmond", "Contra Costa", "CA", 116448 UNION
    SELECT "Antioch", "Contra Costa", "CA", 115291 UNION
    SELECT "San Mateo", "San Mateo", "CA", 105661 UNION
    SELECT "Daly City", "San Mateo", "CA", 104901 UNION
    SELECT "Vacaville", "Solano", "CA", 102386 UNION
    SELECT "Los Angeles", "Los Angeles", "CA", 3898747 UNION
    SELECT "Palatine", "Cook", "IL", 67908 UNION
    SELECT "Berkeley", "Cook", "IL", 5338 UNION
    SELECT "Berkeley", "St Louis", "MO", 8228 UNION 
    SELECT "Berkeley", "Ocean", "NJ", 43754 UNION
    SELECT "Springfield", "Baca", "CO", 1325 UNION
    SELECT "Springfield", "Bay", "FL", 8075 UNION
    SELECT "Springfield", "Florida", "GA", 2703 UNION
    SELECT "Springfield", "Sangamon", "IL", 114394;

--Queries
SELECT * FROM cities LIMIT 3;

SELECT
a.city, a.pop_2020 - b.pop_2010 AS pop_difference
FROM 
cities as a, pop_area_2010 as b 
WHERE 
a.city = b.city AND a.county = b.county AND a.state = b.state
ORDER BY pop_difference DESC LIMIT 1;
