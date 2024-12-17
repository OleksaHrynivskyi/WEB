import random
import streamlit as st

def find_element(spysok, chyslo):
    """
    Шукає вказаний елемент у списку та повертає результат пошуку.

    Функція перевіряє, чи присутній заданий елемент у списку. Якщо елемент
    знайдено, вона повертає повідомлення з індексом елемента. Якщо елемент
    не знайдено, повертається повідомлення, що елемент не знайдено.

    """
    return spysok.index(chyslo) if chyslo in spysok else -200


def lab2():
    st.subheader("Пошук елемента в списку")
    n = st.number_input("Введіть кількість елементів списку: ", min_value=1, step=1)
    n = int(n)

    spysok_random = [random.randint(-10, 10) for i in range(n)]

    shchyslo = st.number_input("Введіть число, яке треба знайти: ", step = 1)

    res = find_element(spysok_random, shchyslo)

    if res != -200:
        st.markdown(f"""
                    ```
            Згенерований список - {spysok_random}
            Елемент {shchyslo} знайдено на індексі - {res}
            ```""")

    else:
        st.markdown(f"""
                    ```
            Згенерований список - {spysok_random}
            Елемент {shchyslo} не знайдено в списку
            ```""")



