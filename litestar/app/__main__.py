# -*- coding: utf-8 -*-

from __future__ import annotations

import psutil


def print_memory_mb(label: str) -> None:
    print(label, psutil.Process().memory_info().rss / 2**20)


def main():
    print_memory_mb("start")

    import litestar
    print_memory_mb("import litestar")

    from .routers import ROUTERS
    print_memory_mb("import routers")

    main.app = litestar.Litestar(route_handlers=ROUTERS)
    print_memory_mb("build app")


if __name__ == "__main__":
    main()
