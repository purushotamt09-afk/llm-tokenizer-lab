from transformers import AutoTokenizer
import tiktoken

def load_hf_tokenizer(model_name):
    return AutoTokenizer.from_pretrained(model_name)

def load_openai_tokenizer():
    return tiktoken.get_encoding("cl100k_base")

def tokenize_text(tokenizer, text):
    return tokenizer.encode(text)

def tokenize_openai(tokenizer, text):
    return tokenizer.encode(text)

def decode_text(tokenizer, tokens):
    return tokenizer.decode(tokens)

def decode_openai(tokenizer, tokens):
    return tokenizer.decode(tokens)