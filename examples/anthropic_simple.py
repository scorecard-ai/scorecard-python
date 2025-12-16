"""Simple example of wrapping Anthropic SDK with Scorecard tracing."""

import os

from anthropic import Anthropic

from scorecard_ai import wrap

# Wrap the Anthropic client
claude = wrap(
    Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY")),
)


def main() -> None:
    """Run a simple Anthropic completion with automatic tracing."""
    response = claude.messages.create(
        model="claude-3-5-haiku-20241022",
        max_tokens=500,
        messages=[{"role": "user", "content": "What is the capital of France?"}],
    )

    text_content = next((block for block in response.content if block.type == "text"), None)
    print("Response:", text_content.text if text_content else "No response")


if __name__ == "__main__":
    main()
