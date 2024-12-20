# WEB Менеджер Лабораторних Робіт

## Опис проекту

Цей веб-додаток створений для демонстрації та інтерактивного запуску 7 лабораторних робіт з програмування. Додаток розроблений з використанням Streamlit та надає зручний інтерфейс для перегляду відео, опису та безпосереднього запуску лабораторних робіт.

## Особливості

- Навігація через бічне меню
- Сторінки:
  - Головна: Вибір та запуск лабораторних робіт
  - Про мене: Інформація про автора
  - Зв'яжіться зі мною: Форма зворотного зв'язку

- Функціональність для кожної лабораторної роботи:
  - Перегляд відео демонстрації
  - Читання опису лабораторної роботи
  - Безпосередній запуск програми

## Технології

- Python
- Streamlit
- smtplib (для надсилання електронної пошти)
- Модулі власних лабораторних робіт

## Вимоги до середовища

- Python 3.x
- Бібліотеки:
  - streamlit
  - smtplib
  - ssl

## Встановлення та запуск

1. Клонуйте репозиторій:
   ```bash
   git clone [URL цього репозиторію]
   ```

2. Встановіть необхідні залежності:
   ```bash
   pip -r requirements.txt
   ```

3. Запустіть додаток:
   ```bash
   python -m streamlit run web.py
   ```
або скористайтеся покликанням на згенерований сайт: https://my-app-web-exam.streamlit.app/

## Структура проекту

```
laboratory-works/
│
├── web.py             # Головний файл Streamlit
├── functions.py        # Додаткові функції
├── labs/               # Директорія з лабораторними роботами
│   ├── lab1.py
│   ├── lab2.py
│   ├── ...
│   └── lab7.py
└── README.md
```

## Функції

### Головна сторінка
- Вибір лабораторної роботи
- Три режими перегляду: відео, опис, запуск

### Сторінка "Про мене"
- Коротка інформація про автора
- Можливість залишити зірковий відгук

### Сторінка "Зв'яжіться зі мною"
- Форма для надсилання електронного листа
- Підтримка зворотного зв'язку

