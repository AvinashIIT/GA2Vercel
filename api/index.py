import json
import os
from urllib.parse import parse_qs

# Load data from JSON file
with open(os.path.join(os.path.dirname(__file__), '../q-vercel-python.json')) as f:
    data = json.load(f)

# Create a name → marks mapping
name_to_marks = {entry["name"]: entry["marks"] for entry in data}

def handler(request, response):
    # Enable CORS
    response.headers["Access-Control-Allow-Origin"] = "*"

    # Parse names from query string
    query_params = parse_qs(request.query_string.decode())
    names = query_params.get("name", [])

    # Get marks in same order
    marks = [name_to_marks.get(name, None) for name in names]

    return response.json({"marks": marks})
