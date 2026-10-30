# Stock Analyzer AI Agent

Copy `.env.example` to `.env` and set the required `AI_MODEL_BASE_URL`,
`AI_MODEL_API_KEY`, and `AI_MODEL_NAME` for your OpenAI-compatible provider.
The example model is `qwen3.8-flash`; your provider must support the selected
model and tool calling. Missing or blank settings produce a configuration error.

```sh
uv sync
uv run python-ai-agent "Analyze AAPL's business and key risks"
```

Without an argument, the agent asks for a request interactively.
The response streams to the terminal as the model generates text.
The `web_search` tool is registered as a placeholder; it retrieves no data
until a search provider is implemented.
