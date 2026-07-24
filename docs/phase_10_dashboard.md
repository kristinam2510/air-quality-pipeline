# Phase 10 — Dashboard & Analytics Layer

## Objective

The objective of this phase is to visualize air quality insights and create an interactive analytics dashboard for monitoring pollution patterns.

The dashboard consumes data from the **ClickHouse Gold Layer** and presents meaningful insights using **Metabase**.

---

# Architecture

```
ClickHouse Gold Layer
        |
        |
        ↓
     Metabase
        |
        |
        ↓
Air Quality Analytics Dashboard
```

---

# Technology Used

| Component | Technology |
|-----------|------------|
| Visualization Tool | Metabase |
| Database | ClickHouse |
| Analytics Layer | Gold Layer |
| Query Language | SQL |

---

# Dashboard Name

## Air Quality Analytics Dashboard

The dashboard provides insights into:

- Overall AQI levels
- Number of monitored cities
- Pollution trends
- Highly polluted cities
- AQI category distribution
- City-wise pollution comparison

---

# Data Sources

The dashboard is connected to the following Gold tables:

```
gold.daily_city_aqi

gold.city_rankings

gold.pollution_trends

gold.aqi_summary_agg
```

---

# Dashboard Cards

## 1. Overall Average AQI

### Visualization

```
Number Card
```

### Purpose

Displays the overall average AQI value across all monitored cities.

### Query

```sql
SELECT
    round(avg(avg_aqi),2) AS overall_average_aqi
FROM gold.daily_city_aqi
WHERE isFinite(avg_aqi);
```

---

# 2. Total Cities

### Visualization

```
Number Card
```

### Purpose

Displays the total number of cities available in the dataset.

### Query

```sql
SELECT
    countDistinct(City) AS total_cities
FROM gold.daily_city_aqi;
```

---

# 3. Total AQI Records

### Visualization

```
Number Card
```

### Purpose

Shows the total number of AQI observations available for analysis.

### Query

```sql
SELECT
    count() AS total_records
FROM gold.daily_city_aqi;
```

---

# 4. AQI Trend Over Time

### Visualization

```
Line Chart
```

### Purpose

Shows how air quality changes over time.

### Query

```sql
SELECT
    Date,
    round(avg(avg_aqi),2) AS average_aqi
FROM gold.daily_city_aqi
WHERE isFinite(avg_aqi)
GROUP BY Date
ORDER BY Date;
```

---

# 5. Top 10 Most Polluted Cities

### Visualization

```
Bar Chart
```

### Purpose

Identifies cities with the highest average AQI levels.

### Query

```sql
SELECT
    City,
    round(average_aqi,2) AS average_aqi
FROM gold.city_rankings
WHERE isFinite(average_aqi)
ORDER BY average_aqi DESC
LIMIT 10;
```

---

# 6. AQI Category Distribution

### Visualization

```
Pie Chart
```

### Purpose

Shows the distribution of pollution severity levels.

Categories:

- Good
- Moderate
- Poor
- Very Poor
- Severe

### Query

```sql
SELECT
    CASE
        WHEN avg_aqi <= 50 THEN 'Good'
        WHEN avg_aqi <= 100 THEN 'Moderate'
        WHEN avg_aqi <= 200 THEN 'Poor'
        WHEN avg_aqi <= 300 THEN 'Very Poor'
        ELSE 'Severe'
    END AS AQI_Category,
    count() AS records
FROM gold.daily_city_aqi
WHERE isFinite(avg_aqi)
GROUP BY AQI_Category
ORDER BY records DESC;
```

---

# Dashboard Layout

```
------------------------------------------------

| Overall AQI | Total Cities | Total Records |

------------------------------------------------

|              AQI Trend Line Chart            |

------------------------------------------------

| Top Polluted Cities | AQI Category Pie Chart |

------------------------------------------------
```

---

# Insights Generated

The dashboard provides:

- Average pollution level monitoring
- Identification of highly polluted cities
- Historical AQI trend analysis
- Pollution severity classification
- City-wise comparison

---

# Phase 10 Deliverable

Completed:

✅ Metabase dashboard creation  
✅ ClickHouse Gold layer integration  
✅ Interactive AQI visualizations  
✅ Pollution trend analysis  
✅ City ranking analysis  
✅ Analytics-ready dashboard layer  

---

# Conclusion

The Dashboard & Analytics Layer converts processed air quality data into meaningful visual insights. By connecting Metabase with the ClickHouse Gold layer, users can efficiently analyze pollution trends and identify areas with poor air quality.
