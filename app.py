from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np
import joblib
import os

# Debugging info
print("Current working directory:", os.getcwd())
print("Files in this directory:", os.listdir())

app = Flask(__name__)

# Load pre-trained models
kmeans = joblib.load('kmeans_model.pkl')
scaler = joblib.load('scaler.pkl')

# Load data
ss_data = pd.read_csv('cleande_Superstore_data.csv')

'''# Preprocessing
for col in ss_data.select_dtypes(include=['object']).columns:
    ss_data[col] = ss_data[col].str.lower().str.strip()

ss_data['order date'] = pd.to_datetime(ss_data['order date'], dayfirst=True, errors='coerce')
ss_data['ship date'] = pd.to_datetime(ss_data['ship date'], dayfirst=True, errors='coerce')

ss_data['postal code'] = ss_data['postal code'].astype(str)
ss_data['state'] = ss_data['state'].fillna("vermont")
ss_data.drop(columns=['row id'], inplace=True)
ss_data = ss_data.drop_duplicates()'''

# Customer segmentation
customer_sales = ss_data.groupby('customer id', as_index=False)['sales'].median()
customer_sales['sales_scaled'] = scaler.transform(customer_sales[['sales']])
customer_sales['cluster'] = kmeans.predict(customer_sales[['sales_scaled']])

# Merge cluster info
ss_data = ss_data.merge(customer_sales[['customer id', 'cluster']], on='customer id', how='left')

# Product recommendation function (personalized, excluding already purchased)
def recommend_products_for_user(customer_id, top_n=10):
    if customer_id not in ss_data['customer id'].values:
        return ["No recommendations available."]

    user_cluster = ss_data.loc[ss_data['customer id'] == customer_id, 'cluster'].iloc[0]
    cluster_users = ss_data.loc[ss_data['cluster'] == user_cluster, 'customer id'].unique()
    cluster_purchases = ss_data.loc[ss_data['customer id'].isin(cluster_users), 'product name']

    if cluster_purchases.empty:
        return ["No purchase history available for this cluster."]

    top_products = cluster_purchases.value_counts().index.tolist()
    user_purchases = ss_data.loc[ss_data['customer id'] == customer_id, 'product name'].unique()
    recommendations = [p for p in top_products if p not in user_purchases]

    return recommendations[:top_n] if recommendations else ["No new recommendations available."]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    customer_id = request.form['customer_id'].lower().strip()

    if customer_id not in ss_data['customer id'].unique():
        return render_template('error.html')

    recommendations = recommend_products_for_user(customer_id)

    return render_template('results.html',
                           customer_id=customer_id,
                           recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
