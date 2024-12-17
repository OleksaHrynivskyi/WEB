from math import *
import random
import streamlit as st


def lab1():

    zavd = st.selectbox("Виберіть завдання (1-3): ", ["Завдання 1", "Завдання 2", "Завдання 3"],    
     index=None,
     placeholder="Виберіть завдання...")


    if zavd == "Завдання 1":
        st.subheader("Математичний вираз")

        m = st.number_input("Введіть додатнє число m ")

        if m < 0:
            st.write("Ви ввели не додатнє число!")
        else:
            z = 1/(sqrt(m)+sqrt(2))
            st.latex(r"""\frac{1}{\sqrt{m}+\sqrt{2}} = """ + f"{z:.4f}")

    elif zavd == "Завдання 2":
        st.subheader("Перевірка на просте число")

        try:
            number = st.number_input("Введіть число для перевірки", min_value=0, step=1)
            number = int(number)
            is_prime = True  

            if number <= 1:
                is_prime = False
            else:
                if number == 2:
                    is_prime = True
                elif number % 2 == 0:
                    is_prime = False
                else:
                    for i in range(3, int(sqrt(number)) + 1, 2):
                        if number % i == 0:
                            is_prime = False
                            break
            if is_prime:
                st.success(f"Число {number} є простим.")
            else:
                st.error(f"Число {number} не є простим.")

        except ValueError:
            st.error("Ви ввели не число")

    elif zavd == "Завдання 3":
        st.subheader("Робота з списком")

        n = st.number_input("Введіть кількість елементів списку", min_value=1, step=1)
        n = int(n)

        spysok_random = [random.randint(-10, 10) for _ in range(n)]
        min_spys = []

        for i in spysok_random:
            if i > 0:
                min_spys.append(i)
        if not min_spys:
            minim = "Немає додатніх елементів"
        else:
            minim = min(min_spys)   


        sum_spys = []

        for i in spysok_random:
            if i % 2 == 0:
                sum_spys.append(i)
        if not sum_spys:
            sumim = "Немає парних елементів"
        else:
            sumim = sum(sum_spys)


        zvorot = spysok_random[::-1]
        st.markdown(f"""
                    ```
            Згенерований список - {spysok_random}
            Мінімальний додатній елемент - {minim}
            Сума парних елементів - {sumim}
            Зворотній список - {zvorot}
            ```
                                        """)
