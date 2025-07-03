from openai import OpenAI
import streamlit as st

# Cliente OpenAI
API_KEY = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=API_KEY)

# Instruções para o modelo
instructions = """
Você é um assistente virtual que ajuda a melhorar a saúde das pessoas. 
Você receberá uma série de informações de uma pessoa, como peso, altura, idade e sexo. 
Também receberá um texto sobre o perfil da pessoa, suas características, hábitos e momento de vida. 
Com base nessas informações, você deve fornecer dicas de saúde e controle de peso para a pessoa. 
As dicas devem ser personalizadas e relevantes para o perfil da pessoa. 
Seja positivo, motivador e empático ao fornecer as dicas, valorize as conquistas da pessoa.
Escreva as dicas em um único parágrafo com aproximadamente 400 caracteres.
"""

# Contatena o conteúdo para o prompt
def prep_content(name, sex, age, weight, height, bmi, status, history):
    content = 'Nome: ' + name + ', '
    content += 'Sexo: ' + sex + ', '
    content += 'Idade: ' + str(age) + ', '
    content += 'Peso: ' + str(weight) + ', '
    content += 'Altura: ' + str(height) + ', '
    content += 'IMC: ' + str(bmi) + ','
    content += 'Status: ' + status + ', '
    content += 'Histórico: ' + history
    return content

# Submete o prompt ao modelo
def submit(content):

    # Prepara a requisição (prompt)
    messages = []
    messages.append({"role": "system", "content": instructions})
    messages.append({"role": "user", "content": content})   

    # Envia a solicitação para o modelo    
    response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    result = response.choices[0].message.content

    return result