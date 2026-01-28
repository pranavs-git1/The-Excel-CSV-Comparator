# The "Excel/CSV" Comparator
# 1. Project Title & Goal
A Python-based ETL testing utility designed to perform row-by-row validation between a source data file and a target migration file to ensure data integrity.

# 2. Setup Instructions
To run this script, ensure you have Python installed and follow these commands:

"Bash"
Install the required library
pip install pandas

Run the comparison script
python comparator.py

# 3. The Logic (How I Thought)
Why this approach? 
I chose Pandas over the standard CSV library because of its "vectorized" comparison capabilities. Instead of writing nested loops to check every cell (which is slow for large datasets), Pandas allows us to compare entire DataFrames instantly using df1 != df2. This makes the code more readable, maintainable, and significantly faster for actual ETL production environments.

Hardest Bug & Fix: The most common issue was Index Misalignment. If the source and target files were sorted differently, the script flagged every row as a mismatch even if the data was identical.

The Fix: I implemented a sorting step using sort_values() on a unique identifier (like ID) before the comparison. This ensures we are comparing "Apples to Apples" regardless of the order in which the database exported the rows.

# 4. Output Screenshots


# 5. Future Improvements
If I had two more days to refine this tool, I would add:

Tolerance Levels: For financial data, I’d add a "fuzzy match" feature where differences of less than 0.01% are ignored to account for minor rounding discrepancies between systems.

HTML Reporting: Instead of just printing to the console, I would generate a visual HTML report with mismatched cells highlighted in red for easier debugging by non-technical stakeholders.

Schema Validation: A pre-check to ensure column names and data types (e.g., String vs. Integer) match before comparing the actual values.
