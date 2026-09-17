import asyncio
import os
import sys

from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from dotenv import load_dotenv
from openai import AsyncOpenAI, DefaultAsyncHttpx2Client


load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434/v1")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3.5:0.8b-mlx")


async def run_agent(prompt: str) -> str:
    """Run a single prompt through an OpenAI Agents SDK agent backed by Ollama."""
    set_tracing_disabled(True)

    async with AsyncOpenAI(
        base_url=OLLAMA_BASE_URL,
        api_key="ollama",  # Ollama ignores the value, but the client requires one.
        # This is a localhost-only client; do not route it through system proxies.
        http_client=DefaultAsyncHttpx2Client(trust_env=False),
    ) as client:
        model = OpenAIChatCompletionsModel(
            model=OLLAMA_MODEL,
            openai_client=client,
        )
        agent = Agent(
            name="Ollama Assistant",
            instructions="You are a helpful assistant. Answer clearly and concisely.",
            model=model,
        )
        result = await Runner.run(agent, prompt)

    return str(result.final_output)


def main() -> None:
    prompt = " ".join(sys.argv[1:]).strip()
    if not prompt:
        prompt = input("Ask the agent: ").strip()
    if not prompt:
        raise SystemExit("A prompt is required.")

    print(asyncio.run(run_agent(prompt)))


if __name__ == "__main__":
    main()
