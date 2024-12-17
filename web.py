import streamlit as st
import smtplib, ssl
from labs.lab1 import lab1 
from labs.lab2 import lab2
from labs.lab3 import lab3
from labs.lab4 import lab4
from labs.lab5 import lab5
from labs.lab6 import lab6
from labs.lab7 import lab7

def labs(video_url, readme, run):
    typ = st.radio("Виберіть тип взаємодії:",
                   ["Подивитись відео роботи в CLI", 
                    "Переглянути опис програми", 
                    "Запустити програму"], 
                   index=None, 
                   horizontal=True)
    if typ == "Подивитись відео роботи в CLI":
        st.video(video_url)

    elif typ == "Переглянути опис програми":
        with open(readme, "r", encoding="utf-8") as f:
            readme = f.read()
        st.markdown(readme)
        
    elif typ == "Запустити програму":
        run()

def send_email(message):
    username = 'hrynivskyi.oleksa.clg@chnu.edu.ua'  
    password = st.secrets["PASSWORD"] 

    host = "smtp.gmail.com"
    port = 465

    receiver = 'hrynivskyi.oleksa.clg@chnu.edu.ua' 
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message.encode('utf-8'))




st.sidebar.title("**Навігація по сайту**")

if "page" not in st.session_state:
    st.session_state.page = "Головна"

if st.sidebar.button("🏠 Головна"):
    st.session_state.page = "Головна"
if st.sidebar.button("🔗Про сайт"):
    st.session_state.page = "Про сайт"
if st.sidebar.button("👤 Про мене"):
    st.session_state.page = "Про мене"
if st.sidebar.button("✉️ Зв'яжіться зі мною"):
    st.session_state.page = "Зв'яжіться зі мною"



page = st.session_state.page 

if page == "Головна":

    st.title("Web - Інтерфейс")
    st.subheader("Оберіть лабораторну для запуску")

    option = st.selectbox(
        "",
        ("Лабораторна робот №1", 
        "Лабораторна робот №2", 
        "Лабораторна робот №3", 
        "Лабораторна робот №4", 
        "Лабораторна робот №5", 
        "Лабораторна робот №6", 
        "Лабораторна робот №7"),    
        index=None,
        placeholder="Виберіть лабораторну роботу...")

    match option:
        case "Лабораторна робот №1":
            st.write("Запуск лабораторної роботи №1")
            labs(
                "https://youtu.be/9QzOviHmjRQ", 
                "labs/lab1/README.md", 
                lab1.lab1
            )

        case "Лабораторна робот №2":
            st.write("Запуск лабораторної роботи №2")
            labs(
                "https://youtu.be/atYYRUphooU",
                "labs/lab2/README.md",
                lab2.lab2
            )
        case "Лабораторна робот №3":
            st.write("Запуск лабораторної роботи №3")
            labs(
                "https://youtu.be/D7LACh0ANJI",
                "labs/lab3/README.md",
                lab3.lab3
            )
        case "Лабораторна робот №4":
            st.write("Запуск лабораторної роботи №4")
            labs(
                "https://youtu.be/wQPJ8FDUYGw",
                "labs/lab4/README.md",
                lab4.lab4
            )
        case "Лабораторна робот №5":
            st.write("Запуск лабораторної роботи №5")
            labs(
                "https://youtu.be/YsxavtKmZl0",
                "labs/lab5/README.md",
                lab5.lab5
            )
        case "Лабораторна робот №6":
            st.write("Запуск лабораторної роботи №6")
            labs(
                "https://youtu.be/tI23nLg3YMk",
                "labs/lab6/README.md",
                lab6.lab6
            )
        case "Лабораторна робот №7":
            st.write("Запуск лабораторної роботи №7")
            labs(
                "https://youtu.be/RWr1CECE-p0",
                "labs/lab7/README.md",
                lab7.lab7
            )

elif page == "Про мене":
    st.title("Про мене")
    st.subheader("Привіт! Мене звати Олекса. Я студент коледжу ЧНУ, який набує досвіду в галузі програмування. ")
    st.write("""
    Завжди захоплювався написанням програм, тому вирішив створити цей сайт, щоб покращити знання та успішно здати сесію. 

    На сайті ви знайдете головне вікно, де представлені адаптовані 7 лабораторних робіт з відео матеріалами та описом.
    Також присутня ця вкладка про мене, і вкладка для зв'язку у разі якихось проблем.


    Сподіваюся, що мій сайт буде корисним для вас!
    """)


    selected = st.feedback("stars")
    if selected:
        st.subheader("Дякую за відгук!")

elif page == "Зв'яжіться зі мною":
    st.title("Зв'яжіться зі мною")



    with st.form(key='contact_form'):
        user_email = st.text_input("Ваша електронна адреса")
        user_name = st.text_input("Ваше ім'я")
        raw_message = st.text_area("Повідомлення")
        message = f"""\
Subject: Нове повідомлення з вашого сайту!

Від: {user_email}, {user_name}
{raw_message}
"""
        button = st.form_submit_button("Надіслати")
        if button:
            send_email(message)
            st.info("Повідомлення надіслано!")

elif page == "Про сайт":
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()
    st.markdown(readme)