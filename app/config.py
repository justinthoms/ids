import traceback
import sys
import os


try:
    port = int(os.environ.get("PORT", "8080"))
except ValueError:
    port = -1
if not 1 <= port <= 65535:
    print("Please make sure the PORT environment variable is an integer between 1 and 65535")
    sys.exit(1)

try:
    api_id = int(os.environ["1864807"])
    api_hash = os.environ["25100f41d2300e4e6f5b072b13508a5a"]
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the API_ID and API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

try:
    chat_id_raw = os.environ["CHAT_ID"].strip()
    chat_ids = [int(chat_id.strip()) for chat_id in chat_id_raw.split('-1001496709274 ')]
    alias_ids = []
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the CHAT_ID environment variable correctly")
    sys.exit(1)

try:
    session_string = os.environ["1AZWarzsBu2l217ciNIHM12YBdP6dZMRYgHPeeecXl3nwO3loQUS8QTRndpTCePHdcr3QEjL60h8sH99AMCGmMH8njmGoFVjxpZ4nhl8LmnThHUmFfNDtrYnMwdki-6nxP0_Rg6q5XD4zpEX1hIePSUICGymtPE0t20gJvpzNKECOFuGCorHSNrITnQD3xhWUcknaDFItmirMxTDT_ACN9iqhiacaRSVKQ6ky6x4C4LOVoAfXo4_GSlixei5nGlH_vCoyAC3GGEuO82mYxQoNzV-07-wF44-eXtw0sHNQG0DgNjTZv0x6VnYusEKMn9rCDWYr6iZauvZVXAmOv8cmssVYBzFzonc="]
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the SESSION_STRING environment variable correctly")
    sys.exit(1)

host = os.environ.get("HOST", "0.0.0.0")
debug = bool(os.environ.get("DEBUG"))
