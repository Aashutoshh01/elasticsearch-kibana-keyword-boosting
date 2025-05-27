import json
from collections import defaultdict

# Load search logs
with open('search_logs.json') as f:
    logs = json.load(f)

# Load catalog data for lookup
with open('catalog.json') as f:
    catalog = json.load(f)
id_to_brand = {item['id']: item['brand'] for item in catalog}
id_to_product_type = {item['id']: item['product_type'] for item in catalog}

# Aggregate counts
keyword_brand_counts = defaultdict(lambda: defaultdict(int))
keyword_product_type_counts = defaultdict(lambda: defaultdict(int))

for entry in logs:
    q = entry['query']
    pid = entry['clicked_product_id']
    brand = id_to_brand.get(pid, 'unknown')
    ptype = id_to_product_type.get(pid, 'unknown')
    keyword_brand_counts[q][brand] += 1
    keyword_product_type_counts[q][ptype] += 1

# Normalize scores between 0 and 1
def normalize(d):
    max_val = max(d.values()) if d else 1
    return {k: v/max_val for k,v in d.items()}

result = {}
for kw in keyword_brand_counts.keys():
    result[kw] = {
        "brands": normalize(keyword_brand_counts[kw]),
        "product_types": normalize(keyword_product_type_counts[kw])
    }

print(json.dumps(result, indent=2))
