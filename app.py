# app.py
import gradio as gr
from transformers import pipeline

sentiment = pipeline("sentiment-analysis")

def analyze_text(text):
    result = sentiment(text)[0]
    return f"Sentiment: {result['label']} (score: {result['score']:.2f})"

gr.Interface(fn=analyze_text, inputs="text", outputs="text", title="Mini AI Sentiment Analyzer").launch()
