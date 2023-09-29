<div align='center'>

<img src = ./fig/logo.png width=50%>


基于 [ViT](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning) 和 [ChatGPT](https://openai.com/chatgpt) 混合模型开发的全新问答系统！

[![Structure](https://img.shields.io/badge/-Structure-7e57c2)](/src/structure.html)

</div>

## 产品介绍

"问春" 是一个基于自然语言处理和图像处理技术的问答系统, 可以回答用户对于一张图片和一个问题的提问.

- 输入

    "问春" 需要用户提供一张图片和一个问题. 您可以将要提问的图片和问题分别输入到图像和文本框中.

- 回答

    "问春" 将返回一个针对提问图片以及问题的回答. 例如, 如果您提供了一张图片, 并问 "图片中的女孩是什么发色", 该系统可能会回答: "女孩的发色是蓝色的”.

- 技术支持

    "问春" 采用了自然语言处理和图像处理技术, 通过使用训练的语言模型和图像编码器来理解问题和图片, 并使用深度学习技术来训练和部署模型. 此外, 该系统使用了多个开源软件库来提高效率和可靠性.

<div align='center'>

<img src=./fig/demo.jpg width=90%/>

</div>

- 应用平台

    "问春" 利用混合模型的优势, 提高了系统的准确性和鲁棒性, 同时可以根据用户的反馈, 动态调整模型的权重, 实现自适应学习, 具有广阔的应用前景, 如智慧医疗医疗图像辅助诊断, 智慧安保通过预设问题分析监控检测危险等.


## 简明示范

<div align='center'>

<img src=./fig/System.gif width=100%/>

</div>

## 安装说明

1. 下载zip文件

2. 将自己的OpenAI API 放入`api.txt`中。

3. 执行main.py即可