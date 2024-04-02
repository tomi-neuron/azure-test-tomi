import gradio as gr
from fastapi import FastAPI

app = FastAPI()

def echo(message, history):
    return message

demo = gr.ChatInterface(fn=echo, examples=["hello", "hola", "merhaba"], title="Echo Bot")

app = gr.mount_gradio_app(app, demo, path="/")

