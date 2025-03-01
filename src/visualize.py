#!/usr/bin/env python3

# command line args
import argparse
import matplotlib.pyplot as plt
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

if args.key not in counts:
    print(f"Error: Key '{args.key}' not found in {args.input_path}")
    exit(1)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

sorted_items = sorted(counts[args.key].items(), key=lambda item: item[1])
top_items = sorted_items[-10:]  # Get the top 10

labels, values = zip(*top_items)

plt.figure(figsize=(12, 6))
plt.barh(labels, values, color='skyblue')  # Horizontal bar chart
plt.xlabel("Frequency" if not args.percent else "Percentage")
plt.ylabel("Hashtags / Languages")
plt.title(f"Top 10 occurrences for '{args.key}' in {args.input_path}")
plt.tight_layout()

output_filename = f"{args.input_path}_{args.key}.png".replace("#", "")
plt.savefig(output_filename, dpi=300)
print(f"Graph saved as {output_filename}")

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k, ':', v)
