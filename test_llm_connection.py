#!/usr/bin/env python3
"""
Comprehensive test for Crawl4AI LLM connection
"""
import os
import sys
from pathlib import Path

def test_main_crawl4ai_config():
    """Test the main crawl4ai config"""
    print("=== Testing Main Crawl4AI Config ===")
    
    # Add main crawl4ai to path
    main_crawl4ai_path = Path(__file__).parent / "crawl4ai"
    sys.path.insert(0, str(main_crawl4ai_path))
    
    try:
        from config import PROVIDER_MODELS, DEFAULT_PROVIDER, DEFAULT_PROVIDER_API_KEY
        print(f"✅ Main config loaded successfully")
        print(f"Default provider: {DEFAULT_PROVIDER}")
        print(f"Default API key env: {DEFAULT_PROVIDER_API_KEY}")
        
        # Check if the API key is loaded
        deepseek_key = PROVIDER_MODELS.get("deepseek/deepseek-chat")
        print(f"DeepSeek API key loaded: {bool(deepseek_key)}")
        print(f"DeepSeek API key length: {len(deepseek_key) if deepseek_key else 0}")
        print(f"DeepSeek API key preview: {deepseek_key[:8] if deepseek_key else 'None'}...")
        
        return deepseek_key is not None
    except Exception as e:
        print(f"❌ Main config failed: {e}")
        return False

def test_docker_config():
    """Test the docker config"""
    print("\n=== Testing Docker Config ===")
    
    # Add docker directory to path
    docker_path = Path(__file__).parent / "deploy" / "docker"
    sys.path.insert(0, str(docker_path))
    
    try:
        from utils import load_config
        config = load_config()
        print(f"✅ Docker config loaded successfully")
        
        # Check LLM configuration
        llm_config = config.get("llm", {})
        provider = llm_config.get("provider")
        api_key_env = llm_config.get("api_key_env")
        
        print(f"LLM provider: {provider}")
        print(f"API key env var: {api_key_env}")
        
        # Check if environment variable is available
        api_key = os.getenv(api_key_env) if api_key_env else None
        print(f"Environment variable '{api_key_env}' loaded: {bool(api_key)}")
        print(f"API key length: {len(api_key) if api_key else 0}")
        print(f"API key preview: {api_key[:8] if api_key else 'None'}...")
        
        return api_key is not None
    except Exception as e:
        print(f"❌ Docker config failed: {e}")
        return False

def test_direct_env_loading():
    """Test direct environment file loading"""
    print("\n=== Testing Direct Environment Loading ===")
    
    from dotenv import load_dotenv
    
    # Test loading from root
    env_file = Path(__file__).parent / ".llm.env"
    print(f"Checking .llm.env at: {env_file}")
    print(f"File exists: {env_file.exists()}")
    
    if env_file.exists():
        load_dotenv(env_file)
        deepseek_key = os.getenv('DEEPSEEK_API_KEY')
        groq_key = os.getenv('GROQ_API_KEY')
        
        print(f"✅ Environment file loaded")
        print(f"DEEPSEEK_API_KEY loaded: {bool(deepseek_key)}")
        print(f"DEEPSEEK_API_KEY length: {len(deepseek_key) if deepseek_key else 0}")
        print(f"GROQ_API_KEY loaded: {bool(groq_key)}")
        
        return deepseek_key is not None
    else:
        print(f"❌ Environment file not found")
        return False

def test_crawl4ai_import():
    """Test importing crawl4ai and LLM components"""
    print("\n=== Testing Crawl4AI Import ===")
    
    try:
        from crawl4ai import AsyncWebCrawler, LLMExtractionStrategy, LLMConfig
        print("✅ Crawl4AI imports successful")
        
        # Try to create LLM config
        llm_config = LLMConfig(
            provider="deepseek/deepseek-chat",
            api_token=os.getenv("DEEPSEEK_API_KEY", "")
        )
        print(f"✅ LLMConfig created successfully")
        print(f"Provider: {llm_config.provider}")
        print(f"API token set: {bool(llm_config.api_token)}")
        
        return True
    except Exception as e:
        print(f"❌ Crawl4AI import failed: {e}")
        return False

def main():
    print("🔍 Comprehensive Crawl4AI LLM Connection Test\n")
    
    results = []
    
    # Test 1: Direct environment loading
    results.append(test_direct_env_loading())
    
    # Test 2: Main crawl4ai config
    results.append(test_main_crawl4ai_config())
    
    # Test 3: Docker config
    results.append(test_docker_config())
    
    # Test 4: Crawl4AI imports
    results.append(test_crawl4ai_import())
    
    # Summary
    print("\n" + "="*50)
    print("📊 TEST RESULTS SUMMARY")
    print("="*50)
    
    tests = [
        "Direct Environment Loading",
        "Main Crawl4AI Config", 
        "Docker Config",
        "Crawl4AI Import"
    ]
    
    for i, (test_name, result) in enumerate(zip(tests, results)):
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{i+1}. {test_name}: {status}")
    
    all_passed = all(results)
    print(f"\n🎯 Overall Status: {'✅ ALL TESTS PASSED' if all_passed else '❌ SOME TESTS FAILED'}")
    
    if all_passed:
        print("🚀 Your Crawl4AI setup should work fine with LLM connections!")
    else:
        print("⚠️  There are issues that need to be fixed before LLM connections will work properly.")

if __name__ == "__main__":
    main()
