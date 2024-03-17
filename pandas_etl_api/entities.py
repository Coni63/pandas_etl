from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import Field


class _Connector(BaseModel):
    node: str
    output: str | None = None
    input: str | None = None


class _Connection(BaseModel):
    connections: list[_Connector]


class _ActionData(BaseModel):
    description: dict[str, Any]


class SingleAction(BaseModel):
    id: int
    name: str
    data: _ActionData
    inputs: dict[str, _Connection]
    outputs: dict[str, _Connection]


class Workflow(BaseModel):
    data: dict[str, SingleAction]


class ActionState(BaseModel):
    key: str
    name: str
    inputs: int
    outputs: int
    allow_multiple_input: bool
    classname: str
    icon: tuple[str, str]


class AllActionsState(BaseModel):
    extractors: list[ActionState] = Field(default_factory=list)
    transformers: list[ActionState] = Field(default_factory=list)
    loaders: list[ActionState] = Field(default_factory=list)
