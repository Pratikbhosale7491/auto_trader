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

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/auto_trader.git
cd auto_trader

2. Install dependencies

pip install -r requirements.txt

3. Configure your API keys
Edit the config.json or .env file to include:

API key

Secret key

Trade symbols

Buy/sell threshold values

4. Run the bot
 
python main.py

5. Run with Docker (optional)
 
docker build -t auto-trader .
docker run -d auto-trader

📬 Alerts (Optional)
You can integrate with Telegram or Email for trade notifications.

📌 Disclaimer
This project is for educational purposes only. It does not execute real money trades unless integrated with a live trading API. Use with caution.


🧑‍💻 Author
Pratik Bhosale
LinkedIn :- http://www.linkedin.com/in/pratikbhosale00


  

  

