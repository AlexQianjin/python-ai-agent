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
The `web_search` tool fetches https://data.10jqka.com.cn/market/longhu/
and extracts the 个股明细 market summaries for 深市、沪市、科创板, excluding
京市 and negative gains. Results use percentage strings, for example
`[{"stock_name": "冰山冷热", "stock_up": "10.03%"}]`. Zero gains are retained.
The source shows its latest published trading data; this is not a general web search.
