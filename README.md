# elasticsearch-kibana-keyword-boosting
# 🔍 Elasticsearch + Kibana: Keyword-Catalog Relevance Boosting

This project demonstrates how to use **Elasticsearch** and **Kibana** to build a relevance boosting system based on **user search behavior** for a product catalog.

## 🚀 Project Overview

- Simulate a search catalog (products, brands, categories)
- Generate synthetic user search logs
- Analyze clicked data to compute boosting scores
- Apply boosting to search results using Elasticsearch's `function_score`
- Visualize catalog, query patterns, and impact in Kibana

---

## 📦 Project Structure

```bash
.
├── docker-compose.yml            # Elasticsearch + Kibana setup
├── catalog.json                  # Synthetic catalog data
├── search_logs.json              # Simulated user search behavior
├── catalog_mapping.json          # Elasticsearch mapping for catalog index
├── bulk_catalog.json             # Bulk indexing format for catalog
├── calculate_boosts.py           # Python script to compute boosting weights
├── boost_map.json                # Output of boosting weights
└── README.md
```
## 🐳 Step 1: Run Elasticsearch + Kibana Using Docker

```bash
docker-compose up -d
```
Elasticsearch: http://localhost:9200

Kibana: http://localhost:5601

## 📊 Step 2: Index the Catalog in Elasticsearch
```bash
curl -X PUT "localhost:9200/apnamart_catalog" \
-H 'Content-Type: application/json' \
-d @catalog_mapping.json

curl -X POST "localhost:9200/_bulk" \
-H 'Content-Type: application/json' \
--data-binary @bulk_catalog.json
```

## 🧠 Step 3: Generate Boosting Weights
Run the Python script to analyze search logs and compute brand/product_type boost weights:
```bash
python3 calculate_boosts.py > boost_map.json
```
Sample output:
```bash
{
  "milk": {
    "brands": {"Amul": 1.0, "Sudha": 0.5},
    "product_types": {"Milk": 1.0, "Curd": 0.75}
  }
}
```



