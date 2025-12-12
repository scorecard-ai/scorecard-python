"""Example of LLM call nested within a custom span."""

import os
from opentelemetry import trace
from scorecard_ai import wrap
from openai import OpenAI

# Wrap the client
openai = wrap(
    OpenAI(api_key=os.getenv("OPENAI_API_KEY")),
    {
        "api_key": os.getenv("SCORECARD_API_KEY"),
        "project_id": "987",
    },
)


def process_user_request(user_id: str, question: str) -> str:
    """Process a user request with tracing."""
    tracer = trace.get_tracer("my-app")

    with tracer.start_as_current_span("process-request") as span:
        span.set_attribute("user.id", user_id)
        span.set_attribute("question.length", len(question))

        # This LLM call will automatically be a child of the 'process-request' span
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": question}],
            max_tokens=100,
        )

        answer = response.choices[0].message.content if response.choices else ""
        span.set_attribute("answer.length", len(answer))

        return answer


def main():
    """Run the basic nesting example."""
    answer = process_user_request("user-123", "What is the capital of France?")
    print("Answer:", answer)
    print("\n✅ The OpenAI span is nested under the 'process-request' span!")


if __name__ == "__main__":
    main()
