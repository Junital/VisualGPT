import gradio as gr
from transformers import ViltProcessor, ViltForQuestionAnswering, AutoTokenizer, ViTImageProcessor, \
    VisionEncoderDecoderModel
import torch
from llm.gpt import transla, infer

processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model1 = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model2 = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer2 = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model2.to(device)
gen_kwargs = {"max_length": 16, "num_beams": 4}

def give_answer(image, text):
    with open('api.txt', 'r') as file:
        key = file.read()
        
    after_trans = transla(key, text)
    encoding = processor(image, after_trans, return_tensors="pt")
    outputs = model1(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()
    pixel_values = feature_extractor(images=[image], return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)
    output_ids = model2.generate(pixel_values, **gen_kwargs)
    preds = tokenizer2.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    
    print("Predicted answer:", model1.config.id2label[idx], ",", preds[0])
    global myans
    myans=infer(key, model1.config.id2label[idx], preds[0], after_trans)
    return myans

demo = gr.Interface(fn=give_answer, inputs=[gr.inputs.Image(), gr.inputs.Textbox(label="Your question")], 
                    outputs=gr.outputs.Textbox(label="Output"))

demo.launch(share=True)