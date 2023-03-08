import streamlit as st
from ai import *

st.set_page_config(page_title='ChatGPT Toolbox')

st.title("ChatGPT Toolbox")

tab_translate, tab_rephrase, tab_write = st.tabs(["Translate", "Rephrase", "Write"])

with tab_translate:
    text = st.text_area("Enter text:",height=200,max_chars=None,key="text_to_translate",help="Enter your text here")

    option_target = st.selectbox('Output language',
                        ('chinese (simplified)', 'chinese (traditional)', 'english', 'french', 'german', 'italian', 'japanese', 'russian', 'spanish'))

    if st.button('Translate'):
        if text == "":
            st.warning('Please **enter text** for translation')

        else:
            result = translate(text, option_target)
            st.info(str(result))

            st.success("Translation is **successfully** completed!")
    else:
        pass

with tab_rephrase:
    text = st.text_area("Enter text:",height=200,max_chars=None,key="text_to_rephrase",help="Enter your text here")

    if st.button('Improve my writing'):
        if text == "":
            st.warning('Please **enter text** to be improved')

        else:
            result = rephrase(text)
            st.info(str(result))

            st.success("Rephrasing is **successfully** completed!")
    else:
        pass

with tab_write:
    language = st.selectbox('Language', ('chinese (simplified)', 'english'))

    if language == "chinese (simplified)":
        title_placeholder = "例：ChatGPT写作：快速生成优质博客文章的神器"
        content_placeholder = "例：ChatGPT是一个基于GPT-3的在线写作工具，可以帮助你快速生成优质博客文章。要熟悉使用ChatGPT的技巧和方法，写出更高质量的文章，可以按照以下...步骤进行。"
        other_req_placeholder = "例：长度1000字左右"
    elif language == "english":
        title_placeholder = "e.g. ChatGPT Writing: A tool to quickly generate high-quality blog posts"
        content_placeholder = "e.g. ChatGPT is an online writing tool based on GPT-3 that can help you quickly generate high-quality blog posts. To familiarize yourself with the skills and methods of using ChatGPT to write higher quality articles, you can follow the steps below..."
        other_req_placeholder = "e.g. The length should be about 1000 words."
    else:
        st.error("Language not supported")

    title = st.text_input("Title:",max_chars=None,key="title",placeholder=title_placeholder)
    content = st.text_area("Content:",height=None,max_chars=None,key="content",placeholder=content_placeholder)
    other_req = st.text_input("Other requirements:",max_chars=None,key="other_req",placeholder=other_req_placeholder)
    
    if st.button('Write'):
        if title == "" or content == "":
            st.warning('Title and Content are required.')
        else:
            result = write(language, title, content, other_req)
            st.info(str(result))
            st.success("Writing is **successfully** completed!")
