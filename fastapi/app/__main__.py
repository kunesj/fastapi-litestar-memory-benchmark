# -*- coding: utf-8 -*-

from __future__ import annotations

import psutil


def print_memory_mb(label: str) -> None:
    print(label, psutil.Process().memory_info().rss / 2**20)


def main():
    print_memory_mb("start")

    from fastapi import FastAPI
    print_memory_mb("import FastAPI")

    from .routers import ROUTERS
    print_memory_mb("import routers")

    main.app = FastAPI()
    for router in ROUTERS:
        main.app.include_router(router)
    print_memory_mb("build app")


if __name__ == "__main__":
    main()
