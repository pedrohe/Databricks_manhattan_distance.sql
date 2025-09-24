SELECT 
  ROUND(
    ABS(MIN(LAT_N) - MAX(LAT_N))   -- |a - c|
  + ABS(MIN(LONG_W) - MAX(LONG_W)) -- |b - d|
  , 4) AS manhattan_distance
FROM Station;
