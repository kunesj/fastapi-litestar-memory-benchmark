# FastAPI vs Litestar memory benchmark

This is a very basic comparison of how much memory is consumed at standby by FastAPI vs Litestar.

Test data: 100x (7 models, 81 fields, 8 endpoints)


### FastAPI

```
python 3.11 
fastapi 0.115.12
pydantic 2.11.4
```

| Step                           | Memory (MB) |
|--------------------------------|-------------|
| Python interpreter             | 12.750      |
| `from fastapi import FastAPI`  | 42.304      |
| `from .routers import ROUTERS` | 95.054      |
| `app = FastAPI(...)`           | 115.679     |
 

### Litestar

```
python 3.11
litestar 2.16.0
msgspec 0.19.0
```

| Step                           | Memory (MB) |
|--------------------------------|-------------|
| Python interpreter             | 12.625      |
| `import litestar`              | 33.929      |
| `from .routers import ROUTERS` | 39.429      |
| `app = Litestar(...)`          | 57.4296     |
