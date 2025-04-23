from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Join CSV").getOrCreate()

orders = spark.read.csv("gs://your-bucket-name/input/orders.csv", header=True, inferSchema=True)
customers = spark.read.csv("gs://your-bucket-name/input/customers.csv", header=True, inferSchema=True)

# Join on customer_id
joined_df = orders.join(customers, orders.customer_id == customers.id, "inner")

joined_df.write.csv("gs://your-bucket-name/output/joined_data", header=True)

spark.stop()
