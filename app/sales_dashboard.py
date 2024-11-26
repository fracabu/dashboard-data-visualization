import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Configura la pagina
st.set_page_config(page_title="Dashboard Vendite (API)", layout="wide")

# Titolo della dashboard
st.title("Dashboard delle Vendite con Dati API")
st.write("Analizza i dati delle vendite recuperati in tempo reale da un'API.")

# URL dell'API (modifica con il tuo indirizzo API se ospitata su un server)
api_url = "http://127.0.0.1:5000/api/vendite"  # API locale

# Recupera i dati dall'API
st.write("Recupero dati dall'API in corso...")
response = requests.get(api_url)

if response.status_code == 200:
    # Converti i dati JSON in un DataFrame
    data = pd.DataFrame(response.json())
    data["Data"] = pd.to_datetime(data["Data"])

    st.success("Dati caricati con successo!")
    st.write("Ecco i dati recuperati:")
    st.dataframe(data)

    # Filtri interattivi
    st.sidebar.subheader("Filtri")
    categoria = st.sidebar.multiselect("Seleziona la categoria:", options=data["Categoria"].unique(), default=data["Categoria"].unique())
    regione = st.sidebar.multiselect("Seleziona la regione:", options=data["Regione"].unique(), default=data["Regione"].unique())
    data_inizio = st.sidebar.date_input("Data di inizio:", data["Data"].min())
    data_fine = st.sidebar.date_input("Data di fine:", data["Data"].max())

    # Filtra i dati
    dati_filtrati = data[
        (data["Categoria"].isin(categoria)) &
        (data["Regione"].isin(regione)) &
        (data["Data"] >= pd.to_datetime(data_inizio)) &
        (data["Data"] <= pd.to_datetime(data_fine))
    ]

    st.write("Dati filtrati:")
    st.dataframe(dati_filtrati)

    # Grafico delle vendite totali nel tempo
    st.subheader("Vendite totali nel tempo")
    vendite_tempo = dati_filtrati.groupby("Data")["Vendite"].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=vendite_tempo, x="Data", y="Vendite", ax=ax)
    ax.set_title("Andamento delle vendite nel tempo")
    st.pyplot(fig)

    # Distribuzione delle vendite per regione
    st.subheader("Distribuzione delle vendite per regione")
    vendite_regione = dati_filtrati.groupby("Regione")["Vendite"].sum().reset_index()
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(data=vendite_regione, x="Regione", y="Vendite", ax=ax2)
    ax2.set_title("Vendite per regione")
    st.pyplot(fig2)
    
    

    # Esportazione dei dati filtrati
    st.download_button(
        label="Scarica i dati filtrati in CSV",
        data=dati_filtrati.to_csv(index=False).encode("utf-8"),
        file_name="vendite_filtrate.csv",
        mime="text/csv"
    )
else:
    st.error("Errore nel recupero dei dati dall'API. Controlla il server.")
# Distribuzione delle vendite per categoria (grafico a torta)
st.subheader("Distribuzione delle vendite per categoria")
fig3, ax3 = plt.subplots()
vendite_categoria = dati_filtrati.groupby("Categoria")["Vendite"].sum()
ax3.pie(vendite_categoria, labels=vendite_categoria.index, autopct='%1.1f%%', startangle=90)
ax3.axis("equal")  # Assicura che il grafico sia circolare
st.pyplot(fig3)
