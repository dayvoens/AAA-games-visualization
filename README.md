# ⚔️ Анализ культовых AAA-синглов

> Интерактивный дашборд для сравнения топовых одиночных игр по оценкам критиков и времени прохождения сюжета. Никакого онлайн-калла — только чистокровные шедевры.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-🔥-FF4B4B?style=for-the-badge)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-📊-2385CD?style=for-the-badge)](https://plotly.com)

🔗 **[Открыть интерактивный дашборд в браузере](https://aaa-games-visualization-xemzsiwjadi2v8kwqmfhmd.streamlit.app/)**

---

## 🕹️ Что умеет это приложение?

* **Фильтрация по франшизам:** Удобный выбор культовых серий в один клик (Resident Evil, RDR, God of War).
* **Динамическое переключение метрик:** График на лету перестраивается между оценками на Metacritic и реальным временем на прохождение сюжета.
* **Полная интерактивность:** Графики можно зумить, масштабировать и смотреть точные данные при наведении мыши благодаря Plotly.

## 🛠️ Стек технологий

* **Python** - база и логика приложения
* **Streamlit** - быстрый и чистый веб-интерфейс без HTML/CSS
* **Plotly Express** - сочные интерактивные графики

---

## 🚀 Как запустить проект у себя на компе

```bash
git clone [https://github.com/dayvoens/AAA-games-visualization.git](https://github.com/dayvoens/AAA-games-visualization.git)

cd AAA-games-visualization

pip install -r requirements.txt

streamlit run games-genres.py
