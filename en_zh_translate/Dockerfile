# Basic Image Environment
FROM python:3.11-slim

# set Image工作目錄
WORKDIR /app

# 將 Dockerfile 所在目錄下的所有檔案複製到 Image 的工作目錄 /app 底下
ADD . /app

# 在 Image 中執行的指令：安裝 requirements.txt 中所指定的 dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 啟動 FastAPI 伺服器
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8097", "--workers", "4"]

