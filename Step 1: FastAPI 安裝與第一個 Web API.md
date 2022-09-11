# Step 1: 安裝第一個 FastAPI 

## 1.1 安裝 fastAPI 相關模組

```
pip install fastapi
pip install uvicorn
```

> uvicorn 設計的初衷是想要實現一個極速的asyncio伺服器，基於ASGI(非同步伺服器閘道器介面)的最小的應用程式介面

## 1.2  用 requirement.txt 管理套件相依性

Python 常常會使用 pip 安裝很多套件(Library)，但是怎麼知道這個專案需要安裝哪些套件，讓其他機器也能一次安裝回來，就可以定義一個 requirement.txt (這只是習慣的檔名)

```
fastapi={version}
uvicorn={version}

pip install -r requirement.txt
```

## 1.3 建立第一個 GET 的 API

```python
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

```

## 1.4 執行 FastAPI Server

```
uvicorn main:app --reload
```

## 1.5  push to github 
git config --global user.name = "My Name"
git config --global user.email = "email@example.com"
git remote add origin https://github.com/huanchen1107/FastAPI-LInbot.git
git branch -M main
git push -u origin main