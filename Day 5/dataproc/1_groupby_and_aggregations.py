from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Sales Aggregation").getOrCreate()

df = spark.read.csv("gs://your-bucket-name/input/sales.csv", header=True, inferSchema=True)

# Group by region and sum sales
agg_df = df.groupBy("region").sum("sales")

# Rename the column
agg_df = agg_df.withColumnRenamed("sum(sales)", "total_sales")

agg_df.write.csv("gs://your-bucket-name/output/region_sales", header=True)

spark.stop()
