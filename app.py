import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Ekibastuz Biz Hub", layout="wide")

# Верхнее меню
tab1, tab2 = st.tabs(["💰 Финансы бизнеса", "🏆 Квесты (Задачи)"])

# Вкладка 1: ФИНАНСЫ
with tab1:
    st.header("Учет доходов и рекламы")
    col_in, col_met = st.columns([1, 2])
    
    with col_in:
        biz_type = st.selectbox("Проект", ["Полировка плит", "Курс Ремонт", "Курс Таргет", "Wildberries"])
        spend = st.number_input("Затраты на рекламу (₸)", min_value=0, step=500)
        rev = st.number_input("Выручка (₸)", min_value=0, step=1000)
        if st.button("Сохранить транзакцию"):
            st.success("Данные учтены!")
            
    with col_met:
        profit = rev - spend
        st.metric("Чистая прибыль", f"{profit} ₸", delta=f"{profit} ₸")
        st.info("Тут будет график, когда наберется история за несколько дней")

# Вкладка 2: ГЕЙМИФИКАЦИЯ
with tab2:
    st.header("Прокачка предпринимателя")
    
    if 'xp' not in st.session_state: st.session_state.xp = 0
    if 'tasks' not in st.session_state: st.session_state.tasks = []

    lvl = st.session_state.xp // 100
    st.write(f"### Уровень: {lvl} 🛡️")
    st.progress((st.session_state.xp % 100) / 100)
    
    with st.expander("➕ Добавить новый квест"):
        t_name = st.text_input("Название задачи")
        t_xp = st.slider("Награда (XP)", 10, 100, 20)
        if st.button("Добавить в список"):
            st.session_state.tasks.append({"name": t_name, "xp": t_xp, "done": False})
            st.rerun()

    for i, t in enumerate(st.session_state.tasks):
        if not t["done"]:
            if st.button(f"✅ {t['name']} (+{t['xp']} XP)", key=f"t_{i}"):
                t["done"] = True
                st.session_state.xp += t["xp"]
                st.rerun()
