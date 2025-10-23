"""Simple HTTP web client utility.

Implements a reusable `fetch` function that returns response status and JSON/text.
Also exposes a CLI entrypoint `main()` for quick requests.
"""
from __future__ import annotations

import argparse
import json
from typing import Tuple, Optional

import requests


def fetch(url: str, timeout: int = 10) -> Tuple[int, Optional[dict], str]:
    """Fetch a URL using GET.

    Returns:
        (status_code, json_obj_or_None, text)
    """
    resp = requests.get(url, timeout=timeout)
    try:
        body = resp.json()
    except Exception:
        body = None
    return resp.status_code, body, resp.text


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Simple HTTP GET client")
    parser.add_argument("url", help="URL to fetch")
    parser.add_argument("--timeout", "-t", type=int, default=10, help="Request timeout in seconds")
    parser.add_argument("--json", action="store_true", help="Pretty-print JSON if response is JSON")
    args = parser.parse_args(argv)

    try:
        status, body, text = fetch(args.url, timeout=args.timeout)
    except Exception as e:
        print(f"Request failed: {e}")
        return 2

    print(f"HTTP {status}")
    if args.json and body is not None:
        print(json.dumps(body, indent=2, ensure_ascii=False))
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
