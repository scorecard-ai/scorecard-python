# This file was auto-generated by Fern from our API Definition.

import typing

RunStatus = typing.Union[
    typing.Literal[
        "pending",
        "awaiting_execution",
        "running_execution",
        "awaiting_scoring",
        "running_scoring",
        "awaiting_human_scoring",
        "completed",
    ],
    typing.Any,
]
