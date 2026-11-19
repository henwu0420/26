# scripts/generate_explanations.py
# This script reads raw_mcqs.json and enriches each question with comprehensive explanations,
# key concepts, option-by-option analysis, and exam tips.

import json
import re

with open('raw_mcqs.json', 'r', encoding='utf-8') as f:
    mcqs = json.load(f)

# Let's inspect the items and write rule-based and expert detailed content for all 103 questions.
print(f"Loaded {len(mcqs)} questions for enrichment.")
