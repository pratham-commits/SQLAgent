# SQLAgent

---

⚡ Talk to your SQL database like it's ChatGPT.  
Built with 🦙 LLaMA 3 + LangChain + Streamlit.  

> Gen Z devs don't query SQL. We chat with it. 🤖💬

---

## 🚀 What’s Inside?

This app is a full-blown SQL whisperer. You just ask it things like _“Which students scored above 90?”_ and it shoots SQL behind the scenes — no sweat, no syntax errors.

- 💾 Works with both **SQLite (`student.db`)** and your own **MySQL database**
- 🧠 Powered by **LLaMA-3.3-70B** (via **Groq**) — ultra fast ⚡
- 🎨 Clean, chat-style UI built using Streamlit
- 🛠️ LangChain handles all the SQL conversion magic
- 📂 All logic lives in `app.py`

---

## 🧠 Setup

### 📁 1. Clone & Navigate
```bash
git clone https://github.com/your-username/SQLAgent.git
cd SQLAgent
```

### 🐍 2. Create a Virtual Environment (Recommended)
```bash
# Create venv
python -m venv venv

# Activate venv
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

### 📦 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 🗝️ 4. Add your API Key
Create a `.env` file in the root directory and add your [Groq](https://console.groq.com/) API key:
```env
GROQ_API_KEY=your_groq_key_here
```

---

## 💻 Running the App

```bash
streamlit run app.py
```

Then head over to: [http://localhost:8501](http://localhost:8501)

---

## 📐 Using the App

### 🧩 Step 1: Choose Your DB

Use the sidebar to select:
- `Sqlite3 - student.db` — a local `.db` file for quick testing
- OR
- `Connect to your SQL database` — enter your MySQL creds live

### 🔌 Step 2: For MySQL
You'll be prompted to input:
- Host (e.g., `localhost:<PORTNUMBER>`)
- Username (e.g., `root`)
- Password
- Database name

> 🧠 All handled securely inside the Streamlit session.

---

## 📝 Example Queries

```bash
🧠 "List all students who passed"
📊 "What is the average score in each subject?"
📅 "How many users signed up last month?"
```

LangChain + Groq turn these into raw SQL, run them, and summarize results for you. Magic.

---

## 📦 `requirements.txt`

```txt
mysql-connector-python
SQLAlchemy
streamlit
langchain
langchain_community
langchain_groq
dotenv
```

---

## 🔥 Future Upgrades You Could Build

- Add session memory / context retention
- Enable CSV download of query results
- Drop-in dark mode with theming
- Hook into more LLM providers (e.g. Claude, Gemini)

---

## 🛠️ Tech Stack

- 🧠 LLaMA 3.3 - 70B via Groq
- 🔗 LangChain Agents
- 📊 SQLAlchemy + MySQL/SQLite
- 🎨 Streamlit UI
- 🔐 `.env`-based API key loading

---

## 👾 Built for Devs Who'd Rather Chat Than Code SQL

🦙 x 💬 x 💡 = 🧠

---
