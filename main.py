import streamlit as st
import pandas as pd
from Class_Bert import BertClassifier
from sklearn.model_selection import train_test_split

def start_inf():
    new_new = news_text
    class_pred = ["Bad", "Good"][classifier.predict(new_new)]
    st.write(f"Predicted class: {class_pred}")

# Инициализация модели
classifier = BertClassifier(
    model_path='cointegrated/rubert-tiny2',
    tokenizer_path='cointegrated/rubert-tiny2',
    n_classes=2,
    epochs=4,
    model_save_path='bert.pt'
)

st.set_page_config(layout="wide")
st.title("Предсказание класса новости")

# Вставка новости через текстовое поле
news_text = st.text_input("Вставьте новость")

# Кнопка для начала предсказания
if st.button("Начать предсказание"):
    start_inf()
