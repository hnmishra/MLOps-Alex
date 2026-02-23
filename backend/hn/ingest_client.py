import os
import requests
from typing import Any, Dict, Optional

# Endpoint from environment variable or default
API_ENDPOINT = os.getenv(
    "ALEX_API_ENDPOINT",
    "https://z6vs4ben0m.execute-api.us-east-1.amazonaws.com/prod/ingest",
)

# Set your API key in environment variable or pass directly
API_KEY = os.getenv("ALEX_API_KEY")  # <-- put your 'xxxx' value here in env
API_KEY="xxx"
API_ENDPOINT = "https://z6vs4ben0m.execute-api.us-east-1.amazonaws.com/prod/ingest"


class IngestError(Exception):
    """Raised when the ingest API call fails."""


def send_to_ingest(
    payload: Dict[str, Any],
    api_key: Optional[str] = None,
    timeout: int = 30,
) -> Dict[str, Any]:
    """
    Send data to the ingest API.

    Args:
        payload: JSON-serializable dict to send
        api_key: Optional API Gateway API key
        timeout: Request timeout in seconds

    Returns:
        Parsed JSON response

    Raises:
        IngestError on non-2xx responses
    """
    headers = {
        "Content-Type": "application/json",
    }

    # Use provided API key or default environment key
    key_to_use = api_key or API_KEY
    if key_to_use:
        headers["x-api-key"] = key_to_use

    try:
        response = requests.post(
            API_ENDPOINT,
            json=payload,
            headers=headers,
            timeout=timeout,
        )
    except requests.RequestException as exc:
        raise IngestError(f"Failed to connect to ingest API: {exc}") from exc

    if not response.ok:
        raise IngestError(
            f"Ingest API error {response.status_code}: {response.text}"
        )

    if not response.content:
        return {}

    return response.json()