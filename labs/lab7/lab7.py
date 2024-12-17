import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import streamlit as st



def lab7():

    try:
        zavd = st.selectbox("Виберіть завдання (1-3): ", ["Завдання 1", "Завдання 2", "Завдання 3"],     
            index=None,
            placeholder="Виберіть завдання...")

        if zavd == "Завдання 1":
            st.subheader("Графік функції")
            x = np.linspace(0.01, 5, 1000)
            y = 5 * np.cos(10 * x) * np.sin(3 * x) / np.sqrt(x)
            plt.plot(x, y, color = "pink", label=r'$F(x) = \frac{5 \cos(10x) \sin(3x)}{\sqrt{x}}$')

            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Графік функції F(x) = 5 * cos(10x) * sin(3x) / sqrt(x)')
            plt.legend()

            plt.savefig('labs/lab7/function.png', dpi=500)

            with open("labs/lab7/function.png", "rb") as file:
                image = file.read()


            st.image('labs/lab7/function.png')

            st.download_button(
                label="Завантажити зображення",
                data=image,
                file_name="function.png"
            )


        elif zavd == "Завдання 2":
            st.subheader("Побудова гістограми за текстом")

            text = st.text_input("Введіть текст для аналізу ")
            text = text.lower()
            text = text.replace(" ", "")
            count = Counter(text)
            bykvu = list(count.keys())
            chastota = list(count.values())
            if text:
                plt.bar(bykvu, chastota, color='pink')

                plt.xlabel('Літери')
                plt.ylabel('Частота')
                plt.title('Частота літер у тексті')

                plt.savefig('labs/lab7/histograma.png', dpi=500)

                with open("labs/lab7/histograma.png", "rb") as file:
                    image = file.read()

                st.image('labs/lab7/histograma.png')

                st.download_button(
                    label="Завантажити зображення",
                    data=image,
                    file_name="histograma.png"
                )              

        elif zavd == "Завдання 3":
            st.subheader("Побудова гістограми за типами речень")

            text = st.text_input(("Введіть текст для аналізу "))
            text = text.replace('...', ' <<TripleDot>> ')

            prosti = []
            potal = []
            oklich = []
            trykrap = []

            words = text.split()
            for word in words:  
            
                if "<<TripleDot>>" in word:
                    trykrap.append(word)
                elif word.endswith("!"):
                    oklich.append(word)
                elif word.endswith("?"):
                    potal.append(word)
                elif word.endswith("."):
                    prosti.append(word)

            types = ['Прості', 'Питальні', 'Окличні', 'Три крапки']

            chastota = [len(prosti), len(potal), len(oklich), len(trykrap)]

            if text:

                plt.bar(types, chastota, color=['blue', 'green', 'red', 'orange'])
                plt.xlabel('Типи речень')
                plt.ylabel('Частота')
                plt.title('Частота появи різних типів речень у тексті')

                plt.savefig('labs/lab7/histograma_2.png', dpi=500)

                with open("labs/lab7/histograma_2.png", "rb") as file:
                    image = file.read()

                st.image('labs/lab7/histograma_2.png')

                st.download_button(
                    label="Завантажити зображення",
                    data=image,
                    file_name="histograma_2.png"
                )              

    except Exception as e:
        print(f"Сталася помилка: {e}")