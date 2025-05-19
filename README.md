# 中翻英翻譯機器（FastAPI + Hugging Face）
基於 [FastAPI](https://fastapi.tiangolo.com/) 與 [Hugging Face Transformers](https://huggingface.co/transformers/) 

## 專案功能

- 使用 Hugging Face 提供的 `opus-mt-zh-en` 模型進行中翻英。
- 提供 `/translate` API 路由，接收 JSON 格式請求並回傳翻譯結果。
- 支援 GPU/CPU 自動偵測。
- 可使用 Docker 容器快速打包與部署。

---

## 專案架構
- server.py # FastAPI 伺服器主程式
- client.py # 測試翻譯功能的客戶端
- Dockerfile # Docker 建構設定
- requirements.txt # Python 相依套件清單
- README.md # 說明文件

---
## 使用Docker啟動專案
1. 包成Image
    ```
    docker build -t text_translate .
    ```
2. 執行
    ```
    docker run -d --name text_translate_container -p 8097:8097 text_translate
    ```
---
## 測試API
1. 伺服器監聽
   ```
   python server.py
   ```
2. 客戶端發布請求
   ```
   python client.py
   ```
請求："text": "你好，今天天氣好"  
回應："translated_text": "Hello, the weather is nice today"
