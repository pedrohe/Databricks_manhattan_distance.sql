# Databricks / PySpark
from pyspark.sql import Row
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

# ---- 1) Schema (mirrors the prompt) ----
schema = StructType([
    StructField("ID", IntegerType(), False),
    StructField("CITY", StringType(), True),     # VARCHAR2(21)
    StructField("STATE", StringType(), True),    # VARCHAR2(2)
    StructField("LAT_N", DoubleType(), True),    # NUMBER -> use Double
    StructField("LONG_W", DoubleType(), True)    # NUMBER -> use Double (west longitudes are negative)
])

# ---- 2) Mock data (diverse lat/long for clear min/max) ----
# Tip: include duplicates/nearby values to test edge cases & ties if you want.
data = [
    Row(1,  "Anchorage",     "AK", 61.2181,  -149.9003),
    Row(2,  "Seattle",       "WA", 47.6062,  -122.3321),
    Row(3,  "San Francisco", "CA", 37.7749,  -122.4194),
    Row(4,  "Los Angeles",   "CA", 34.0522,  -118.2437),
    Row(5,  "Denver",        "CO", 39.7392,  -104.9903),
    Row(6,  "Chicago",       "IL", 41.8781,   -87.6298),
    Row(7,  "Miami",         "FL", 25.7617,   -80.1918),
    Row(8,  "New York",      "NY", 40.7128,   -74.0060),
    Row(9,  "Boston",        "MA", 42.3601,   -71.0589),
    Row(10, "San Juan",      "PR", 18.4655,   -66.1057),
    Row(11, "Honolulu",      "HI", 21.3069,  -157.8583),
    Row(12, "Fairbanks",     "AK", 64.8378,  -147.7164),
]

df = spark.createDataFrame(data, schema)
df.write.mode("overwrite").saveAsTable("Station")
df.show()
