import streamlit as st

def read_file(file_name):
    try:
        with open("labs/lab3/" + file_name, 'r', encoding = "utf-8") as file_local:
            datas = file_local.readlines()
            return datas
    except FileNotFoundError:
        st.warning(f"Файл {file_name} не знайдено.")
        create_file = st.radio("Бажаєте створити файл?", ["Так", "Ні"], index= 1 )
        if create_file == "Так":
            write_file(file_name, [])
            st.success(f"Файл {file_name} створено.")
            return []  
        elif create_file == "Ні":
            st.info("Введіть правильний файл або створіть його.")
            st.stop()  
            return []

def write_file(file_name, data):
    with open("labs/lab3/" + file_name, 'w', encoding = "utf-8") as file_local:
        file_local.writelines(data)

def lab3():
    st.subheader("Управління студентами")

    menu_options = [
        "Додати студента",
        "Відобразити студентів",
        "Знайти студента",
        "Сортувати студентів за середнім балом",
        "Видалити студента"
    ]

    choice = st.selectbox("Виберіть опцію:", menu_options)

    group = st.text_input("Введіть групу (англійською, наприклад 11-KI):")
    if group:
        group += ".txt"

    if group: 
        data = read_file(group) 

    if choice == "Додати студента" and group:
        surname = st.text_input("Введіть прізвище студента:")
        avg_bal = st.number_input("Введіть середній бал:", min_value=0, step=1)
        if st.button("Додати студента"):
            data.append(f"{surname} {avg_bal}\n")
            write_file(group, data)
            st.success("Дані успішно додані.")

    elif choice == "Відобразити студентів" and group:
        if data: 
            st.write("Список студентів:")
            for i, student in enumerate(data):     
                st.markdown(f"""
                    ```
                    {i + 1}. {student.strip()}
                    ```""")
        else:
            st.warning("Список порожній.")

    elif choice == "Знайти студента" and group:
        shyk_student = st.text_input("Введіть шуканого студента:")
        if st.button("Знайти студента"):
            found = False
            for entry in data:
                if entry.startswith(shyk_student):
                    found = True
                    surname, avg_bal = entry.strip().split(" ")
                    st.success(f"Студент {surname} знайдений у списку з середнім балом {avg_bal}.")
                    break
            if not found:
                st.error("Студента нема в списку.")

    elif choice == "Сортувати студентів за середнім балом" and group:
        if data:
            valid_data = []
            for entry in data:
                if len(entry.split()) == 2:
                    valid_data.append(entry)
            sorted_data = sorted(valid_data, key=lambda x: float(x.split(" ")[1]), reverse=True)
            st.write("Відсортований список студентів:")
            for entry in sorted_data:
                st.markdown(f"""```
{entry.strip()}""")
        else:
            st.warning("Список порожній.")
    elif choice == "Видалити студента" and group:
        if data:
            delete_index = st.number_input("Введіть номер студента для видалення:", min_value=1, max_value=len(data), step=1)
            if st.button("Видалити студента"):
                stud_delete = data.pop(delete_index - 1).strip()
                write_file(group, data)
                st.success(f"Студента {stud_delete} успішно видалено.")
        else:
            st.warning("Список порожній.")
