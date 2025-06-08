import streamlit as st
from geradores.tpcds_generator import build_tpcds_graph_scenario
from algoritmos.executor_isomorfismo import run_isomorphism
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="DataCraft - Redundância em Data Mesh", layout="wide")

st.title("🔎 DataCraft: Detecção de Redundância em Arquiteturas Data Mesh")

st.sidebar.header("Parâmetros da Geração")
sor = st.sidebar.selectbox("Número de SORs", [2, 4, 8, 16])
domain = st.sidebar.selectbox("Número de Domínios", [1, 2, 3, 4, 5])
seed = st.sidebar.number_input("Seed", value=42)

if st.sidebar.button("Gerar Grafo"):
    G = build_tpcds_graph_scenario(sor_count=sor, domain_count=domain, seed=seed, save_gml=False)
    st.success("Grafo gerado com sucesso!")
    pos = nx.spring_layout(G, seed=seed)
    node_colors = ['gray' if G.nodes[n]['type'] == 'SOR' else 'skyblue' if G.nodes[n]['type'] == 'SOT' else 'green' for n in G.nodes]
    fig, ax = plt.subplots(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color=node_colors, ax=ax, node_size=800, font_size=8)
    st.pyplot(fig)

    st.subheader("🔬 Algoritmo de Isomorfismo")
    algorithm = st.selectbox("Escolha o algoritmo", ["VF2", "Node Match (Custom)"])

    if st.button("Executar Isomorfismo"):
        pairs = run_isomorphism(G, algorithm=algorithm)
        st.write(f"🔗 Pares isomórficos detectados ({len(pairs)}):")
        st.json(pairs)