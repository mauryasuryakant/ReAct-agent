# import json
# import re

# def parse_response(text):
#     action = None
#     action_input = {}

#     # Extract Action
#     action_match = re.search(r"Action:\s*(\w+)", text, re.IGNORECASE)
#     if action_match:
#         action = action_match.group(1).lower()

#     # Extract Action Input (flexible)
#     input_match = re.search(r"Action\s*Input:\s*(.*)", text, re.IGNORECASE)
#     if input_match:
#         raw_input = input_match.group(1).strip()

#         try:
#             action_input = json.loads(raw_input)
#         except:
#             # fallback: treat as plain string
#             action_input = raw_input.strip('"')

#     return action, action_input

import json
import re

def parse_response(text):
    action = None
    action_input = {}

    # --- Extract ALL actions (take the LAST one) ---
    action_matches = re.findall(r"Action:\s*(\w+)", text, re.IGNORECASE)
    if action_matches:
        action = action_matches[-1].lower()

    # --- Extract ALL inputs (take the LAST one) ---
    input_matches = re.findall(
        r"Action\s*Input:\s*(\{.*?\}|\".*?\"|[^\n]+)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if input_matches:
        raw_input = input_matches[-1].strip()

        # Try parsing JSON
        try:
            action_input = json.loads(raw_input)
        except:
            # If not JSON, treat as plain string
            action_input = raw_input.strip('"')

    return action, action_input