"""Example of streaming responses with Anthropic SDK and Scorecard tracing."""

import os

from anthropic import Anthropic

from scorecard_ai import wrap

# Wrap the Anthropic client
claude = wrap(
    Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY")),
)


def main() -> None:
    """Stream an Anthropic completion with automatic tracing."""
    print("Streaming response from Claude...\n")

    # Create a streaming request
    with claude.messages.stream(
        model="claude-3-5-haiku-20241022",
        messages=[
            {"role": "user", "content": "Write a short poem about Python programming."},
        ],
        temperature=0.7,
        max_tokens=200,
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)

    print("\n\nStream complete! Check your Scorecard dashboard for traces.")


if __name__ == "__main__":
    main()
