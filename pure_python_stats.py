#!/usr/bin/env python
# coding: utf-8


import csv
from collections import defaultdict, Counter
from statistics import mean, stdev

# Step 1: Load the data

import sys
DATA_PATH = '2024_fb_posts_president_scored_anon.csv'
if len(sys.argv) > 1:
    DATA_PATH = sys.argv[1]
with open(DATA_PATH, newline='', encoding='utf-8') as csvfile: 
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

# Step 2: Helper functions
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def compute_stats(values):
    stats = {"count": len(values)}
    if all(isinstance(v, (int, float, float)) for v in values):
        stats.update({
            "mean": mean(values) if values else None,
            "min": min(values),
            "max": max(values),
            "std_dev": stdev(values) if len(values) > 1 else 0.0
        })
    else:
        counter = Counter(values)
        stats.update({
            "unique_values": len(counter),
            "most_common": counter.most_common(1)[0] if counter else None
        })
    return stats

# Step 3: Detect numeric vs non-numeric columns
numeric_columns = set()
column_values = defaultdict(list)

for row in data[:100]:  # sample to detect types
    for k, v in row.items():
        v = v.strip()
        if v == '':
            continue
        if is_number(v):
            column_values[k].append(float(v))
            numeric_columns.add(k)
        else:
            column_values[k].append(v)

# Step 4: Print overall stats
print("\n===== OVERALL STATISTICS =====")
for col, vals in column_values.items():
    print(f"\nColumn: {col}")
    for k, v in compute_stats(vals).items():
        print(f"  {k}: {v}")

# Step 5: Grouped analysis by Page Admin Top Country
grouped = defaultdict(list)
# Print keys in a sample row to help identify the correct key
print("\nSample row keys:", data[0].keys())
for row in data:
    grouped[row['Page Admin Top Country']].append(row)

print("\n===== GROUPED BY Page Admin Top Country =====")
for group_key, rows in grouped.items():
    print(f"\n--- Group: {group_key} ---")
    col_vals = defaultdict(list)
    for row in rows:
        for col, val in row.items():
            val = val.strip()
            if val == '':
                continue
            if col in numeric_columns and is_number(val):
                col_vals[col].append(float(val))
            else:
                col_vals[col].append(val)
    for col, vals in col_vals.items():
        print(f"\nColumn: {col}")
        for k, v in compute_stats(vals).items():
            print(f"  {k}: {v}")





