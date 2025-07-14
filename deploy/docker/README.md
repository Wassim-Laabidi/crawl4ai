# Crawl4AI LLM Provider Integration Update

This update enables **Crawl4AI to successfully manage alternative LLM API keys** beyond DeepSeek, allowing flexible usage of different LLM providers such as OpenAI, Ollama, or others supported by your setup.

---

## Changes Made

To implement this, the following files were modified:

- **`crawl4ai/utils.py`**  
  Added logic to handle API keys and requests for other LLM providers.

- **`crawl4ai/config.py`**  
  Updated configuration options to support new LLM provider parameters.

- **`deploy/docker/configuration.yml`**  
  Adjusted environment variables to inject new LLM provider API keys into the container environment.

- **`.llm.env`**  
  Added environment variables for the new LLM provider API keys to be used at runtime.

---

## Deployment Example

Run the Docker container with your updated image and environment file:

```bash
docker run -d -p 11235:11235 --name crawl4ai --env-file .llm.env --shm-size=1g wassimlaabidi/crawl4ai:deepseek-chat

Make sure .llm.env contains your desired LLM API key(s), for example:

LLM_PROVIDER=openai/gpt-4o
OPENAI_API_KEY=your_openai_api_key_here
