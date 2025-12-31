import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Agro Intelligence", layout="wide")

st.title("🌱 Dashboard de Inteligência Agro")

# === Carregar planilha ===
arquivo = "Matriz_APIs_AGROINSIGHTS_Organizada - MODELO 11-12.xlsx"

df_fin = pd.read_excel(arquivo, sheet_name="11. Viabilidade Financeira")
df_prod = pd.read_excel(arquivo, sheet_name="5. Potencial Produtivo")
df_risco = pd.read_excel(arquivo, sheet_name="12. Matriz Riscos")

# === Função para puxar preço de commodities ===
def preco_commodity(ticker):
    url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={ticker}"
    r = requests.get(url).json()
    return r["quoteResponse"]["result"][0]["regularMarketPrice"]

preco_milho = preco_commodity("ZC=F")
preco_soja = preco_commodity("ZS=F")

# === Visão Geral ===
st.header("📊 Visão Geral")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Registos Financeiros", len(df_fin))

with col2:
    st.metric("Registos Produtivos", len(df_prod))

with col3:
    st.metric("Riscos Mapeados", len(df_risco))

st.divider()

# === Mercado ===
st.header("🌽 Mercado")

col1, col2 = st.columns(2)

with col1:
    st.metric("Milho (CBOT)", f"US$ {preco_milho}")

with col2:
    st.metric("Soja (CBOT)", f"US$ {preco_soja}")

# === Insight ===
st.divider()
st.header("🧠 Insight Inteligente")

custo_racao = 72  # valor inicial (pode vir da planilha depois)

if preco_milho > custo_racao * 1.1:
    st.warning("⚠️ Preço do milho acima do custo base da ração.")
else:
    st.success("✅ Custo de ração sob controle.")
