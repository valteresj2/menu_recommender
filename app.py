#from bardapi import BardCookies,Bard
#cookie_dict = {
#    "__Secure-1PSID": "cwhfXPk9Wp16QA1k4E0JHQH9SAsH6ULsqFBrvJf97a1-Kjw4xKvvHEH-Iuf9WPAf22ZHPw.",
#    "__Secure-1PSIDTS": "sidts-CjEBNiGH7qX0_i1F77u70nZVl9AisrZAQu18Llc1KI8lCvnZK7FLb3xN2z3LA5cbPyB_EAA",
#    
#}
#bard = Bard(token_from_browser=True)
#bard = BardCookies(cookie_dict=cookie_dict,language='pt')

#path='C:/Users/valteresj/Desktop'
#image = open(path+'/Menu.jpg', 'rb').read()



#bard_answer = bard.ask_about_image('Hoje que gastar apenas R$ 30 e comer uma tilapia, qual prato você me recomenda?', image)



#Prompt=bard_answer['content']

#ask_user='\n\n Gostaria de almoçar e só posso gastar até R$ 35, porém gostaria de comer filé mion com fritas, qual prato você me recomenda?'

#Prompt=Prompt+ask_user

#bard.get_answer(Prompt)['content']
from tempfile import NamedTemporaryFile
import streamlit as st
from bardapi import BardCookies,Bard
#from langchain.chat_models import ChatOpenAI
#from langchain.chains.conversation.memory import ConversationBufferWindowMemory

def click_button():
    st.session_state.clicked = True


cookie_dict = {
    "__Secure-1PSID": "cwhfXPk9Wp16QA1k4E0JHQH9SAsH6ULsqFBrvJf97a1-Kjw4xKvvHEH-Iuf9WPAf22ZHPw.",
    "__Secure-1PSIDTS": "sidts-CjEBNiGH7qX0_i1F77u70nZVl9AisrZAQu18Llc1KI8lCvnZK7FLb3xN2z3LA5cbPyB_EAA",
    
}


#conversational_memory = ConversationBufferWindowMemory(
#    memory_key='chat_history',
#    k=3,
#    return_messages=True
#)

#llm = ChatOpenAI(
#    openai_api_key='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',
#    temperature=0,
#    model_name="gpt-3.5-turbo"
#)



# set title
st.title('Ask a question to an image')

# set header
st.header("Please upload an image")

# upload file
file = st.file_uploader("", type=["jpeg", "jpg", "png"])


text_input_1PSID =st.text_input(
        "Cole aqui o seu __Secure-1PSID do navegador com a conta Google",
        "Cole aqui",
        key="placeholder1",
    )

text_input_1PSIDTS =st.text_input(
        "Cole aqui o seu __Secure-1PSIDTS do navegador com a conta Google",
        "Cole aqui",
        key="placeholder2",
    )

if file:
    # display image
    st.image(file, use_column_width=True)

    # text input
    user_question = st.text_input('Ask a question about your image:')
    button_input=st.button("Perguntar!", on_click=click_button)
    if button_input:
        #bard = Bard(token_from_browser=True)
        cookie_dict['__Secure-1PSID']=text_input_1PSID
        cookie_dict['__Secure-1PSIDTS']=text_input_1PSIDTS
        bard = BardCookies(cookie_dict=cookie_dict,language='pt')
        with NamedTemporaryFile(dir='.') as f:
            f.write(file.getbuffer())
            image_path = f.name
        
        #image = open(image_path, 'rb').read()
        image=file.read()
        bard_answer = bard.ask_about_image(user_question, image)
        st.write(bard_answer['content'])
        button_input=False
        st.session_state.clicked=False


    
