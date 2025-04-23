from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date, col

spark = SparkSession.builder.appName("Date Filter").getOrCreate()

df = spark.read.csv("gs://your-bucket-name/input/events.csv", header=True, inferSchema=True)

df = df.withColumn("event_date", to_date(col("event_date"), "yyyy-MM-dd"))

# Filter for March 2024
march_df = df.filter((col("event_date") >= "2024-03-01") & (col("event_date") <= "2024-03-31"))

march_df.write.csv("gs://your-bucket-name/output/march_events", header=True)

spark.stop()
