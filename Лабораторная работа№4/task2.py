import json
import os

INPUT_FILENAME = "input.json"

def task() -> float:
    with open(INPUT_FILENAME) as f:
        data = json.load(f)
    sum_result = sum([item["score"] * item["weight"] for item in data])
    return round(sum_result, 3)

print(task())