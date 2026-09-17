import requests
import json
import time

S2_API_URL = "https://api.semanticscholar.org/graph/v1"

def get_paper_details(doi):
    print(f"Fetching details for DOI: {doi}")
    url = f"{S2_API_URL}/paper/DOI:{doi}?fields=title,authors,year,abstract,citations,citations.title,citations.authors,citations.year,citations.abstract,citations.externalIds"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error {response.status_code} for DOI {doi}")
            return None
    except Exception as e:
        print(f"Exception for {doi}: {e}")
        return None
    finally:
        time.sleep(1) # rate limiting

dois = [
    "10.5194/ms-16-821-2025",
    "10.1007/s11465-025-0843-5",
    "10.1016/j.taml.2025.100633",
    "10.1109/TCST.2026.3690756" # Track B specific paper
]

results = {}
for doi in dois:
    data = get_paper_details(doi)
    if data:
        results[doi] = data

with open("outputs/verification/D1-V003/semantic_scholar_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("Saved results.")
