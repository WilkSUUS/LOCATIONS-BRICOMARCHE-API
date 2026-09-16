import requests

headers = {
    "accept": "application/vnd.enp.api+json;version=v1",
    "content-website": "4",
    "pagination-limit": "100000",
    "x-spark": "hybrid",
    "user-agent": "Mozilla/5.0"
}

r = requests.get(
    "https://www.bricomarche.pl/api/pos/list",
    headers=headers,
    timeout=60
)

print("STATUS:", r.status_code)
print(r.text[:500])
