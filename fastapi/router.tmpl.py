from __future__ import annotations

import datetime
from typing import Annotated, Any, Literal

from fastapi import APIRouter, Query, Path, Body, Response
from pydantic import BaseModel, Field

router = APIRouter(prefix="/modelXYZ")


class ModelCreateDataXYZ(BaseModel):
    foo1: bool = Field()
    foo2: bool = Field()
    foo3: bool = Field()
    foo4: bool = Field()

    foo5: str | None = Field()
    foo6: str | None = Field()
    foo7: str | None = Field()
    foo8: str | None = Field()

    foo9: list[str] = Field()
    foo10: list[str] = Field()
    foo11: list[str] = Field()
    foo12: list[str] = Field()

    foo13: datetime.date | None = Field()
    foo14: datetime.date | None = Field()
    foo15: datetime.datetime | None = Field()
    foo16: datetime.datetime | None = Field()

    foo17: ModelReadDataXYZ = Field()
    foo18: ModelReadDataXYZ = Field()
    foo19: ModelReadDataXYZ = Field()
    foo20: ModelReadDataXYZ = Field()

    foo21: list[ModelReadDataXYZ] = Field()
    foo22: list[ModelReadDataXYZ] = Field()
    foo23: list[ModelReadDataXYZ] = Field()
    foo24: list[ModelReadDataXYZ] = Field()


class ModelReadDataXYZ(BaseModel):
    foo1: bool = Field()
    foo2: bool = Field()
    foo3: bool = Field()
    foo4: bool = Field()

    foo5: str | None = Field()
    foo6: str | None = Field()
    foo7: str | None = Field()
    foo8: str | None = Field()

    foo9: list[str] = Field()
    foo10: list[str] = Field()
    foo11: list[str] = Field()
    foo12: list[str] = Field()

    foo13: datetime.date | None = Field()
    foo14: datetime.date | None = Field()
    foo15: datetime.datetime | None = Field()
    foo16: datetime.datetime | None = Field()

    foo17: ModelReadDataXYZ = Field()
    foo18: ModelReadDataXYZ = Field()
    foo19: ModelReadDataXYZ = Field()
    foo20: ModelReadDataXYZ = Field()

    foo21: list[ModelReadDataXYZ] = Field()
    foo22: list[ModelReadDataXYZ] = Field()
    foo23: list[ModelReadDataXYZ] = Field()
    foo24: list[ModelReadDataXYZ] = Field()


class ModelUpdateDataXYZ(BaseModel):
    foo1: bool = Field()
    foo2: bool = Field()
    foo3: bool = Field()
    foo4: bool = Field()

    foo5: str | None = Field()
    foo6: str | None = Field()
    foo7: str | None = Field()
    foo8: str | None = Field()

    foo9: list[str] = Field()
    foo10: list[str] = Field()
    foo11: list[str] = Field()
    foo12: list[str] = Field()

    foo13: datetime.date | None = Field()
    foo14: datetime.date | None = Field()
    foo15: datetime.datetime | None = Field()
    foo16: datetime.datetime | None = Field()

    foo17: ModelReadDataXYZ = Field()
    foo18: ModelReadDataXYZ = Field()
    foo19: ModelReadDataXYZ = Field()
    foo20: ModelReadDataXYZ = Field()

    foo21: list[ModelReadDataXYZ] = Field()
    foo22: list[ModelReadDataXYZ] = Field()
    foo23: list[ModelReadDataXYZ] = Field()
    foo24: list[ModelReadDataXYZ] = Field()


class ModelSearchResponseXYZ(BaseModel):
    results: list[ModelReadDataXYZ] = Field()
    total: int = Field()
    limit: int = Field()


class ModelRequest1_XYZ(BaseModel):
    content: str = Field()
    count: int = Field(examples=[123])
    users: list[ModelReadDataXYZ] = Field()


class ModelRequest2_XYZ(BaseModel):
    foo: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] = Field()


class ModelRequest3_XYZ(BaseModel):
    domain: list[Literal["&", "|", "!"] | tuple[str, Literal["=", "!=", "<", "<=", ">", ">="], Any]] = Field()
    order: list[tuple[str, int]] = Field()


@router.get("/")
async def model_search(
    domain: Annotated[str, Query()],
    order: Annotated[str, Query()] = "asc",
    offset: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=0, le=100)] = 50,
    fields: Annotated[str | None, Query()] = None,
) -> ModelSearchResponseXYZ:
    ...


@router.post("/")
async def model_create(
    data: Annotated[ModelCreateDataXYZ, Body()],
    fields: Annotated[str | None, Query()] = None,
) -> ModelSearchResponseXYZ:
    ...


@router.get("/{record_id}")
async def record_read(
    record_id: Annotated[str, Path()],
    fields: Annotated[str | None, Query()] = None,
) -> ModelReadDataXYZ:
    ...


@router.patch("/{record_id}")
async def record_update(
    record_id: Annotated[str, Path()],
    data: Annotated[ModelUpdateDataXYZ, Body()],
    fields: Annotated[str | None, Query()] = None,
) -> ModelReadDataXYZ:
    ...


@router.delete("/{record_id}")
async def record_delete(
    record_id: Annotated[str, Path()],
) -> Response:
    ...


@router.post("/{record_id}/req1")
async def record_request1(
    record_id: Annotated[str, Path()],
    data: Annotated[ModelRequest1_XYZ, Body()],
) -> Response:
    ...


@router.post("/{record_id}/req2")
async def record_request2(
    record_id: Annotated[str, Path()],
    data: Annotated[ModelRequest2_XYZ, Body()],
) -> Response:
    ...


@router.post("/{record_id}/req3")
async def record_request3(
    record_id: Annotated[str, Path()],
    data: Annotated[ModelRequest3_XYZ, Body()],
) -> Response:
    ...
