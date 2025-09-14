# S3 Data Processing Pipeline Using AWS Glue

## 📖 Project Overview
This project demonstrates how to build a serverless data processing pipeline using **Amazon S3** and **AWS Glue**. The pipeline ingests raw data files from an S3 bucket, processes and transforms the data using AWS Glue Studio, and stores the results in another S3 bucket in JSON format.

---

## ✅ What I Have Implemented

1. **Amazon S3 Input Bucket**  
   - Created an S3 bucket where I upload data files (in `.csv` or `.txt` format).
   - These files contain raw data that needs to be processed.

2. **Amazon S3 Output Bucket**  
   - Created another S3 bucket where the processed results are stored.
   - The output is in `.json` format after transformation.

3. **AWS Glue Pipeline**  
   - Configured a **Crawler** to scan and catalog the raw data stored in the input bucket.
   - Used **AWS Glue Studio** to build an **ETL job** that reads the cataloged data, transforms it, and writes the output into the destination S3 bucket in JSON format.

---

## 🛠 Tools & Technologies Used

- **Amazon S3** – For storing both input files and processed output.
- **AWS Glue Studio** – For orchestrating and managing the ETL pipeline.
- **AWS Glue Crawler** – To scan and catalog datasets in S3.
- **ETL (Extract, Transform, Load)** – To process the raw data and convert it to a structured format.
- **JSON** – The format in which the transformed data is stored.

---

## 📂 Input File Format

The input files can be in `.csv` or `.txt` format containing structured or semi-structured data. For example:

```csv
id,name,salary,country
1,John Doe,70000,USA
2,Jane Smith,80000,Canada
3,Alice Brown,90000,USA
