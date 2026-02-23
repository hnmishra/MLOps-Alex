from ingest_client import send_to_ingest

data = {
    "url": "https://example.com",
    "title": "Example Page",
    "text": "Some extracted text"  # Required by API
}

# Option 1: Use environment variable
result = send_to_ingest(data)
print("Result:", result)

# Option 2: Pass API key directly
result = send_to_ingest(data, api_key="xxx")  # your alex-api-key here
print("Result:", result)