#!/usr/bin/env python3
"""
run.py — Skill uppercase cho OpenFang
I4 - Pham Quoc Dat

Input  (stdin JSON): {"text": "hello world"}
Output (stdout JSON): {"result": "HELLO WORLD"}
"""

import sys
import json


def main():
    try:
        # OpenFang truyen input qua stdin duoi dang JSON
        raw = sys.stdin.read().strip()
        input_data = json.loads(raw)

        text = input_data.get("text", "")

        if not isinstance(text, str):
            print(json.dumps({
                "error": f"Input phai la string, nhan duoc: {type(text).__name__}"
            }))
            sys.exit(1)

        result = text.upper()

        # Tra ket qua qua stdout dang JSON
        print(json.dumps({"result": result}))

    except json.JSONDecodeError as e:
        print(json.dumps({"error": f"Invalid JSON input: {e}"}))
        sys.exit(1)
    except Exception as e:
        print(json.dumps({"error": f"Unexpected error: {e}"}))
        sys.exit(1)


if __name__ == "__main__":
    main()
