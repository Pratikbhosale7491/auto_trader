# 🧠 Auto Trader – Automated Stock Trading Bot

Auto Trader is an intelligent stock trading bot that automatically executes buy/sell trades based on predefined strategies and live market data. 
This project was built to simulate algorithmic trading using technical indicators, decision logic, and automation workflows.

---

## 🚀 Features

- 📈 Monitors real-time stock price data
- ⚙️ Executes trades based on defined rules (buy/sell thresholds)
- 📊 Uses APIs for market data and trade execution
- 🔁 Runs continuously with auto-restart support
- 📩 Sends alerts on executed trades (via terminal/Telegram)
- 🐳 Dockerized for easy deployment

---

## 🛠️ Tech Stack

- **Language:** Python - FastAPI
- **API Provider:** Angle One 
- **Automation:** Docker, GitHub Actions
- **Infrastructure:** AWS EC2 (Ubuntu)
- **Monitoring:** Bash scripts, optional Prometheus & Grafana

---

## 📁 Project Structure
   auto_trader/
├── main.py # Entry point of the bot
├── config.json # Strategy parameters & symbols
├── strategies/ # Custom trading logic
├── utils/ # Helper functions (indicators, logging)
├── Dockerfile # Containerization setup
└── README.md # Project documentation

 

  

  

