# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Whoami", "Membership", "Org"]


class Membership(BaseModel):
    id: str
    """The ID of the organization."""

    name: str
    """The name of the organization."""

    role: Optional[str] = None
    """The user's role in the organization, for example `org:admin`.

    Null for a JWT or an org API key, which list only their own organization.
    """


class Org(BaseModel):
    """The organization this request acts in."""

    id: str
    """The ID of the organization."""

    name: str
    """The name of the organization."""

    slug: str
    """The URL slug of the organization."""


class Whoami(BaseModel):
    """The identity and organization of the caller."""

    auth_type: Literal["jwt", "personal-api-key", "org-api-key", "oauth-key"] = FieldInfo(alias="authType")
    """
    How the request authenticated: `jwt` (Scorecard web session),
    `personal-api-key`, `org-api-key`, or `oauth-key` (OAuth token, for example from
    the MCP server).
    """

    memberships: List[Membership]
    """The organizations this credential can act in.

    Pass one of these IDs in the `X-Scorecard-Org-Id` header to switch organization.
    A JWT or an org API key lists only its own organization.
    """

    org: Org
    """The organization this request acts in."""

    org_id: str = FieldInfo(alias="orgId")
    """The ID of the organization this request acts in.

    Set it with the `X-Scorecard-Org-Id` header.
    """

    user_id: str = FieldInfo(alias="userId")
    """The ID of the user. For an org API key, the user who created the key."""
