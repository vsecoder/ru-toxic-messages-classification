from api import API
import json
import gradio as gr


# Initialize API
api = API()


def check(text):
    res = api.check(text)
    #answer = \
    #    f'Verdict: {"Toxic" if res["toxic_percent"] > 70 else "Neutral"}\n\n' \
    #    f' Toxic - {res["toxic_percent"]}%\n' \
    #    f' Neutral - {res["neutral_percent"]}%\n\n' \
    #    f'Work time: {res["work_time"]}'
    answer = {"toxic": res["toxic_percent"]/100, "neutral": res["neutral_percent"]/100}
    return answer


with gr.Blocks() as demo:
    gr.Markdown("# Russian toxic messages classification.")
    name = gr.Textbox(label="Message")
    #output = gr.Textbox(label="Result")
    output = gr.Label(num_top_classes=2)
    greet_btn = gr.Button("Check")
    greet_btn.click(fn=check, inputs=name, outputs=output, api_name="check")

    with gr.Accordion("Samples"):
        gr.Markdown("https://t.me/CoffeeCodeBot")
        gr.Markdown("![изображение](https://user-images.githubusercontent.com/60792943/236311527-c0998f7c-6b91-4dd0-a7f8-1c6c29ca17ed.png)")

    with gr.Accordion("GitHub"):
        gr.Markdown("https://github.com/vsecoder/ru-toxic-messages-classification")


demo.launch(share=True)
