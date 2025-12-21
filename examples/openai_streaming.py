"""Example of streaming responses with OpenAI SDK and Scorecard tracing."""

import os

from openai import OpenAI

from scorecard_ai import wrap

# Wrap the OpenAI client
openai = wrap(
    OpenAI(api_key=os.getenv("OPENAI_API_KEY")),
)


def main() -> None:
    """Stream an OpenAI completion with automatic tracing."""
    print("Streaming response from OpenAI...\n")

    # Note: stream_options={"include_usage": True} enables usage tracking in streams
    stream = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Write a short poem about Python programming."},
        ],
        temperature=0.7,
        max_tokens=200,
        stream=True,
        stream_options={"include_usage": True},
    )

    # Consume the stream
    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)

    print("\n\nStream complete! Check your Scorecard dashboard for traces.")


if __name__ == "__main__":
    main()
