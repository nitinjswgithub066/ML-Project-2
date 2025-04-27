import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Sample lists for synthetic data generation
query_texts = [
    "How do I register for courses?",
    "What is the deadline for fee payment?",
    "I cannot access my student portal.",
    "When is the semester starting?",
    "I need help with course selection.",
    "My grade has not been updated.",
    "How can I get a transcript?",
    "Website shows error 404.",
    "Is there any scholarship available?",
    "I forgot my password, need assistance."
]
query_categories = ["Academic", "Financial", "Technical", "Administrative"]
resolved_flags = ["Yes", "No"]

rows = []
start_time = datetime(2025, 4, 1, 9, 0)

# Generate 1,500 rows for a larger synthetic dataset
for i in range(1, 1501):
    timestamp = start_time + timedelta(minutes=5 * i)
    row = {
        "Query_ID": i,
        "Timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "Student_ID": np.random.randint(1000, 1100),
        "Query_Text": np.random.choice(query_texts),
        "Query_Category": np.random.choice(query_categories),
        "Satisfaction_Score": round(np.random.uniform(3.0, 5.0), 1),
        "Response_Time": np.random.randint(10, 45),
        "Resolved_Flag": np.random.choice(resolved_flags)
    }
    rows.append(row)

df = pd.DataFrame(rows)
df.to_csv("query data.csv", index=False)
print("CSV file 'synthetic_data_large.csv' generated with 1500 rows.")
