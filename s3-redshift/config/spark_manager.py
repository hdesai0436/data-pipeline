from pyspark.sql import SparkSession
from dotenv import load_dotenv
import os #provides ways to access the Operating System and allows us to read the environment variables

load_dotenv()
access_key_id = os.getenv('access_key_id')
secret_access_key = os.getenv('secret_access_key')
spark = (SparkSession.builder.master('local[*]').appName('bigdata') 
     .config("spark.executor.instances", "1") 
    .config("spark.executor.memory", "6g") 
    .config("spark.driver.memory", "6g") 
    .config("spark.executor.memoryOverhead", "8g") 
    
    .getOrCreate())


spark._jsc.hadoopConfiguration().set("fs.s3.awsAccessKeyId",access_key_id)
spark._jsc.hadoopConfiguration().set("fs.s3.awsSecretAccessKey",secret_access_key)



