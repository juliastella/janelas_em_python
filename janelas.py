import PySimpleGUI as janelas

# Criar janelas e estilos.
#Primeira janela
def janela_escolha():
    janelas.theme('LightGreen')
    layout = [
        [janelas.Text('Escolha que tipo de opção faz sua necessidade:', size=(35,1))],
        [janelas.Button('Cadastro de funcionarios', size=(20,1)), janelas.Button('Cadastro de aluno', size=(15, 1))], # butões de escolha de janelas.
        [janelas.Button('Cadastro de diciplinas', size=(20,1)), janelas.Button('Cadastro de curso', size=(17, 1))],
        [janelas.Button('Cadastro de turno', size=(17,1)), janelas.Button('Matricula', size=(10, 1))]
    ]
    return janelas.Window('escolha', layout=layout, finalize=True, size=(500,500)) #Chamando a janela

def janela_cadastro_aluno():
    janelas.theme('LightGreen')
    layout = [
        [janelas.Text('Nome'), janelas.Input(size=(40,3))],
        [janelas.Text('E-mail'), janelas.Input(size=(40,3))],
        [janelas.Text('Telefone'),janelas.Input(size=(40,3))],
        [janelas.Text('Cep'), janelas.Input(size=(40,3))],
        [janelas.Text('CPF'), janelas.Input(size=(40,3))],
        [janelas.Button('Voltar'), janelas.Button('Salvar')]
    ]
    return janelas.Window('Cadastro de aluno', layout=layout,  finalize=True, size=(500,500))  

def janela_cadastro_funcionarios():
    janelas.theme('LightGreen')
    layout = [
        [janelas.Text('Nome'), janelas.Input(size=(40,3))],
        [janelas.Text('E-mail'), janelas.Input(size=(40,3))],
        [janelas.Text('Telefone'),janelas.Input(size=(40,3))],
        [janelas.Text('Cep'), janelas.Input(size=(40,3))],
        [janelas.Text('CPF'), janelas.Input(size=(40,3))],
        [janelas.Text('Senha'), janelas.Input(key='Senha', password_char='*', size=(40,3))],
        [janelas.Button('Voltar'), janelas.Button('Salvar')]
    ]
    return janelas.Window('Cadastro de funcionarios', layout=layout,  finalize=True, size=(500,500))  

def janela_cadastro_disciplina():
    janelas.theme('LightGreen')
    layout = [
        [janelas.Text('Nome da disciplina'), janelas.Input(size=(40,3))],
        [janelas.Button('Voltar'), janelas.Button('Salvar')]
    ]
    return janelas.Window('Cadastro de diciplinas', layout=layout,  finalize=True, size=(500,500))  

def janela_cadastro_curso():
    janelas.theme('LightGreen')
    layout = [
        [janelas.Text('Nome do curso'), janelas.Input(size=(40,3))],
        [janelas.Text('Carga horário'), janelas.Input(size=(40,3))],
        [janelas.Button('Voltar'), janelas.Button('Salvar')]
    ]
    return janelas.Window('Cadastro de curso', layout=layout,  finalize=True, size=(500,500))  

def janela_cadastro_turno():
    janelas.theme('LightGreen')
    layout = [
        [janelas.Text('Turno'), janelas.Combo(['Manhã (07:00 - 12:00)', 'Tarde (13:00 - 17:00)', 'Noite (18:0 - 23:00)'],'Turno', size=(40,3))],
        [janelas.Text('Carga horário'), janelas.Input(size=(40,3))],
        [janelas.Button('Voltar'), janelas.Button('Salvar')]
    ]
    return janelas.Window('Cadastro de turno', layout=layout,  finalize=True, size=(500,500))  

def janela_cadastro_matricula():
    janelas.theme('LightGreen')
    layout = [
        [janelas.Text('CPF'), janelas.Input(size=(40,3))],
        [janelas.Text('Curso'), janelas.Input(size=(40,3))],
        [janelas.Text('Diciplina'), janelas.Input(size=(40,3))],
        [janelas.Text('Turno'), janelas.Input(size=(40,3))],
        [janelas.Button('Voltar'), janelas.Button('Salvar')]
    ]
    return janelas.Window('Matricula', layout=layout,  finalize=True, size=(500,500)) 

# Criar as janelas inicias.
janela1, janela2, janela3, janela4, janela5, janela6, janela7   = janela_escolha(), None, None, None, None, None, None #Criadas das duas janelas, o None serve para que a janela não recebar nenhum valor.

# Criar um loop de leitura de eventos.
while True: # lupe infinito
    window,event,values = janelas.read_all_windows()
    # Quando janela for fechada;
    if window == janela1 and event == janelas.WIN_CLOSED:
        break
    # Quando queremos ir para próxima janela;
    if window == janela1 and event == 'Cadastro de aluno': 
        janela2 = janela_cadastro_aluno()
        janela1.hide() 
     # Do home até  cadastro até funcionarios; 
    if window == janela1 and event == 'Cadastro de funcionarios': 
        janela3 = janela_cadastro_funcionarios()
        janela1.hide()
    # Do home até  cadastro até diciplinas; 
    if window == janela1 and event == 'Cadastro de diciplinas': 
        janela4 = janela_cadastro_disciplina()
        janela1.hide()       
    # Do home até  cadastro até diciplinas; 
    if window == janela1 and event == 'Cadastro de curso':
        janela5 = janela_cadastro_curso()
        janela1.hide()
    # Do home até  cadastro até turno;
    if window == janela1 and event == 'Cadastro de turno':
        janela6 = janela_cadastro_turno()
        janela1.hide()
    # Do home até  cadastro até Matricula;
    if window == janela1 and event == 'Matricula':
        janela7 = janela_cadastro_matricula()
        janela1.hide()
    
    # Quando queremos voltar para janela de home;
    if window == janela2 and event == "Voltar":
        janela2.hide()
        janela1.un_hide()  
    
    if window == janela3 and event == "Voltar":
        janela3.hide()
        janela1.un_hide() 
         
    if window == janela4 and event == "Voltar":
        janela4.hide()
        janela1.un_hide()   
        
    if window == janela5 and event == "Voltar":
        janela5.hide()
        janela1.un_hide()  
    
    if window == janela6 and event == "Voltar":
        janela6.hide()
        janela1.un_hide()  
    
    if window == janela7 and event == "Voltar":
        janela7.hide()
        janela1.un_hide()     
              
    # Receber os valores 
    
# Lógica de o que deve acontecer ao clicar

