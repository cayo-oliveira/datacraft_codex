# 📊 DataCraft: Redundância em Data Mesh com Isomorfismo de Grafos

DataCraft é uma ferramenta desenvolvida para detectar estruturas redundantes em arquiteturas distribuídas de dados utilizando técnicas de isomorfismo de grafos. Ideal para cenários inspirados em Data Mesh.

---

## 📦 Estrutura

```
DataCraft/
├── algoritmos/              # Algoritmos de detecção (VF2, Node Match)
├── avaliacao/               # Cálculo de ACC, ERR, ET, ETT
├── geradores/               # Geração de grafos benchmark (TPC-DS)
├── validacao/               # Geração e salvamento de pares reais
├── visualizacao/            # Plotagem de grafos e métricas
├── data/                    # Grafos em formato .gml
├── predicted_pairs/         # Saídas dos algoritmos
├── validations/             # Pares validados (automáticos ou manuais)
├── main.py                  # Interface Streamlit
├── requirements.txt         # Dependências
└── README.md
```

---

## ▶️ Como Executar Localmente

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/DataCraft.git
cd DataCraft
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute o aplicativo Streamlit:
```bash
streamlit run main.py
```

---

## 🌐 Como Executar no Streamlit Cloud

1. Faça login em [streamlit.io](https://streamlit.io/)
2. Crie um novo app e conecte seu repositório GitHub com o projeto
3. Aponte para o arquivo `main.py` como entry point
4. Pronto!

---

## 🧠 Tecnologias Utilizadas

- Python
- Streamlit
- NetworkX
- Pandas
- Matplotlib / Seaborn
- SciPy

---

## ✍️ Autor

Desenvolvido por **Cayo de Oliveira** como parte de uma pesquisa sobre detecção de redundância estrutural em Data Mesh utilizando grafos.

---