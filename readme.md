# 🎯 Complete Dashboard Premium

> 📊 Un dashboard interattivo per esplorare, analizzare e visualizzare i dati in modo semplice e intuitivo!

Questa applicazione combina la potenza di **Streamlit** ⚡ per creare dashboard interattive con un'API Flask deployata su **Render** 🚀 per fornire dati simulati o reali in tempo reale. È progettata per offrire una soluzione completa per l'analisi e la visualizzazione dei dati.

---
![image](https://github.com/user-attachments/assets/a26880e7-e1fb-45c2-b03d-4f50b8252f64)

![image](https://github.com/user-attachments/assets/7521c4cb-a535-4b9b-bb2c-be9ce8f7273b)

![image](https://github.com/user-attachments/assets/00d4a42e-ff86-4a27-83a7-fb7bf39a60e6)




## 🏗️ Struttura del Progetto

```plaintext
dashboard-data-visualization/
├── app/                  # Moduli principali dell'app
│   ├── __init__.py       # Rende la cartella un pacchetto Python
│   ├── api.py            # Gestisce chiamate all'API Flask
│   ├── utils.py          # Funzioni di utilità generiche
│   └── visualizations.py # Funzioni per generare grafici e visualizzazioni
├── main.py               # File principale per l'esecuzione dell'app Streamlit
├── .streamlit/           # Configurazioni personalizzate per Streamlit
│   └── config.toml       # Impostazioni del tema e altri parametri
├── .vscode/              # Configurazioni per Visual Studio Code
├── venv/                 # Ambiente virtuale Python
├── requirements.txt      # Dipendenze del progetto
├── runtime.txt          # Specifica la versione di Python (per Streamlit Cloud/Render)
├── .gitignore           # File per escludere elementi dal repository
├── readme.md            # Documentazione del progetto
└── tests/               # Directory per i test
    └── test_api.py      # Test per verificare il funzionamento dell'API Flask
```

---

## ✨ Funzionalità

### 🎨 **Dashboard Interattivo (Streamlit)**
- **Visualizzazioni dinamiche**: Grafici come istogrammi, grafici a barre, scatter plot e mappe di correlazione
- **Filtraggio avanzato**: Filtri per colonne numeriche e testuali
- **Esportazione dati**: Scarica i dati filtrati in formato CSV o Excel
- **Tema personalizzabile**: Alterna tra tema chiaro e scuro

### 🔌 **API Flask**
- **Endpoint API**: Un'API semplice per simulare dataset o recuperare dati reali
- **Dataset medico simulato**: Utilizzato per testare le funzionalità dell'app
- **Hosting su Render**: L'API è stata deployata su Render per accesso pubblico continuo

---

## 🚀 Deployment

### 🌐 **Dashboard Streamlit**
L'app è stata deployata su **Streamlit Cloud**, rendendola accessibile online 24/7.

Link al dashboard:  
**[Accedi al Dashboard Interattivo](https://tuo-link-all-app.streamlit.app)** 🔗

### ⚙️ **API Flask**
L'API è ospitata su **Render** e fornisce i dati utilizzati dal dashboard per le visualizzazioni e l'analisi.

Link API Render:  
**[Accedi all'API Flask](https://tuo-api-deploy-su-render.com)** 🔗

---

## 💻 Requisiti Tecnici

- **Browser**: Chrome 🌐, Firefox 🦊, Edge 🌊 o Safari 🧭
- **Python Version**: Specificata in `runtime.txt` (ad esempio, `python-3.9`)
- **File Supportati**: CSV con una struttura predefinita

---

## 🛠️ Installazione Locale

Per eseguire l'app in locale, segui questi passaggi:

1. **Clona il repository**:
   ```bash
   git clone https://github.com/tuo-repo/dashboard-data-visualization.git
   cd dashboard-data-visualization
   ```

2. **Crea un ambiente virtuale**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Su Windows: venv\Scripts\activate
   ```

3. **Installa le dipendenze**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Esegui il dashboard**:
   ```bash
   streamlit run main.py
   ```

---

## 🔮 Funzionalità Future

- 📁 Supporto per dataset generici, indipendentemente dalla struttura
- 📊 Importazione di file in formati Excel e JSON
- 🎯 Mappatura personalizzabile delle colonne per adattarsi a dataset generici
- 🔄 Estensione delle API per supportare più endpoint e dataset reali

---

## 🚦 Configurazione Sviluppo Locale

### **1. Primo Terminale: Avvia il Server Flask** 🖥️
1. Apri un terminale e spostati nella directory del progetto:
   ```bash
   cd dashboard-data-visualization
   ```
2. Attiva l'ambiente virtuale:
   ```bash
   venv\Scripts\activate
   ```
3. Avvia il server Flask:
   ```bash
   python api_premium.py
   ```
4. **Lascia questo terminale aperto** con il server in esecuzione.

---

### **2. Secondo Terminale: Avvia la Dashboard Streamlit** 📊
1. Apri un secondo terminale e spostati nella directory del progetto:
   ```bash
   cd dashboard-data-visualization
   ```
2. Attiva l'ambiente virtuale:
   ```bash
   venv\Scripts\activate
   ```
3. Avvia la dashboard Streamlit:
   ```bash
   streamlit run main.py
   ```
4. Il dashboard sarà accessibile su [http://localhost:8501](http://localhost:8501) 🌐

---

Se hai domande o richieste di personalizzazione, non esitare a contattarmi! 💌


# 🎯 Complete Dashboard Premium

> 📊 An interactive dashboard for exploring, analyzing, and visualizing data in a simple and intuitive way!

This application combines the power of **Streamlit** ⚡ for creating interactive dashboards with a Flask API deployed on **Render** 🚀 to provide real-time simulated or real data. It's designed to offer a complete solution for data analysis and visualization.

---

## 🏗️ Project Structure

```plaintext
dashboard-data-visualization/
├── app/                  # Main app modules
│   ├── __init__.py       # Makes the folder a Python package
│   ├── api.py            # Handles Flask API calls
│   ├── utils.py          # Generic utility functions
│   └── visualizations.py # Functions for generating charts and visualizations
├── main.py               # Main file for Streamlit app execution
├── .streamlit/           # Custom Streamlit configurations
│   └── config.toml       # Theme settings and other parameters
├── .vscode/              # Visual Studio Code configurations
├── venv/                 # Python virtual environment
├── requirements.txt      # Project dependencies
├── runtime.txt          # Python version specification (for Streamlit Cloud/Render)
├── .gitignore           # File to exclude items from repository
├── readme.md            # Project documentation
└── tests/               # Tests directory
    └── test_api.py      # Tests to verify Flask API functionality
```

---

## ✨ Features

### 🎨 **Interactive Dashboard (Streamlit)**
- **Dynamic Visualizations**: Histograms, bar charts, scatter plots, and correlation maps
- **Advanced Filtering**: Filters for numeric and text columns
- **Data Export**: Download filtered data in CSV or Excel format
- **Customizable Theme**: Toggle between light and dark theme

### 🔌 **Flask API**
- **API Endpoints**: A simple API for simulating datasets or retrieving real data
- **Simulated Medical Dataset**: Used for testing app functionality
- **Render Hosting**: API deployed on Render for continuous public access

---

## 🚀 Deployment

### 🌐 **Streamlit Dashboard**
The app has been deployed on **Streamlit Cloud**, making it accessible online 24/7.

Dashboard link:  
**[Access Interactive Dashboard](https://tuo-link-all-app.streamlit.app)** 🔗

### ⚙️ **Flask API**
The API is hosted on **Render** and provides the data used by the dashboard for visualizations and analysis.

Render API link:  
**[Access Flask API](https://tuo-api-deploy-su-render.com)** 🔗

---

## 💻 Technical Requirements

- **Browser**: Chrome 🌐, Firefox 🦊, Edge 🌊 or Safari 🧭
- **Python Version**: Specified in `runtime.txt` (e.g., `python-3.9`)
- **Supported Files**: CSV with predefined structure

---

## 🛠️ Local Installation

Follow these steps to run the app locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tuo-repo/dashboard-data-visualization.git
   cd dashboard-data-visualization
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the dashboard**:
   ```bash
   streamlit run main.py
   ```

---

## 🔮 Future Features

- 📁 Support for generic datasets, regardless of structure
- 📊 Excel and JSON file import support
- 🎯 Customizable column mapping to adapt to generic datasets
- 🔄 Extended APIs to support more endpoints and real datasets

---

## 🚦 Local Development Setup

### **1. First Terminal: Launch Flask Server** 🖥️
1. Open a terminal and navigate to the project directory:
   ```bash
   cd dashboard-data-visualization
   ```
2. Activate the virtual environment:
   ```bash
   venv\Scripts\activate
   ```
3. Start the Flask server:
   ```bash
   python api_premium.py
   ```
4. **Keep this terminal open** with the server running.

---

### **2. Second Terminal: Launch Streamlit Dashboard** 📊
1. Open a second terminal and navigate to the project directory:
   ```bash
   cd dashboard-data-visualization
   ```
2. Activate the virtual environment:
   ```bash
   venv\Scripts\activate
   ```
3. Start the Streamlit dashboard:
   ```bash
   streamlit run main.py
   ```
4. The dashboard will be accessible at [http://localhost:8501](http://localhost:8501) 🌐

---

If you have any questions or customization requests, don't hesitate to contact me! 💌

### **1. Primo Terminale: Avvia il Server Flask**
1. Apri un terminale e spostati nella directory del progetto:
   ```bash
   cd dashboard-data-visualization
   ```
2. Attiva l'ambiente virtuale:
   ```bash
   venv\Scripts\activate
   ```
3. Avvia il server Flask:
   ```bash
   python api_premium.py
   ```
4. **Lascia questo terminale aperto** con il server in esecuzione.

---

### **2. Secondo Terminale: Avvia la Dashboard Streamlit**
1. Apri un secondo terminale e spostati nella directory del progetto:
   ```bash
   cd dashboard-data-visualization
   ```
2. Attiva l'ambiente virtuale (può essere attivato in più terminali contemporaneamente):
   ```bash
   venv\Scripts\activate
   ```
3. Avvia la dashboard Streamlit:
   ```bash
   streamlit run main.py (sostituire con il py della dashboard da deployare)
   ```
4. La dashboard sarà accessibile su [http://localhost:8501](http://localhost:8501).



