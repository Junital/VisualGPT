import gradio as gr
from transformers import ViltProcessor, ViltForQuestionAnswering, AutoTokenizer, ViTImageProcessor, \
    VisionEncoderDecoderModel
from PIL import Image as im
from PIL import ImageTk
import torch

processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model2 = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model2.to(device)

max_length = 16
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}


def give_answer(image, text):
    # print("ss", selectFileName)

    # prepare inputs
    encoding = processor(image, text, return_tensors="pt")

    # forward pass
    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()

    pixel_values = feature_extractor(images=[image], return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)

    output_ids = model2.generate(pixel_values, **gen_kwargs)

    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]

    print("Predicted answer:", model.config.id2label[idx], ",", preds[0])
    global myans
    myans = 'Here is a picture about \"' + preds[0] + \
            '\", and  when it comes to the question\"' + text + '\" , I think the answer is \"' \
            + model.config.id2label[idx] + '\".'
    # Here is a picture about "people standing on top of a body of water", and  when it comes to the question
    # "How many fishes are there in the picture?" , I think the answer is "12".
    return myans


demo = gr.Interface(fn=give_answer, inputs=[gr.inputs.Image(), gr.inputs.Textbox(label="Your question")], 
                    outputs=gr.outputs.Textbox(label="Output"))


demo.launch(share=True)