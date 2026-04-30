import dlt
from pyspark.sql.functions import *

@dlt.table(
    name="silver_patient_visits"
)

def silver_patient_visits():
    df= dlt.read("bronze_patient_visits")

    return df.withColumn("test_cost", col("number_of_tests") * 2000)\
             .withColumn("total_bill", col("consultation_fee") + col("test_cost"))\
             .filter(col("consultation_fee") > 0)\
             .select("visit_id", "patient_name", "city", upper(col("department")).alias("department"), "consultation_fee", "number_of_tests", "test_cost","total_bill")
