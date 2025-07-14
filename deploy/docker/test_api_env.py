#!/usr/bin/env python3
"""
Test environment loading for the API server
"""
import os
import sys
from pathlib import Path

# Add the docker directory to the path so we can import utils
sys.path.insert(0, str(Path(__file__).parent))

from utils import load_config

print("Testing API server environment loading...")
print(f"Current working directory: {os.getcwd()}")
print(f"Script location: {Path(__file__).parent}")

# Test config loading
config = load_config()
print(f"Config loaded successfully: {bool(config)}")
print(f"LLM provider: {config.get('llm', {}).get('provider', 'Not found')}")
print(f"API key env var name: {config.get('llm', {}).get('api_key_env', 'Not found')}")

# Check if the environment variable is now available
api_key_env = config.get('llm', {}).get('api_key_env', '')
api_key = os.getenv(api_key_env, '')
print(f"Environment variable '{api_key_env}' loaded: {bool(api_key)}")
print(f"API key length: {len(api_key) if api_key else 0}")
print(f"API key (first 8 chars): {api_key[:8] if api_key else 'None'}...")

# Test the exact same logic as the API code
if "api_key" in config["llm"]:
    final_api_key = config["llm"]["api_key"]
    print(f"Using direct API key from config")
else:
    final_api_key = os.environ.get(config["llm"].get("api_key_env", None), "")
    print(f"Using API key from environment variable")

print(f"Final API key that would be used: {bool(final_api_key)}")
print(f"Final API key length: {len(final_api_key) if final_api_key else 0}")
