# Datathon - Passos Mágicos

Projeto desenvolvido para o Datathon da Pós-Tech, com análise dos indicadores PEDE de 2022, 2023 e 2024 e modelo de Machine Learning para risco de defasagem.

## Estrutura
- `app.py`: aplicação Streamlit
- `notebooks/datathon_passos_magicos.ipynb`: análise e modelagem
- `models/modelo_risco.pkl`: modelo treinado
- `models/metricas.json`: métricas
- `data/dataset_modelo_longitudinal.csv`: base longitudinal preparada

## Estratégia preditiva
Para reduzir vazamento de informação, os indicadores do ano **t** predizem se o aluno estará em defasagem no ano **t+1**.

Treino: 2022 -> 2023 (600 transições)  
Teste temporal: 2023 -> 2024 (765 transições)

### Resultado do Random Forest
- Accuracy: 0.705
- Precision: 0.660
- Recall: 0.549
- F1: 0.599
- ROC-AUC: 0.741

## Rodar localmente
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy no Streamlit Community Cloud
1. Suba esta pasta em um repositório GitHub.
2. Entre no Streamlit Community Cloud.
3. Selecione o repositório.
4. Arquivo principal: `app.py`.
5. Faça o deploy.

## Observação
O modelo deve ser utilizado como ferramenta de apoio à priorização de acompanhamento, não como decisão automática sobre o aluno.
