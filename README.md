# 📊 Marketing Funnel & Conversion Analysis

🚀 This project is part of my **Data Science & Analytics Internship (Task 3)**, where I analyzed real-world e-commerce behavior data to understand user journeys, conversion rates, and business performance.

---

## 📌 Problem Statement

Analyze marketing funnel data to:
- Identify **conversion drop-offs**
- Understand **user behavior patterns**
- Evaluate **brand and category performance**
- Generate **actionable business insights**

---

## 📂 Project Structure

```
├── README.md
├── .gitignore
├── .env.example
├── notebooks/
│   └── analysis.ipynb
├── screenshots/
│   ├── 1_marketing_funnel.png
│   ├── 2_hourly_activity.png
│   ├── 3_daily_activity.png
│   ├── 4_price_bracket_cr.png
│   ├── 5_purchase_price_dist.png
│   ├── 6_event_distribution.png
│   ├── 7_weekly_active_users.png
│   ├── 8_brand_engagement.png
│   ├── 9_category_interest.png
│   └── 10_brand_conversion_efficiency.png
└── scripts/
    ├── download_dataset.py
    ├── extract_dataset.py
    └── clean_data.py
```

---

## ⚙️ Tech Stack

- **Python**
- **Pandas**
- **KaggleHub**
- **Data Visualization (Matplotlib/Seaborn)**

---

## 🔄 Data Pipeline (ETL Process)

### 1. Extract
- Download dataset from Kaggle using `kagglehub`
- Handle large dataset efficiently

### 2. Transform (Data Cleaning)
- Removed missing values (`user_id`, `user_session`)
- Filtered invalid price values
- Handled null categories & brands
- Removed duplicate events
- Standardized datetime format

### 3. Load
- Saved cleaned dataset for analysis

---

## 📊 Key Analysis & Visualizations

### 🔹 Marketing Funnel
- Tracked user journey: **View → Cart → Purchase**
- Identified major drop-off points

### 🔹 User Activity Analysis
- Hourly activity trends
- Daily engagement patterns

### 🔹 Conversion Insights
- Conversion rate by price segments
- Purchase distribution

### 🔹 Engagement Analysis
- Brand-level engagement
- Category interest trends

### 🔹 Retention & Growth
- Weekly active users
- Event distribution patterns

---

## 📈 Key Insights

- Significant drop-offs occur between **view → cart stage**
- Certain price ranges show **higher conversion efficiency**
- A few brands dominate **user engagement and conversions**
- Peak activity occurs during **specific hours of the day**
- Weekly trends indicate **consistent returning users**

---

## 🧠 Learnings

- Handling large datasets using **chunk processing**
- Importance of **data cleaning in real-world datasets**
- Building a **complete data pipeline (ETL)**
- Translating raw data into **business insights**
- Importance of **data storytelling**

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/Aryan-202/FUTURE_DS_03.git
cd FUTURE_DS_03
```

### 2. Setup Environment

Create a `.env` file:

```
FILE_PATH = /path/to/dataset.csv
```

### 3. Run Scripts

```bash
python scripts/download_dataset.py
python scripts/extract_dataset.py
python scripts/clean_data.py
```

---

## 📸 Sample Outputs

> Visualizations are available in the `screenshots/` folder.

---

## 🔗 Dataset

* E-commerce behavior dataset (multi-category store)

---

## 🎯 Conclusion

This project demonstrates how raw user interaction data can be transformed into actionable insights using data analysis techniques. The focus was not just on visualization, but on identifying real business problems and opportunities for improvement.

---

## 📬 Connect With Me

If you found this project interesting, feel free to connect with me on LinkedIn!

---

⭐ If you like this project, consider giving it a star!
