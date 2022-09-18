import pywhatkit
import streamlit as st
import pandas as pd
import time


st.markdown(
    """
    <h1 style='text-align: center; margin-bottom: -35px;'>
    Convocação de Candidatos - Censo 2022
    </h1>
    """
    , unsafe_allow_html=True
    )

st.write("#")
st.write("#")

telefones_xls = st.file_uploader('Selecione o arquivo Excel com os telefone', type=['csv'])

st.write("##")


if telefones_xls is not None:
    df = pd.read_csv(telefones_xls, dtype={'telefones':'object'}, sep=';')
    st.write(df)

st.write("#")
st.write("#")


p = st.empty()

if (telefones_xls is not None) & st.button('Enviar Mensagens'):
    time.sleep(30)
    for row in df.itertuples():

        # TESTAR SE O NÚMERO DE TELEFONE ESTÁ CORRETO. PARA TANTO UM PRIMEIRO PASSO É O REGEX ^\+55$
        
        st.write(f'{row[0]+1}º contato')
        row[1]
        pywhatkit.sendwhatmsg_instantly(
            row[1]
            , f'Teste de envio de mensagem do whatsapp por comando Python para {row[2]}.'
            , tab_close=True
        )
        time.sleep(1)
        p.empty()


# IMPLEMENTAR UM REGISTRO DE LOG PARA SABER QUAIS OS TELEFONES FORAM CONTATADOS
# IMPLEMENTAR ERROR HANDLING



