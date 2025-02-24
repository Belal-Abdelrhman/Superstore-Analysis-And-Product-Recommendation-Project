# Superstore-Product-Recommendation-Analysis-Project

## Project Background
This project aims to enhance product recommendations and analyze sales trends using data from the Superstore dataset. It involves data cleaning, exploratory data analysis (EDA), clustering customers based on sales behavior, and developing a personalized product recommendation system. The insights generated help businesses understand customer purchasing patterns, optimize marketing efforts, and improve overall profitability.

Dataset Structure
The dataset contains customer transactions from an online retail platform, capturing key attributes such as:

Customer Data: Customer ID, Name, Segment, and Region.
Sales Data: Order details, product purchases, quantity, discount, and profit.
Product Information: Product categories, subcategories, and names.
The dataset consists of 10,000+ records with 36 columns, covering purchases across different regions and time periods.

Executive Summary
This project follows a structured approach to analyzing customer purchase behaviors and improving product recommendations using K-Means clustering and collaborative filtering techniques.

## Key Findings:
The "Consumer" segment contributes the highest profitability.
California is the top-performing state in terms of sales and profit.
Certain regions, like North Dakota, show underperformance, indicating potential marketing opportunities.
A personalized recommendation system was built to suggest relevant products based on customer purchase history and similarities within customer clusters.

Project Components
🔹 Data Processing & Analysis
Data Cleaning: Handling missing values, duplicate records, and outlier detection.
Exploratory Data Analysis (EDA): Visualizing sales trends, customer segmentation, and discount impact on profitability.
Feature Engineering: Extracting insights from sales trends and customer behavior.
🔹 Machine Learning Models
Customer Segmentation: Using K-Means clustering to group customers based on purchasing behavior.
Product Recommendation System: Implementing collaborative filtering to provide personalized product suggestions.
🔹 Visualization & Insights
Tableau Dashboards: Interactive visualizations for tracking sales, customer trends, and product performance.
Matplotlib & Seaborn: Used for data exploration and trend analysis.
🔹 Deployment & App Integration
A GUI-based application was built using Tkinter, allowing users to enter a Customer ID and receive product recommendations based on clustering results.

Code & Resources
📌 SQL Queries – Business-related queries for sales and customer analysis [Link]
📌 Interactive Tableau Dashboard – Sales insights & trend analysis [Link]
📌 Python Pipeline – EDA, Model Building, and Recommendation System Deployment [Link]
📌 Recommendation App Demo – GUI for product recommendations [Link]

Dashboard
![image](https://github.com/user-attachments/assets/75b309fe-786c-4b92-bc43-40456cebe1db)

Insights
Category 1: Profitable Market Segment
The "Consumer" category is the most profitable customer segment among our customer segments, generating the highest revenue and profit, highlighting its significance to our business.
Category 2: Top Performing Region
California emerged as the largest and most profitable market, contributing significantly to total sales.
Category 3: Underperforming Markets
North Dakota represents an underperforming market, requiring strategic attention to improve profitability and market share.
Category 4: Growth Forecast
The sales forecast predicts increased sales in Q4 of 2018, presenting growth opportunities for targeted marketing efforts.
Recommendations
Category 1: Capitalize on Growth Opportunities:
With the anticipated growth in Quarterly Sales Forecasting for 2018 Q4, it is advisable to allocate additional additional marketing resources to maximize sales opportunities during this period.
Category 2: Focus on the "Consumer" Category:
Develop targeted marketing campaigns, personalized promotions, and enhanced customer experiences to further boost profitability within the "Consumer" segment segment.
Category 3. Optimize Market Strategies:
As California is the most profitable market, it is essential to continue investing in this region through focused marketing efforts, maintaining customer loyalty, and increasing market share.
Category 4. Improve Underperforming Markets:
Conduct in-depth market research in North Dakota to understand consumer behavior and tailor marketing efforts to boost sales and profitability in the region.
Assumptions and Caveats
Assumptions:
The data provided for analysis is accurate and reflects customer preferences and purchasing patterns.
The sales forecast is based on historical trends and assumes no major disruptions in market behavior.
Caveats:
Seasonal fluctuations and external factors like economic changes or unforeseen events may impact sales trends and market behavior, making forecast predictions less accurate.
The recommendation models are built on available data; their effectiveness may vary if customer preferences shift or if there is insufficient data for new products.
