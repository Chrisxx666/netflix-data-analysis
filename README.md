# Netflix Data Analysis Project

📊 **Interactive Dashboard**: [View on Looker Studio](https://lookerstudio.google.com/s/vABoS93hhe0)

---

## 📝 Project Overview
This project is a full-cycle data analysis of Netflix's content catalog. It covers data cleaning, transformation, SQL-based storage, and visualization using modern tools such as Python, MySQL, and Google Looker Studio.

The goal is to demonstrate practical data handling, pipeline creation, and reporting skills suited for fully remote data roles.

---

## 🧰 Tools & Technologies
- **Python**: Data processing & automation
- **pandas**: Data cleaning & transformation
- **MySQL**: Data storage and querying
- **Looker Studio**: Interactive data visualization
- **Git + GitHub**: Version control and portfolio hosting

---

## 📁 Project Structure
```
netflix-analysis/
├── data/
│   ├── netflix_titles.csv             # Raw data
│   └── netflix_cleaned.csv            # Cleaned data after processing
│
├── notebooks/
│   ├── 01_load_and_preview.py         # Load and inspect raw data
│   ├── 02_clean_and_format.py         # Clean and transform data
│   ├── 03_exploratory_analysis.py     # Chart from CSV
│   ├── 04_sql_analysis.py             # Chart from MySQL
│   ├── load_to_mysql.py               # Upload cleaned data to MySQL
│   └── mysql_config.py                # MySQL connection settings
│
├── README.md
├── requirements.txt (optional)
```

---

## 🔍 Key Insights Visualized
1. **Yearly Content Trend**: Number of titles added to Netflix each year
2. **Content Type Split**: Movie vs TV Show distribution
3. **Top Countries**: Countries with the most Netflix content
4. **Rating Distribution**: Content ratings (TV-MA, PG, etc.) breakdown

---

## 🚀 How to Use
1. Clone the repository
2. Update your MySQL config in `mysql_config.py`
3. Run the pipeline in order:
   - `01_load_and_preview.py`
   - `02_clean_and_format.py`
   - `load_to_mysql.py`
   - Use Looker Studio with MySQL connection for visuals

---

## 📌 Author
**Chris Tsai**  
Remote-focused data analyst in training — building real-world projects with Python + SQL

---

## 🧭 Future Work
- Add content category segmentation analysis
- Connect to BigQuery for scalability
- Embed project into personal portfolio site

---

## 🗂 License
This project is open for educational and demonstration purposes.

