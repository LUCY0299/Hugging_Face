from fastapi import FastAPI, Request
import uvicorn
import torch

app= FastAPI()

# initialize the model and tokenizer
def init_opus():
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
    model_path = "Helsinki-NLP/opus-mt-zh-en"
    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
    model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-zh-en")

    return tokenizer, model

def en_zh_translate(text, tokenizer, model):
    from transformers import pipeline
    translation_pipeline = pipeline("translation_zh_to_en",model=model, tokenizer=tokenizer, device = 0 if torch.cuda.is_available() else -1)
    finaltext = translation_pipeline(text)
    return finaltext[0]['translation_text']
translate_tokenizer, translate_model = init_opus()

# API definition
@app.post("/translate")
async def translate(request: Request):
    data = await request.json()
    text_to_translate = data['text']

    translated_text = en_zh_translate(text_to_translate, translate_tokenizer, translate_model)
    print(f"{text_to_translate} => {translated_text}")
    return {"translated_text": translated_text}

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0",workers=4, port=8097, log_level="info")
