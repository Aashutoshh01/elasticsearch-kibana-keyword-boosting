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
🐳 Step 1: Run Elasticsearch + Kibana Using Docker

```bash
docker-compose up -d
