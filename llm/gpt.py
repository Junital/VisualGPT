import openai

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def transla(key, string):
    openai.api_key = key

    prompt = f"""
    请将下面的文本翻译成英文：

    ```
    {string}
    ```
    """
    response = get_completion(prompt)
    
    return response 


def infer(key, text1, text2, text3):
    openai.api_key = key

    prompt = f"""
    Follow the example to give the answer:
    [Question] What is the cat doing? [Information] Cat、Yellow、Crawl
    [Answer] The cat is crawling.

    ```
    [Question] {text1} [Information] {text2}、{text3}
    ```
    
    """
    response = get_completion(prompt)

    # print(response)

    substring = "[Answer]"
    text = response.replace(substring, "")

    prompt = f"""
    请将下面的英文翻译成中文：

    ```
    {text}
    ```
    """

    response = get_completion(prompt)
    
    return response 

if __name__ == '__main__':
    with open('./api.txt', 'r') as f:
        key = f.read()
    print(infer(key, "What's in the picture?", "mountain", "a mountain range with mountains and mountains"))