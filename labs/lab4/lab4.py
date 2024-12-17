import random
from collections import Counter
import streamlit as st



def lab4():
    zavd = st.selectbox("Виберіть завдання (1-3): ", ["Завдання 1", "Завдання 2", "Завдання 3"],
        index=None,
        placeholder="Виберіть завдання...")


    if zavd == "Завдання 1":
        st.subheader("Генерація випадкової фрази")

        
        spys1 = ["Красивий", "Щасливий", "Злий", "Швидкий", "Терплячий"]

        spys2 = ["какаду", "собака", "тигр", "страус", "кит"]

        spys3 = ["стрибає", "плаває", "бігає", "говорить", "їсть"]


        n = st.button("Згенерувати нове речення")
        if n:
            st.success(f"Згенероване речення: {random.choice(spys1)} {random.choice(spys2)} {random.choice(spys3)}") 

    elif zavd == "Завдання 2":
        st.subheader("Аналіз текстового файлу")

        uploaded_file = st.file_uploader("Оберіть текстовий файл для аналізу", type=["txt"])

        if uploaded_file is not None:

            text = uploaded_file.read().decode("utf-8") 
            
            withspaces = len(text)
            withoutspaces = len(text.replace(" ", ""))
            words = text.split()
            allwords = len(words)
            uniquewords = len(set(words))
            wordsCount = Counter(words)
            word1time = []

            for word, count in wordsCount.items():
                if count == 1:
                    word1time.append(word)

            totalwords1 = len(word1time)
            st.markdown(f"""
                        ```
                Кількість слів, які зустрічаються один раз: {totalwords1}
                Кількість унікальних слів у тексті: {uniquewords}
                Кількість слів у тексті: {allwords}
                Кількість символів з пробілами: {withspaces}
                Кількість символів без пробілів: {withoutspaces}
                ```
                                            """)

    elif zavd == "Завдання 3":
        st.subheader("Аналіз послідовностей текстового файлу")

        uploaded_file = st.file_uploader("Оберіть текстовий файл для аналізу", type=["txt"])

        if uploaded_file is not None:
            
            text = uploaded_file.read().decode("utf-8")

            words = text.split()
            N = st.number_input("Введіть кількіть слів у послідовності N: ", min_value = 2, step = 1)
            N = int(N)
            spys = []
            words_all = len(words) - N + 1

            for i in range(words_all):
                aboba = ""
                for j in range(N):
                    aboba = aboba + words[i + j] + " "
                aboba = aboba.strip()
                spys.append(aboba)

            rah = Counter(spys)
            st.subheader(f"""Топ-10 найчастіше зустрічаємих послідовностей з {N} слів""")
            most_common = rah.most_common(10)
            for i, (s, count) in enumerate(most_common, start=1):
                st.write(f"""```
                            {i}. {s} — Зустрічається: {count} разів""")