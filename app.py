import streamlit as st
import datetime as dt

import functions.ai as ai
import functions.calcs as calcs
import functions.df as df

# Criando valores iniciais
name = ""
sex = ""
weight = 0.0
height = 0.0
birthdate = dt.date(1990, 1, 1)  # Ou qualquer valor válido
history = "Descreva algo sobre você, coisas que você gosta, coisas que você não gosta, seus hábitos alimentares e de atividade física"

# Cabeçalho da página
st.title("Cuide de sua saúde")
st.subheader("Dicas de saúde e controle de peso")
st.write("Preencha os campos abaixo para receber dicas personalizadas de saúde e controle de peso.")

# Nome ou exemplo
name = st.selectbox("Nome", df.get_persons(), accept_new_options=True)

# Carregando os dados do exemplo
if name != "(digite seu nome ou selecione um exemplo)":
    example = df.get_person(name)
    if example is not None and example.notna().all():
        name = example["name"]
        sex = example['sex']
        weight = float(example['weight'])
        height = float(example['height'])
        birthdate = calcs.get_birthdate(example['age'])
        history = example['history']
    
# Input do usuário
c1, c2, c3, c4 = st.columns(4)
sex = c1.text_input("Sexo", value=sex)
weight = c2.number_input("Peso (kg)", min_value=0.0, format="%.0f", value=weight)
height = c3.number_input("Altura (m)", min_value=0.0, format="%.2f", value=height)
birthdate = c4.date_input("Data de nascimento", format="DD/MM/YYYY", value=birthdate)
history = st.text_area("Hábitos", height=150, value=history)

# Calculando idade, IMC e status
age = calcs.get_age(birthdate)
bmi = calcs.get_BMI(weight, height)
status = calcs.get_status(bmi)

# Preparando o conteúdo para o modelo
content = ai.prep_content(name, sex, age, weight, height, bmi, status, history)

# Botão para enviar o conteúdo
if st.button("Enviar"):
    
    # Outputs
    s1, s2 = st.columns(2)
    s1.metric("Idate (anos)", age, border=True)
    s2.metric("IMC", f"{bmi:.2f}", border=True)
    st.write("Status do IMC:", status)

# Enviando o conteúdo para o modelo
with st.spinner("Processando..."):
    result = ai.submit(content)
    st.subheader("Dicas de saúde e controle de peso")
    st.write(result)