import requests
from bs4 import BeautifulSoup
from collections import Counter
import streamlit as st



def lab6():


    url = st.text_input("Введіть покликання: ")

    try:
        if url:
            res = requests.get(url)
            res.raise_for_status()

            soup = BeautifulSoup(res.text, "html.parser")

            text = soup.get_text().lower()

            words = Counter(text.split())

            all_tags = soup.find_all(True)

            tag_name = []

            for tag in all_tags:
                tag_name.append(tag.name)

            tag_kilkist = Counter(tag_name)

            links = len(soup.find_all('a'))
            images = len(soup.find_all('img'))

            output = f"""
            Кількість посилань: {links}\nКількість зображень: {images}
            \nЧастота слів (найбільш популярні):
"""
            for word, count in words.most_common(10):
                output += f"{word}: {count}\n"

            output += "\nЧастота HTML-тегів:\n"
            for tag, count in tag_kilkist.items():
                output += f"{tag}: {count}\n"

            st.markdown(f"```\n{output}\n```")
            
        else:
            st.warning("Будь ласка, введіть покликання")
    except requests.exceptions.RequestException as e:
        st.error(f"Помилка при отриманні сторінки: {e}")