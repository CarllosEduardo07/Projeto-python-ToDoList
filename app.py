import streamlit as st


from db import *

init_db()

st.title('ToDo List')



menu = ["create", "read", "update", "delete"]
choice = st.sidebar.selectbox("Menu", menu)



listStatus = ["Pendente","Concluido",]

if choice == "create":
    st.subheader("create")
    title = st.text_input ("Titulo")
    description = st.text_input ("Descrição")
    status = st.selectbox("Status", listStatus)
    button  = st.button ("salvar")
    
    if button:
        create_task(title, description, status)
        st.success("tarfa criada com sucesso")
        
        
if choice == "update":
    st.subheader("update")
    result = read_task()
    task_list = [task[1] for task in result]
    selected_task = st.selectbox("Selecione uma tarefa", task_list, key="update_select")
    
    task = result[task_list.index(selected_task)]
    title = st.text_input ("Titulo", task[1])
    description = st.text_input ("Descrição", task[2])
    status = st.selectbox("Status", listStatus, listStatus.index(task[3]))
    button  = st.button ("Atualizar")
    
    if button:
        update_task(title, description, status, task[0])
        st.success("tarfa atualizada com sucesso")
    
    
   
if choice == "read":
    st.subheader("Listagem de tarefas")
    result = read_task()
    for task in result:
        st.markdown(f"Titulo: {task[1]}")
        st.markdown(f"Descrição: {task[2]}")
        st.markdown(f"Status: {task[3]}")
        st.markdown(f"-----")
        
        
        
if choice == "delete":
    st.subheader("delete")
    result = read_task()
    task_list = [task[1] for task in result]
    selected_task = st.selectbox("Selecione uma tarefa", task_list, key="delete_select")
    
    task = result[task_list.index(selected_task)]
    button  = st.button ("Deletar")
    
    if button:
        delete_task(task[0])
        st.success("tarfa deletada com sucesso")
        
        


  