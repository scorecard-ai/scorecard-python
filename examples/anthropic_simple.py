"""Simple example of wrapping Anthropic SDK with Scorecard tracing."""

import os
from scorecard_ai import wrap
from anthropic import Anthropic

# Wrap the Anthropic client
claude = wrap(
    Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY")),
    {
        "api_key": os.getenv("SCORECARD_API_KEY"),
        "project_id": "987",
    },
)


def main():
    """Run a simple Anthropic completion with automatic tracing."""
    response = claude.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=500,
        messages=[{"role": "user", "content": "What is the capital of France?"}],
    )

    text_content = next((block for block in response.content if block.type == "text"), None)
    print("Response:", text_content.text if text_content else "No response")


if __name__ == "__main__":
    main()
