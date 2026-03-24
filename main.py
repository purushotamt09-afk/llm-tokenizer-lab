import warnings
warnings.filterwarnings('ignore')

from transformers import AutoTokenizer
import requests
from dotenv import load_dotenv
import os

# =========================
# LOAD API KEY FROM .env
# =========================
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    print("❌ API key missing. Check your .env file")
    exit()

# =========================
# COLORS
# =========================
colors = [
    '102;194;165', '252;141;98', '141;160;203',
    '231;138;195', '166;216;84', '255;217;47'
]

# =========================
# FUNCTION: SHOW TOKENS
# =========================
def show_tokens(sentence: str, tokenizer_name: str):
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    token_ids = tokenizer(sentence).input_ids

    print(f"\n🔹 Model: {tokenizer_name}")
    print(f"Vocab length: {len(tokenizer)}")

    for idx, t in enumerate(token_ids):
        print(
            f'\x1b[0;30;48;2;{colors[idx % len(colors)]}m' +
            tokenizer.decode(t) +
            '\x1b[0m',
            end=' '
        )
    print("\n")

# =========================
# INPUT TEXT
# =========================
text = """
English and CAPITALIZATION
🎵 鸟
show_tokens False None elif == >= else: two tabs:"    " Three tabs: "       "
12.0*50=600
"""

print("\n===== TOKENIZER COMPARISON =====\n")

# =========================
# TOKENIZER COMPARISON
# =========================
show_tokens(text, "bert-base-cased")
show_tokens(text, "bert-base-uncased")
show_tokens(text, "gpt2")

# =========================
# OPENROUTER OUTPUT
# =========================
print("\n===== OPENROUTER OUTPUT =====\n")

try:
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": "Explain tokenization simply"}
            ]
        }
    )

    data = response.json()
    print(data["choices"][0]["message"]["content"])

except Exception as e:
    print("❌ Error:", e)