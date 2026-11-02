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
Completed responses are also saved as UTF-8 Markdown in `./data/`, using
`YYYY-MM-DD-{slot}.md`, where `slot` is a filename-safe version of the prompt.
Repeated requests receive a numbered suffix to preserve previous results.
The local Ollama agent saves responses using the same convention.
The `web_search` tool fetches https://data.10jqka.com.cn/market/longhu/
and extracts the 个股明细 market summaries for 深市、沪市, excluding
京市、科创板, names containing `*ST`, and negative gains. Results use percentage strings, for example
`[{"stock_name": "冰山冷热", "stock_up": "10.03%"}]`. Zero gains are retained.
The source shows its latest published trading data; this is not a general web search.

The agent also connects to Notion's hosted MCP server at
`https://mcp.notion.com/mcp`. On startup, a browser opens for OAuth authorization.
Authorize access to your Notion workspace to enable its search and editing tools.
OAuth credentials persist across restarts in the git-ignored `.notion-oauth/`
directory, encrypted with a locally generated key. Keep this directory private
and do not share it. Delete it to clear the saved login and authorize again. Model settings are still loaded from `.env`.

```sh
uv run python-ai-agent "Search Notion for my stock research notes and summarize them"
```

Notion tools run asynchronously alongside the existing stock tool. Completed
responses continue to be saved locally; ask explicitly to save a report in Notion.
