# FastAPI vs Litestar memory benchmark

This is a very basic comparison of how much memory is consumed at standby by FastAPI vs Litestar.


### FastAPI

```
python 3.11 
fastapi 0.115.12
pydantic 2.11.4
```

- Test data: no routes or models

| Step                           | Memory (MB)      |
|--------------------------------|------------------|
| Python interpreter             | 12.25            |
| `from fastapi import FastAPI`  | 42.183 (+29.933) |
| `from .routers import ROUTERS` | 42.308 (+0.125)  |
| `app = FastAPI(...)`           | 42.308 (+0)      |

- Test data: 100x (7 models, 81 fields, 8 endpoints)

| Step                           | Memory (MB)       |
|--------------------------------|-------------------|
| Python interpreter             | 12.75             |
| `from fastapi import FastAPI`  | 42.304 (+29.554)  |
| `from .routers import ROUTERS` | 95.054 (+52.750)  |
| `app = FastAPI(...)`           | 115.679 (+20.625) |
 

### Litestar

```
python 3.11
litestar 2.16.0
msgspec 0.19.0
```

- Test data: no routes or models

| Step                           | Memory (MB)      |
|--------------------------------|------------------|
| Python interpreter             | 12.25            |
| `import litestar`              | 33.878 (+21.628) |
| `from .routers import ROUTERS` | 33.878 (+0)      |
| `app = Litestar(...)`          | 35.128 (+1.25)   |

- Test data: 100x (7 models, 81 fields, 8 endpoints)

| Step                           | Memory (MB)      |
|--------------------------------|------------------|
| Python interpreter             | 12.625           |
| `import litestar`              | 33.929 (+21.304) |
| `from .routers import ROUTERS` | 39.429 (+5.5)    |
| `app = Litestar(...)`          | 57.429 (+18)     |


### TLDR

- FastAPI library is a bit larger (29.55 MB vs 21.3 MB)
- **FastAPI uses roughly 10x more memory** for the same routes and models (52.75 MB vs 5.5 MB)
- Creation of the FastAPI app object consumes a slightly more memory (20.625 MB vs 18 MB)
