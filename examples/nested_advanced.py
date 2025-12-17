"""Example of nested traces with wrapped LLM clients."""

from __future__ import annotations

import os

from openai import OpenAI
from anthropic import Anthropic
from opentelemetry import trace

from scorecard_ai import wrap

# Wrap the clients
openai = wrap(
    OpenAI(api_key=os.getenv("OPENAI_API_KEY")),
)

claude = wrap(
    Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY")),
)


def analyze_with_multiple_llms(user_query: str) -> dict[str, str]:
    """Complex workflow with nested traces using multiple LLMs."""
    tracer = trace.get_tracer("my-app")

    # Parent span for the entire workflow
    with tracer.start_as_current_span("analyze-query-workflow") as workflow_span:
        print("Starting analysis workflow...")

        # First LLM call (will be nested under workflow span)
        with tracer.start_as_current_span("get-gpt-analysis") as gpt_span:
            gpt_span.set_attribute("llm.provider", "openai")

            gpt_response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Analyze this query and provide initial thoughts."},
                    {"role": "user", "content": user_query},
                ],
                max_tokens=200,
            )

            gpt_analysis = ""
            if gpt_response.choices and gpt_response.choices[0].message:
                gpt_analysis = gpt_response.choices[0].message.content or ""

        print(f"GPT Analysis: {gpt_analysis}")

        # Second LLM call (will also be nested under workflow span)
        with tracer.start_as_current_span("get-claude-analysis") as claude_span:
            claude_span.set_attribute("llm.provider", "anthropic")

            claude_response = claude.messages.create(
                model="claude-3-5-haiku-20241022",
                max_tokens=200,
                messages=[
                    {
                        "role": "user",
                        "content": f'Here\'s an analysis from another model: "{gpt_analysis}"\n\nNow provide your own analysis of: {user_query}',
                    }
                ],
            )

            text_content = next((block for block in claude_response.content if block.type == "text"), None)
            claude_analysis = text_content.text if text_content else ""

        print(f"Claude Analysis: {claude_analysis}")

        # Final synthesis
        workflow_span.set_attribute("workflow.status", "completed")

        return {
            "gpt_analysis": gpt_analysis,
            "claude_analysis": claude_analysis,
        }


def main() -> None:
    """Run the nested trace example."""
    result = analyze_with_multiple_llms("What are the key differences between Python and JavaScript?")

    print("\nFinal Result:", result)
    print("\n✅ Check your Scorecard dashboard to see the nested trace tree!")


if __name__ == "__main__":
    main()
