# Scorecard Python SDK Examples

## LLM SDK Wrappers

Simple wrappers for OpenAI and Anthropic SDKs that automatically send traces to Scorecard.

### Installation

```bash
pip install scorecard-ai openai anthropic
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
        "api_key": os.getenv("SCORECARD_API_KEY"),
        "project_id": "987"
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
        "api_key": os.getenv("SCORECARD_API_KEY"),
        "project_id": "987"
    }
)

# Use normally - traces are automatically sent to Scorecard
response = claude.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=500,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

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

See `basic_nesting.py` and `nested_traces.py` for complete examples.

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

# Run examples
python openai_simple.py
python anthropic_simple.py
python basic_nesting.py
python nested_traces.py
```

### What Gets Traced

The wrappers automatically capture:
- Request model, temperature, max_tokens, top_p
- Prompt messages
- Response model, finish reason, tokens used
- Completion text
- Errors and exceptions

All traces include GenAI semantic conventions compatible with the Scorecard backend.
