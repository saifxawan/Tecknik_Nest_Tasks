# Task 6: Gradio app to return reversed sentence
import gradio as gr

def reverse_sentence(sentence):
    return sentence[::-1]

demo = gr.Interface(fn=reverse_sentence, inputs="text", outputs="text")
demo.launch()
