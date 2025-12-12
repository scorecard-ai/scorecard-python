"""Simple example of wrapping OpenAI SDK with Scorecard tracing."""

import os

from openai import OpenAI  # type: ignore[import-not-found]

from scorecard_ai import wrap

# Wrap the OpenAI client
openai = wrap(
    OpenAI(api_key=os.getenv("OPENAI_API_KEY")),
)


def main() -> None:
    """Run a simple OpenAI completion with automatic tracing."""
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"},
        ],
        temperature=0.7,
        max_tokens=500,
    )

    print("Response:", response.choices[0].message.content if response.choices else "No response")


if __name__ == "__main__":
    main()
