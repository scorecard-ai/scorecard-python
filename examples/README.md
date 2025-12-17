# Scorecard Python SDK Examples

## LLM SDK Wrappers

Simple wrappers for OpenAI and Anthropic SDKs that automatically send traces to Scorecard.

### Installation

```bash
pip install -r requirements.txt
```

Or install packages individually:

```bash
pip install scorecard-ai[otel] openai anthropic
```

### Usage

#### OpenAI

```python
from scorecard_ai import wrap
from openai import OpenAI
import os

openai = wrap(
    OpenAI(api_key=os.getenv("OPENAI_API_KEY")),
    {
        # Scorecard configuration
        "api_key": os.getenv("SCORECARD_API_KEY"),
        "project_id": os.getenv("SCORECARD_PROJECT_ID")
    }
)

# Use normally - traces are automatically sent to Scorecard
response = openai.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

#### Anthropic (Claude)

```python
from scorecard_ai import wrap
from anthropic import Anthropic
import os

claude = wrap(
    Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY")),
    {
        # Scorecard configuration
        "api_key": os.getenv("SCORECARD_API_KEY"),
        "project_id": os.getenv("SCORECARD_PROJECT_ID")
    }
)

# Use normally - traces are automatically sent to Scorecard
response = claude.messages.create(
    model="claude-3-5-haiku-20241022",
    max_tokens=500,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Streaming Support

The wrapper fully supports streaming responses from both OpenAI and Anthropic:

```python
# OpenAI streaming
stream = openai.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True,
    stream_options={"include_usage": True}  # Include token usage in stream
)

for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

```python
# Anthropic streaming with context manager
with claude.messages.stream(
    model="claude-3-5-sonnet-20241022",
    messages=[{"role": "user", "content": "Tell me a story"}],
    max_tokens=200
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

The wrapper accumulates metadata (tokens, finish reason, content) as the stream is consumed and automatically closes the trace when the stream completes.

See [`openai_streaming.py`](./openai_streaming.py) and [`anthropic_streaming.py`](./anthropic_streaming.py) for complete examples.

### Nested Traces

The wrapper automatically respects OpenTelemetry context, so LLM calls will be nested as children of any active spans:

```python
from opentelemetry import trace

tracer = trace.get_tracer("my-app")

# Create a parent span
with tracer.start_as_current_span("my-workflow") as span:
    # This LLM call will be a child of 'my-workflow'
    response = openai.chat.completions.create(...)
```

See [`nested_simple.py`](./nested_simple.py) and [`nested_advanced.py`](./nested_advanced.py) for complete examples.

### Configuration

Both wrappers accept the same config:

| Option | Description | Default |
|--------|-------------|---------|
| `api_key` | Scorecard API key | `SCORECARD_API_KEY` env var |
| `project_id` | Project ID to associate traces with | `SCORECARD_PROJECT_ID` env var |
| `service_name` | Service name for telemetry | `"llm-app"` |
| `endpoint` | OTLP endpoint for traces | `"https://tracing.scorecard.io/otel/v1/traces"` |

### Running Examples

```bash
# Set environment variables
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export SCORECARD_API_KEY="ak_..."
export SCORECARD_PROJECT_ID="123"

# Run examples
python openai_simple.py
python anthropic_simple.py
python openai_streaming.py
python anthropic_streaming.py
python nested_simple.py
python nested_advanced.py
```

### What Gets Traced

The wrappers automatically capture:
- Request model, temperature, max_tokens, top_p
- Prompt messages
- Response model, finish reason, tokens used
- Completion text
- Errors and exceptions
- Streaming responses (accumulated as stream is consumed)

All traces include GenAI semantic conventions compatible with the Scorecard backend.
