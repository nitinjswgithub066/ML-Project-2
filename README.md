# **Project Database Instruction**

## **Database Overview**

This branch contains the database for the **_Intelligent Student Query Advisor and FAQ Enhancer_** project. The database is generated using Python's random functions and is stored in **_CSV format_**. It simulates a large set of student query data for training and testing machine learning models.

---

## **Database Features**

- **Data Generation:**  
  The database is programmatically created in Python using random functions to simulate realistic student data.

- **Data Format:**  
  The data is saved in **CSV format**, making it easy to load into Python with libraries like Pandas.

- **Size:**  
  The CSV file contains more than **1,500 rows** of data. Each row represents a unique student query.

---

## **Data Structure**

The CSV database consists of the following **columns**:

- **Query_ID:**  
  Unique identifier for each query.
- **Timestamp:**  
  Date and time when the query was submitted.

- **Student_ID:**  
  Unique identifier for the student who submitted the query.

- **Query_Text:**  
  The content of the student query, generated from a predefined set of query phrases.

- **Query_Category:**  
  The category assigned to the query (e.g., Academic, Technical, Financial, Administrative).

- **Satisfaction_Score:**  
  A floating-point number between 3.0 and 5.0 representing student satisfaction.

- **Response_Time:**  
  The time taken (in minutes) to resolve the query, generated as a random value.

- **Resolved_Flag:**  
  A flag indicating whether the query was resolved (`Yes` or `No`).

---

## **Example Row**

Below is an example of how the data is structured:

| **Query_ID** | **Timestamp**       | **Student_ID** | **Query_Text**                        | **Query_Category** | **Satisfaction_Score** | **Response_Time** | **Resolved_Flag** |
| ------------ | ------------------- | -------------- | ------------------------------------- | ------------------ | ---------------------- | ----------------- | ----------------- |
| 1            | 2025-04-01 09:15:00 | 1001           | How do I register for courses?        | Academic           | 4.5                    | 15                | Yes               |
| 2            | 2025-04-01 09:20:00 | 1002           | What is the deadline for fee payment? | Financial          | 4.2                    | 20                | Yes               |

---

## **How the Database Was Created**

- **Random Data Generation:**

  - **Query_ID:** Sequential numbers from 1 to 1,500.
  - **Timestamp:** Randomly generated within a defined time range.
  - **Student_ID:** Random integers to simulate unique student identifiers.
  - **Query_Text:** Selected randomly from a predefined list of query phrases.
  - **Query_Category:** Randomly chosen among predetermined categories.
  - **Satisfaction_Score:** Generated as random floats between 3.0 and 5.0.
  - **Response_Time:** Generated as random integers within a realistic time range (e.g., 10–45 minutes).
  - **Resolved_Flag:** Randomly assigned as either "Yes" or "No".

- **Reproducibility:**  
  Random seeds can be set in the Python script for reproducible data generation.

---

## **Usage Instructions**

1. **Loading the CSV File in Python:**

   Syntax for using **_csv file_** in **Program**

   ```python
   import pandas as pd

   # Load the CSV file
   stu_query = pd.read_csv('query_data.csv')

   # Display the first few rows and column
   print(stu_query.head())

   # Display all rows and column
   stu_query
   ```

---

---
