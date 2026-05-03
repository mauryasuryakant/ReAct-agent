import json
import re

def parse_response(text):
    action = None
    action_input = {}

    # Extract Action (case insensitive)
    action_match = re.search(r"Action:\s*(\w+)", text, re.IGNORECASE)
    if action_match:
        action = action_match.group(1).lower()

    # Extract Action Input (case insensitive)
    input_match = re.search(
        r"Action\s*Input:\s*(\{.*?\})",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if input_match:
        try:
            action_input = json.loads(input_match.group(1))
        except:
            action_input = {}

    return action, action_input