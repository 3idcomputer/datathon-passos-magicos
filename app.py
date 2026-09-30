import streamlit as st
import pickle
import numpy as np
from pathlib import Path

st.set_page_config(page_title="Passos Mágicos - Risco de Defasagem", page_icon="🪄", layout="wide")

@st.cache_resource
def carregar_modelo():
    with open(Path("models")/"modelo_risco.pkl","rb") as f:
        return pickle.load(f)

modelo = carregar_modelo()

st.title("🪄 Passos Mágicos - Predição de Risco de Defasagem")
st.caption("Datathon PosTech - modelo preditivo com indicadores educacionais do PEDE")

st.info("A probabilidade é um apoio à priorização de acompanhamento e não substitui a avaliação pedagógica e psicossocial.")

c1,c2,c3 = st.columns(3)
with c1:
    ian=st.slider("IAN - Adequação de nível",0.0,10.0,7.0,0.1)
    ida=st.slider("IDA - Desempenho acadêmico",0.0,10.0,6.5,0.1)
    ieg=st.slider("IEG - Engajamento",0.0,10.0,8.0,0.1)
with c2:
    iaa=st.slider("IAA - Autoavaliação",0.0,10.0,8.0,0.1)
    ips=st.slider("IPS - Psicossocial",0.0,10.0,6.5,0.1)
with c3:
    ipv=st.slider("IPV - Ponto de virada",0.0,10.0,7.5,0.1)
    inde=st.slider("INDE - Índice global",0.0,10.0,7.0,0.1)

x=np.array([[ian,ida,ieg,iaa,ips,ipv,inde]],dtype=float)
p=float(modelo.predict_proba(x)[0,1])

st.divider()
st.metric("Probabilidade estimada de risco no próximo ano", f"{p*100:.1f}%")
if p >= .65:
    st.error("Prioridade alta para acompanhamento.")
elif p >= .40:
    st.warning("Prioridade intermediária para acompanhamento.")
else:
    st.success("Risco estimado mais baixo no perfil informado.")

st.subheader("Como interpretar")
st.write("O modelo foi treinado com dados longitudinais: indicadores de um ano são usados para prever se o aluno estará em defasagem no ano seguinte.")
