# Databricks notebook source
from pyspark.sql.functions import col
from pyspark.sql.types import *

# COMMAND ----------

import json

# Read the configuration from JSON file
with open('config.json') as f:
    configs = json.load(f)


dbutils.fs.mount(
source = "abfss://tokyo-olympic-data@olympictokyodata.dfs.core.windows.net", # container@storageacc
mount_point = "/mnt/tokyoolympic",
extra_configs = configs)

# COMMAND ----------

#  %fs
#  ls "/mnt/tokyoolympic"

# COMMAND ----------

spark

# COMMAND ----------

athletes = spark.read.format("csv").option("header","true").option("inferschema","true").load("/mnt/tokyoolymic/raw-data/athletes.csv")
coaches = spark.read.format("csv").option("header","true").option("inferschema","true").load("/mnt/tokyoolymic/raw-data/coaches.csv")
entriesgender = spark.read.format("csv").option("header","true").load("/mnt/tokyoolymic/raw-data/entriesgender.csv")
medals = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolymic/raw-data/medals.csv")
teams = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolymic/raw-data/teams.csv")

# COMMAND ----------

athletes.show()

# COMMAND ----------

athletes.printSchema()

# COMMAND ----------

coaches.show()

# COMMAND ----------

coaches.printSchema()

# COMMAND ----------

entriesgender.show()

# COMMAND ----------

entriesgender.printSchema()

# COMMAND ----------

entriesgender = entriesgender.withColumn("Female",col("Female").cast(IntegerType()))\
    .withColumn("Male",col("male").cast(IntegerType()))\
        .withColumn("Total",col("Total").cast(IntegerType()))

# COMMAND ----------

entriesgender.printSchema()

# COMMAND ----------

medals.show()

# COMMAND ----------

medals.printSchema()

# COMMAND ----------

teams.show()

# COMMAND ----------

teams.printSchema()

# COMMAND ----------

# Find the top countries with the highest number of gold medals
top_gold_medal_countries = medals.orderBy("Gold",ascending = False).select("Team_Country","Gold").show()

# COMMAND ----------

# Calculate the average number of entries by gender for each discipline
average_entries_by_gender = entriesgender.withColumn(
    'Avg_Female', entriesgender['Female'] / entriesgender['Total']
).withColumn(
    'Avg_Male', entriesgender['Male'] / entriesgender['Total']
)
average_entries_by_gender.show()
     

# COMMAND ----------

athletes.repartition(1).write.mode("overwrite").option("header",'true').parquet("/mnt/tokyoolymic/transformed-data/athletes")
coaches.repartition(1).write.mode("overwrite").option("header","true").parquet("/mnt/tokyoolymic/transformed-data/coaches")
entriesgender.repartition(1).write.mode("overwrite").option("header","true").parquet("/mnt/tokyoolymic/transformed-data/entriesgender")
medals.repartition(1).write.mode("overwrite").option("header","true").parquet("/mnt/tokyoolymic/transformed-data/medals")
teams.repartition(1).write.mode("overwrite").option("header","true").parquet("/mnt/tokyoolymic/transformed-data/teams")