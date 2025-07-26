# Task 5: Gradio app to return square of a number
import gradio as gr

def square_number(x):
    return x * x

demo = gr.Interface(fn=square_number, inputs="number", outputs="number")
demo.launch()
