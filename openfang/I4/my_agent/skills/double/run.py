#!/usr/bin/env python3
"""
run.py — Skill double cho OpenFang
I4 - Pham Quoc Dat

Input  (stdin JSON): {"number": 21}
Output (stdout JSON): {"result": 42}
"""

import sys
import json


def main():
    try:
        # OpenFang truyen input qua stdin duoi dang JSON
        raw = sys.stdin.read().strip()
        input_data = json.loads(raw)

        number = input_data.get("number", None)

        if number is None:
            print(json.dumps({"error": "Thieu truong 'number' trong input"}))
            sys.exit(1)

        # Thu chuyen sang int (chap nhan ca string so, vi du "21")
        try:
            number = int(number)
        except (ValueError, TypeError):
            print(json.dumps({
                "error": f"Input phai la so nguyen, nhan duoc: '{number}'"
            }))
            sys.exit(1)

        result = number * 2

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
