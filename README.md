# Smart AI Trip Planner 🌍✈️

An AI-powered trip planning system that generates personalized travel itineraries using a local LLM (Mistral via Ollama) and a modular tool-based architecture.

---

## 🚀 Features

- 🧠 AI-generated 2–3 day travel itineraries  
- 📍 Dynamic city extraction from user input  
- 🏨 Hotel recommendations (tool-based)  
- 🌦 Weather information (simulated/tool-based)  
- 🔍 Place suggestions using DuckDuckGo Search (ddgs)  
- ⚡ Runs locally — no API cost required  

---

## 🏗️ Tech Stack

- Python  
- LangChain  
- Ollama (Mistral LLM)  
- DuckDuckGo Search (`ddgs`)  

---

## 📂 Project Structure
SmartTripAI/
│── main.py
│── requirements.txt
│── README.md
│── agent/
│ ├── planner.py
│ ├── travel_tools.py
│ ├── travel_utils.py
│ └── init.py

## ⚙️ Setup & Run

### 1. Clone the repository

git clone https://github.com/Vaibhavats/SmartTripAI.git

cd SmartTripAI


### 2. Create virtual environment

python -m venv venv
source venv/bin/activate


### 3. Install dependencies

pip install -r requirements.txt


### 4. Run the project

python main.py


---

## 💡 Example Usage


Enter your trip: plan a trip to Goa


### Output includes:
- Day-wise itinerary  
- Suggested hotels  
- Weather overview  
- Places to visit  

---

## 🧠 How It Works

1. User input is parsed to extract the destination city  
2. Tools fetch:
   - Hotels  
   - Weather  
   - Places  
3. The LLM (Mistral via Ollama) generates a structured itinerary  

---

## 🔮 Future Improvements

- 🌐 Real-time API integration (OpenWeather, Geoapify)  
- 🎨 Web UI using Streamlit  
- 💰 Budget-based trip planning  
- 📅 Date-based planning  

---

## ⚠️ Note

This project currently uses simulated tool outputs for stability and offline execution. It is designed to be easily extended with real APIs.

---

## 👨‍💻 Author

**Vaibhav Kumar**  
GitHub: https://github.com/Vaibhavats
