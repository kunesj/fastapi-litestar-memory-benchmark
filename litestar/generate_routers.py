import pathlib
import shutil


ROOT_PATH = pathlib.Path(__file__).parent


def generate_routers(count: int) -> None:
    routers_path = ROOT_PATH / "app" / "routers"
    router_tmpl = (ROOT_PATH / "router.tmpl.py").read_text()
    router_placeholder = "XYZ"

    # purge old code

    if routers_path.exists():
        shutil.rmtree(routers_path)

    # generate new code

    routers_path.mkdir()
    init_lines = []
    router_variables = []

    for i in range(count):
        (routers_path / f"router_{i}.py").write_text(
            router_tmpl.replace(router_placeholder, str(i))
        )
        init_lines.append(f"from .router_{i} import ModelController{i} as _router_{i}")
        router_variables.append(f"_router_{i}")

    init_lines.append(f"ROUTERS = [{', '.join(router_variables)}]")
    (routers_path / "__init__.py").write_text("\n".join(init_lines))


if __name__ == "__main__":
    generate_routers(count=100)
