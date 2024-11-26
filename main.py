import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Configura la pagina
st.set_page_config(
    page_title="Dashboard Apple Style",
    page_icon="🍎",
    layout="wide",
)

# CSS personalizzato migliorato
# CSS personalizzato migliorato
st.markdown("""
    <style>
    /* Sfondo generale */
    body {
        background-color: #fefefe;
        color: #333333;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    /* Sidebar */
    .css-1d391kg {
        background-color: #f9f9f9;
        border-right: 1px solid #eaeaea;
    }

    /* Input nella sidebar */
    .css-1d391kg .stDateInput {
        width: 100%;
        max-width: 95%;
        margin: auto;
    }
    .css-1d391kg input {
        width: 100%;
        max-width: 95%;
    }

    /* Pulsanti */
    .stButton>button {
        background-color: #0071e3;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #005bb5;
    }
    </style>
""", unsafe_allow_html=True)


# Intestazione
st.markdown("""
    <div style="text-align: center; padding: 20px; background-color: #0071e3; color: white; border-radius: 10px; margin-bottom: 20px;">
        <h1>Dashboard Yahoo Finance Apple</h1>
        <p>Analizza i dati finanziari con un design minimal e intuitivo.</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar - Input utente
st.sidebar.title("Impostazioni")
ticker_symbol = st.sidebar.text_input("Simbolo del titolo azionario (es. AAPL, TSLA):", "AAPL")

st.sidebar.write("Seleziona l'intervallo temporale:")
start_date = st.sidebar.date_input("Data di inizio", pd.to_datetime("2010-01-01"))
end_date = st.sidebar.date_input("Data di fine", pd.to_datetime("2023-01-01"))

# Scarica i dati da Yahoo Finance
if st.sidebar.button("Carica dati"):
    try:
        # Dati finanziari
        ticker_data = yf.Ticker(ticker_symbol)
        ticker_df = ticker_data.history(period="1d", start=start_date, end=end_date)

        # Layout principale
        st.subheader(f"Dati finanziari di {ticker_symbol}")
        col1, col2 = st.columns([2, 1])

        # Grafici
        with col1:
            # Grafico del prezzo di chiusura
            st.write("**Prezzo di chiusura**")
            fig_close = go.Figure(
                data=go.Scatter(x=ticker_df.index, y=ticker_df['Close'], line=dict(color="#0071e3"))
            )
            fig_close.update_layout(template="plotly_white", margin=dict(l=0, r=0, t=30, b=20))
            st.plotly_chart(fig_close, use_container_width=True)

            # Grafico a candele
            st.write("**Grafico Candlestick**")
            fig_candlestick = go.Figure(
                data=[go.Candlestick(
                    x=ticker_df.index,
                    open=ticker_df['Open'],
                    high=ticker_df['High'],
                    low=ticker_df['Low'],
                    close=ticker_df['Close']
                )]
            )
            fig_candlestick.update_layout(template="plotly_white", margin=dict(l=0, r=0, t=30, b=20))
            st.plotly_chart(fig_candlestick, use_container_width=True)

        # Tabella
        with col2:
            st.write("**Dati grezzi**")
            st.dataframe(ticker_df, use_container_width=True)

        # Esportazione dati
        csv = ticker_df.to_csv(index=True)
        st.download_button(
            label="Scarica i dati in formato CSV",
            data=csv,
            file_name=f"{ticker_symbol}_data.csv",
            mime="text/csv",
        )

    except Exception as e:
        st.error("Errore durante il caricamento dei dati. Controlla il simbolo o le date.")
