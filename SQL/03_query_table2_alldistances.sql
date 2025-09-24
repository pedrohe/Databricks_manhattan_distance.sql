from pyspark.sql import functions as F

# 1. Carrega a tabela Station
df = spark.table("Station")

# 2. Produto cartesiano (todas as combinações de cidades)
distances = df.alias("A").crossJoin(df.alias("B"))

# 3. Calcula a distância de Manhattan
distances = distances.select(
    F.col("A.CITY").alias("city_a"),
    F.col("B.CITY").alias("city_b"),
    F.round(
        F.abs(F.col("A.LAT_N") - F.col("B.LAT_N")) +
        F.abs(F.col("A.LONG_W") - F.col("B.LONG_W")),
        4
    ).alias("distance")
)

# 4. Pivot automático para gerar a matriz
matrix = distances.groupBy("city_a").pivot("city_b").max("distance").orderBy("city_a")

# 5. Mostrar a matriz completa
matrix.show(truncate=False)
