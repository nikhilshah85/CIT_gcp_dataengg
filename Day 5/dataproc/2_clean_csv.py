from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType

spark = SparkSession.builder.appName("Clean CSV").getOrCreate()

df = spark.read.csv("gs://your-bucket-name/input/raw_data.csv", header=True, inferSchema=True)

# Drop rows with nulls
df_clean = df.dropna()

# Cast column types
df_clean = df_clean.withColumn("age", df_clean["age"].cast(IntegerType()))

df_clean.write.csv("gs://your-bucket-name/output/cleaned_data", header=True)

spark.stop()
