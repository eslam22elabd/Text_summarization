from fastapi import FastAPI
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

# Load the trained model and tokenizer
tokenizer = T5Tokenizer.from_pretrained("summarization_toknizer")
model = T5ForConditionalGeneration.from_pretrained("summarization_model")



app = FastAPI()

class TextInput(BaseModel):
    content: str

def summarize_text(text, max_length=50):
    # إضافة البادئة للنص
    input_text = "summarize: " + text
    
    # تحويل النص إلى توكنز
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    
    # توليد الملخص
    summary_ids = model.generate(input_ids,
                                 max_length=max_length,
                                 num_beams=4,
                                 no_repeat_ngram_size=2,
                                 early_stopping=True)
    
    # فك ترميز الملخص وإرجاعه
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

@app.post("/summarize/")
async def summarize(input: TextInput):
    summary = summarize_text(input.content)
    return {"summary": summary}
