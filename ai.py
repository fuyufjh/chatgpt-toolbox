
import openai
import logging

def translate(text, target_lang):
    logging.info("translate. text: %s, target_lang: %s", text, target_lang)
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": f"Please translate `{text}` to {target_lang}. Please return only translated content not include the origin text.",
        }],
    )
    
    return completion["choices"][0].get("message").get("content").encode("utf8").decode()

def rephrase(text):
    logging.info("rephrase. text: %s", text)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": f"Please improve the writing of the following text in its original language: `{text}`",
        }],
    )    
    return completion["choices"][0].get("message").get("content").encode("utf8").decode()

def write(language, title, content, other_req):
    logging.info("write. language: %s, title: %s, content: %s, other_req: %s", language, title, content, other_req)

    if language == "chinese (simplified)":
        if other_req == "":
            other_req = "无"
        prompt = f"请帮我写一篇标题为《{title}》的文章。文章大意为：\"{content}\"。其他要求：{other_req}。"
    elif language == "english":
        if other_req == "":
            other_req = "None"
        prompt = f"Please write an article with the title of \"{title}\". The main idea of the article is: \"{content}\". Other requirements: {other_req}."
    else:
        raise Exception("Language not supported")

    completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": prompt,
            }],
        )
    return completion["choices"][0].get("message").get("content").encode("utf8").decode()
