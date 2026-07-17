import streamlit as st
import plotly.express as px

data = [
    # Resident Evil
    {"игра": "Resident Evil 4 Remake", "серия": "Resident Evil", "оценка": 93, "часы": 16},
    {"игра": "Resident Evil Village", "серия": "Resident Evil", "оценка": 84, "часы": 15},
    {"игра": "Resident Evil 2 Remake", "серия": "Resident Evil", "оценка": 91, "часы": 11},
    # Red Dead Redemption
    {"игра": "Red Dead Redemption 2", "серия": "RDR", "оценка": 97, "часы": 50},
    {"игра": "Red Dead Redemption", "серия": "RDR", "оценка": 95, "часы": 18},
    # Скандинавский God of War
    {"игра": "God of War (2018)", "серия": "God of War", "оценка": 94, "часы": 21},
    {"игра": "God of War Ragnarök", "серия": "God of War", "оценка": 94, "часы": 26},
]

st.title('⚔️ Анализ культовых AAA-синглов')

franchises = ['Все серии', 'Resident Evil', 'Red Dead Redemption', 'God of War']
selected_franchise = st.sidebar.selectbox('Выбери серию игр:', franchises)

metric = st.sidebar.radio('Что сравниваем?', ['Оценка на Metacritic', 'Время на сюжет (часов)'])
metric_key = 'оценка' if metric == 'Оценка на Metacritic' else 'часы'

if selected_franchise != 'Все серии':
    filtered_data = [item for item in data if item['серия'] == selected_franchise]
else:
    filtered_data = data


fig = px.bar(
    filtered_data,
    x='игра',
    y=metric_key,
    color='серия',
    text=metric_key,
    title=f'Сравнение по параметру: {metric}'
)

fig.update_traces(textposition='inside')
fig.update_layout(yaxis_title=metric)

st.plotly_chart(fig)