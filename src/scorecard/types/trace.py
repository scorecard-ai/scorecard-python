# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Trace", "Span"]


class Span(BaseModel):
    children: List[object] = FieldInfo(alias="Children")

    duration: int = FieldInfo(alias="Duration")

    events_attributes: List[Dict[str, str]] = FieldInfo(alias="Events.Attributes")

    events_name: List[str] = FieldInfo(alias="Events.Name")

    events_timestamp: List[datetime] = FieldInfo(alias="Events.Timestamp")

    links_attributes: List[Dict[str, str]] = FieldInfo(alias="Links.Attributes")

    links_span_id: List[str] = FieldInfo(alias="Links.SpanId")

    links_trace_id: List[str] = FieldInfo(alias="Links.TraceId")

    links_trace_state: List[str] = FieldInfo(alias="Links.TraceState")

    parent_span_id: str = FieldInfo(alias="ParentSpanId")

    resource_attributes: Dict[str, str] = FieldInfo(alias="ResourceAttributes")

    scope_name: str = FieldInfo(alias="ScopeName")

    scope_version: str = FieldInfo(alias="ScopeVersion")

    service_name: str = FieldInfo(alias="ServiceName")

    span_attributes: Dict[str, str] = FieldInfo(alias="SpanAttributes")

    span_id: str = FieldInfo(alias="SpanId")

    span_kind: str = FieldInfo(alias="SpanKind")

    span_name: str = FieldInfo(alias="SpanName")

    status_code: str = FieldInfo(alias="StatusCode")

    status_message: str = FieldInfo(alias="StatusMessage")

    timestamp: datetime = FieldInfo(alias="Timestamp")

    trace_id: str = FieldInfo(alias="TraceId")

    trace_state: str = FieldInfo(alias="TraceState")


class Trace(BaseModel):
    end: datetime = FieldInfo(alias="End")

    start: datetime = FieldInfo(alias="Start")

    trace_id: str = FieldInfo(alias="TraceId")

    spans: Optional[List[Span]] = FieldInfo(alias="Spans", default=None)
