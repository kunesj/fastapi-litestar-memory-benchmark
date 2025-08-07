from __future__ import annotations

import datetime
from typing import Annotated, Any, Literal

import litestar
from litestar.params import Body, Parameter
import msgspec


class ModelCreateDataXYZ(msgspec.Struct, kw_only=True):
    foo1: bool = msgspec.field()
    foo2: bool = msgspec.field()
    foo3: bool = msgspec.field()
    foo4: bool = msgspec.field()

    foo5: str | None = msgspec.field()
    foo6: str | None = msgspec.field()
    foo7: str | None = msgspec.field()
    foo8: str | None = msgspec.field()

    foo9: list[str] = msgspec.field()
    foo10: list[str] = msgspec.field()
    foo11: list[str] = msgspec.field()
    foo12: list[str] = msgspec.field()

    foo13: datetime.date | None = msgspec.field()
    foo14: datetime.date | None = msgspec.field()
    foo15: datetime.datetime | None = msgspec.field()
    foo16: datetime.datetime | None = msgspec.field()

    foo17: ModelReadDataXYZ = msgspec.field()
    foo18: ModelReadDataXYZ = msgspec.field()
    foo19: ModelReadDataXYZ = msgspec.field()
    foo20: ModelReadDataXYZ = msgspec.field()

    foo21: list[ModelReadDataXYZ] = msgspec.field()
    foo22: list[ModelReadDataXYZ] = msgspec.field()
    foo23: list[ModelReadDataXYZ] = msgspec.field()
    foo24: list[ModelReadDataXYZ] = msgspec.field()


class ModelReadDataXYZ(msgspec.Struct, kw_only=True):
    foo1: bool = msgspec.field()
    foo2: bool = msgspec.field()
    foo3: bool = msgspec.field()
    foo4: bool = msgspec.field()

    foo5: str | None = msgspec.field()
    foo6: str | None = msgspec.field()
    foo7: str | None = msgspec.field()
    foo8: str | None = msgspec.field()

    foo9: list[str] = msgspec.field()
    foo10: list[str] = msgspec.field()
    foo11: list[str] = msgspec.field()
    foo12: list[str] = msgspec.field()

    foo13: datetime.date | None = msgspec.field()
    foo14: datetime.date | None = msgspec.field()
    foo15: datetime.datetime | None = msgspec.field()
    foo16: datetime.datetime | None = msgspec.field()

    foo17: ModelReadDataXYZ = msgspec.field()
    foo18: ModelReadDataXYZ = msgspec.field()
    foo19: ModelReadDataXYZ = msgspec.field()
    foo20: ModelReadDataXYZ = msgspec.field()

    foo21: list[ModelReadDataXYZ] = msgspec.field()
    foo22: list[ModelReadDataXYZ] = msgspec.field()
    foo23: list[ModelReadDataXYZ] = msgspec.field()
    foo24: list[ModelReadDataXYZ] = msgspec.field()


class ModelUpdateDataXYZ(msgspec.Struct, kw_only=True):
    foo1: bool = msgspec.field()
    foo2: bool = msgspec.field()
    foo3: bool = msgspec.field()
    foo4: bool = msgspec.field()

    foo5: str | None = msgspec.field()
    foo6: str | None = msgspec.field()
    foo7: str | None = msgspec.field()
    foo8: str | None = msgspec.field()

    foo9: list[str] = msgspec.field()
    foo10: list[str] = msgspec.field()
    foo11: list[str] = msgspec.field()
    foo12: list[str] = msgspec.field()

    foo13: datetime.date | None = msgspec.field()
    foo14: datetime.date | None = msgspec.field()
    foo15: datetime.datetime | None = msgspec.field()
    foo16: datetime.datetime | None = msgspec.field()

    foo17: ModelReadDataXYZ = msgspec.field()
    foo18: ModelReadDataXYZ = msgspec.field()
    foo19: ModelReadDataXYZ = msgspec.field()
    foo20: ModelReadDataXYZ = msgspec.field()

    foo21: list[ModelReadDataXYZ] = msgspec.field()
    foo22: list[ModelReadDataXYZ] = msgspec.field()
    foo23: list[ModelReadDataXYZ] = msgspec.field()
    foo24: list[ModelReadDataXYZ] = msgspec.field()


class ModelSearchResponseXYZ(msgspec.Struct, kw_only=True):
    results: list[ModelReadDataXYZ] = msgspec.field()
    total: int = msgspec.field()
    limit: int = msgspec.field()


class ModelRequest1_XYZ(msgspec.Struct, kw_only=True):
    content: str = msgspec.field()
    count: int = msgspec.field()
    users: list[ModelReadDataXYZ] = msgspec.field()


class ModelRequest2_XYZ(msgspec.Struct, kw_only=True):
    foo: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] = msgspec.field()


class ModelRequest3_XYZ(msgspec.Struct, kw_only=True):
    domain: list[Literal["&", "|", "!"] | tuple[str, Literal["=", "!=", "<", "<=", ">", ">="], Any]] = msgspec.field()
    order: list[tuple[str, int]] = msgspec.field()


class ModelControllerXYZ(litestar.Controller):
    path = "/modelXYZ"

    @litestar.get("/")
    async def model_search(
        self,
        *,
        domain: Annotated[str, Parameter()],
        order: Annotated[str, Parameter()] = "asc",
        offset: Annotated[int, Parameter(ge=0)] = 0,
        limit: Annotated[int, Parameter(ge=0, le=100)] = 50,
        fields: Annotated[str | None, Parameter()] = None,
    ) -> ModelSearchResponseXYZ:
        ...

    @litestar.post("/")
    async def model_create(
        self,
        data: Annotated[ModelCreateDataXYZ, Body()],
        *,
        fields: Annotated[str | None, Parameter()] = None,
    ) -> ModelSearchResponseXYZ:
        ...

    @litestar.get("/{record_id:str}")
    async def record_read(
        self,
        record_id: Annotated[str, Parameter()],
        *,
        fields: Annotated[str | None, Parameter()] = None,
    ) -> ModelReadDataXYZ:
        ...

    @litestar.patch("/{record_id:str}")
    async def record_update(
        self,
        record_id: Annotated[str, Parameter()],
        data: Annotated[ModelUpdateDataXYZ, Body()],
        *,
        fields: Annotated[str | None, Parameter()] = None,
    ) -> ModelReadDataXYZ:
        ...

    @litestar.delete("/{record_id:str}", status_code=200)
    async def record_delete(
        self,
        record_id: Annotated[str, Parameter()],
    ) -> dict[str, Any]:
        ...

    @litestar.post("/{record_id:str}/req1")
    async def record_request1(
        self,
        record_id: Annotated[str, Parameter()],
        data: Annotated[ModelRequest1_XYZ, Body()],
    ) -> dict[str, Any]:
        ...

    @litestar.post("/{record_id:str}/req2")
    async def record_request2(
        self,
        record_id: Annotated[str, Parameter()],
        data: Annotated[ModelRequest2_XYZ, Body()],
    ) -> dict[str, Any]:
        ...

    @litestar.post("/{record_id:str}/req3")
    async def record_request3(
        self,
        record_id: Annotated[str, Parameter()],
        data: Annotated[ModelRequest3_XYZ, Body()],
    ) -> dict[str, Any]:
        ...
