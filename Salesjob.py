import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node AmazonS3source
AmazonS3source_node1757830871789 = glueContext.create_dynamic_frame.from_catalog(database="salesdb", table_name="gluebucket00001", transformation_ctx="AmazonS3source_node1757830871789")

# Script generated for node AmazonS3dest
EvaluateDataQuality().process_rows(frame=AmazonS3source_node1757830871789, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1757830810548", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3dest_node1757830894276 = glueContext.write_dynamic_frame.from_options(frame=AmazonS3source_node1757830871789, connection_type="s3", format="json", connection_options={"path": "s3://mgluejson", "partitionKeys": []}, transformation_ctx="AmazonS3dest_node1757830894276")

job.commit()