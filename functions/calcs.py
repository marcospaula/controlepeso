import datetime as dt

#Função para obter o status do imc (bmi em inglês)
def get_status(bmi):
    if bmi < 18.5:
        return 'Abaixo do peso'
    elif bmi < 25:
        return 'Peso normal'
    elif bmi < 30:
        return 'Sobrepeso'
    elif bmi < 35:
        return 'Obesidade grau 1'
    elif bmi < 40:
        return 'Obesidade grau 2'
    else:
        return 'Obesidade grau 3'

# Função para calcular o IMC
def get_BMI(weight, height):
    if height == 0:
        return 0
    return weight / height**2

# Função para calcular a idade a partir da data de nascimento
def get_age(birthdate):
    # Recupera a data atual
    today = dt.date.today()
    # Calcula a idade considerando o ano atual e o ano de nascimento
    age = today.year - birthdate.year
    # Verifica se o aniversário já passou no ano atual
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

# Função para calcular a data de nascimento a partir da idade
def get_birthdate(age):
    # Recupera a data atual
    today = dt.date.today()
    # Calcula o ano de nascimento
    birthdate = today.year - age
    # Converte para formato de data
    birthdate = dt.date(birthdate, 1, 1)
    # Formata a data de nascimento no formato DD/MM/YYYY
    # birthdate = birthdate.strftime("%d/%m/%Y")
    return birthdate