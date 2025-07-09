
# 📊 Screen Time Tracker

Track and visualize your daily **laptop** and **phone** screen time, compare trends over time, and gain insights into your usage patterns.
Built with **Streamlit**, **SQLite**, and **Plotly**, this app offers an interactive and clean dashboard experience.

---

## 🚀 Features

✅ Log daily screen time (laptop & phone)
✅ Interactive sliders for intuitive input
✅ Automatic updates if you re-enter for the same date
✅ KPIs: totals, averages, device dominance
✅ Interactive line & bar charts with semantic colors (green = positive, red = negative)
✅ View raw data in a sortable, formatted table
✅ Clean layout with tabs for trends, comparisons, and data table

---

## 🖥 Demo

📌 Hosted App: *\[Add link once deployed on Streamlit Cloud]*

---

## 📂 Tech Stack

* **Frontend/UI:** Streamlit
* **Charts:** Plotly
* **Database:** SQLite
* **Language:** Python 3.10+

---

## 📋 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/screen-time-tracker.git
cd screen-time-tracker
```

### 2️⃣ Create Virtual Environment

If you’re using [UV](https://github.com/astral-sh/uv):

```bash
uv venv .venv
source .venv/bin/activate
```

Or with `venv`:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
uv pip install -r requirements.txt
```

or

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App Locally

```bash
streamlit run app.py
```

The app will open in your browser at:
👉 [http://localhost:8501](http://localhost:8501)

---

## 🌐 Deployment

### Streamlit Cloud (Recommended)

1. Push your code to a public or private GitHub repository.
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud).
3. Log in with your GitHub account.
4. Click **"New app"**, select this repository, branch, and point to `app.py`.
5. Deploy — your app will be live at `https://your-app-name.streamlit.app/`.

---

## 📄 Project Structure

```
screen-time-tracker/
├── app.py              # Streamlit app
├── db.py               # Database functions
├── requirements.txt    # Dependencies
├── README.md           # This file
```

---

## 📜 Example Screenshot
![Page Screenshot](<app.png>)


---

## ✨ Future Improvements

* Weekly/monthly aggregates
* Dark/light theme toggle
* Cloud-hosted database (PostgreSQL) for persistence
* Authentication for multi-user support

---



- Built with ❤️ by [Pritam].
- Date: July 9, 2025.
---
