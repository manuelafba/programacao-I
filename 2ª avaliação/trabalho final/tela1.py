import flet as ft
import control as c
import re
import base64
import tela2

components = {
        'tf_nome': ft.Ref[ft.TextField](),
        'tf_cpf': ft.Ref[ft.TextField](),
        'tf_rg':ft.Ref[ft.TextField](),
        'tf_telefone': ft.Ref[ft.TextField](),
        'tf_endereço': ft.Ref[ft.TextField](),
        'tf_nascimento': ft.Ref[ft.TextField](),
        'tf_e-mail': ft.Ref[ft.TextField](),
        #add todos os compontens da tela aqui
    }

#imagem
image_holder = ft.Image(visible=False, fit=ft.ImageFit.CONTAIN, width=100,
        height=100)

selected_file_path = None

# funcao do upload da imagem
def handle_loaded_file(e: ft.FilePickerResultEvent):
    global selected_file_path
    print(e.files)
    if e.files and len(e.files):
        selected_file_path = e.files[0].path
        with open(e.files[0].path, 'rb') as r:
            image_holder.src_base64 = base64.b64encode(r.read()).decode('utf-8')
            image_holder.visible = True
            c.page.update()
    #[{name, path, size}]

#Funcao da mudança do tema
def changetheme(e):
    c.page.theme_mode = "light" if c.page.theme_mode =="dark" else "dark"
    c.page.update()
 
    
 
    toggledarklight.selected = not toggledarklight.selected
 
    
    c.page.update()

toggledarklight = ft.IconButton(
    on_click=changetheme,
    icon="dark_mode",
    selected_icon="light_mode",
    style=ft.ButtonStyle(
    color={"":ft.colors.WHITE,"selected":ft.colors.WHITE}))


# Funcao que mostre todos os componentes da tela 1
def view():
    file_picker = ft.FilePicker(on_result=handle_loaded_file)
    c.page.overlay.append(file_picker)
    def button_clicked(e):
        file_picker.pick_files(allow_multiple=False, allowed_extensions=['jpg', 'jpeg', 'png']) 
        c.page.update()
    return ft.View(
                "tela1",
                [                           
                    ft.Column(
                        [
                            ft.Row([ft.Container( content=ft.Text("Área de Preenchimento de Cadastro", size=20))],alignment=ft.MainAxisAlignment.CENTER),
                            ft.Column([
                                ft.Row([image_holder],alignment=ft.MainAxisAlignment.CENTER),
                                ft.Row([
                                # Botão de upload da foto
                                ft.Container(content= 
                                ft.ElevatedButton(
                                text="Escolher foto", style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10), padding=10),icon="image", on_click=
                                button_clicked
                                ))
                                ],alignment=ft.MainAxisAlignment.CENTER)#Container,
                                ]),    
                            ft.TextField(ref=components['tf_nome'], label="Nome", autofocus=True,prefix_icon=ft.icons.PERSON, helper_text="Apenas letras"),
                            ft.TextField(ref=components['tf_cpf'], label="CPF", prefix_icon=ft.icons.DOCUMENT_SCANNER, helper_text="xxx.xxx.xxx-xx"),
                            ft.TextField(ref=components['tf_rg'], label="RG", prefix_icon=ft.icons.DOCUMENT_SCANNER, helper_text="Deve conter 7 digitos"),
                            ft.TextField(ref=components['tf_telefone'], label="Telefone", prefix_icon=ft.icons.PHONE, helper_text="(xx) xxxxx-xxxx"),
                            ft.TextField(ref=components['tf_endereço'], label="Endereço",prefix_icon=ft.icons.HOME, helper_text="Deve conter no máximo 20 caracteres"),
                            ft.TextField(ref=components['tf_nascimento'], label="Nascimento",prefix_icon=ft.icons.STAR, helper_text="DD/MM/AAAA"),
                            ft.TextField(ref=components['tf_e-mail'], label="E-mail",prefix_icon=ft.icons.EMAIL,helper_text="name@example.com ou name@example.com.br"),
                            ft.Row(
                                [
                                    ft.Container(
                                        #Botao de cadastrar
                                            content= ft.FilledButton(
                                                        text="Cadastrar", style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10), padding=10),
                                                        icon="save", 
                                                        on_click= lambda e: cadastrar(e, selected_file_path)
                                                    )#ElevatedButton   
                                    ),#Container
                                    ft.Container(
                                            content= ft.ElevatedButton(
                                                        text="Pesquisar", style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10), padding=10), 
                                                        icon="search",
                                                        on_click= navigate_to_tela2
                                                    )#ElevatedButton   
                                    ),#Container                                 
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),#Row
                        ],
                        scroll=ft.ScrollMode.ALWAYS,
                        expand=True,
                    ),                    
                ],
                
                appbar= ft.AppBar(            
                    title=ft.Text("Sistema de cadastro", font_family="RobotoSlab",weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                    center_title=True,
                    bgcolor=ft.colors.RED_900,
                    actions=[toggledarklight]                   
                ),    
            )
    
def cadastrar(e, selected_file_path = None):
    

    nome = components['tf_nome'].current.value
    cpf = components['tf_cpf'].current.value
    rg = components['tf_rg'].current.value
    telefone = components['tf_telefone'].current.value
    endereco = components['tf_endereço'].current.value
    nascimento = components['tf_nascimento'].current.value
    email = components['tf_e-mail'].current.value
    import csv
    import uuid
    components['tf_nome'].current.error_text = error_message('nome')
    components['tf_cpf'].current.error_text = error_message('cpf')
    components['tf_rg'].current.error_text = error_message('rg')
    components['tf_telefone'].current.error_text = error_message('telefone')
    components['tf_endereço'].current.error_text = error_message('endereco')
    components['tf_nascimento'].current.error_text = error_message('nascimento')
    components['tf_e-mail'].current.error_text = error_message('email')
    # exibir_snackbar_imagem_salva(selected_file_path)
    c.page.update()

    # # Se todos os campos forem válidos, escreva no arquivo CSV
    # if validar_nome(nome) and validar_telefone(telefone) and validar_cpf(cpf) and validar_rg(rg) and validar_email(email) and validar_nascimento(nascimento) and validar_endereco(endereco) and selected_file_path is not None:
    #     dados = [
    #         [nome, telefone, cpf, rg, endereco, nascimento, email, selected_file_path]]

    #     # Abre o arquivo em modo de escrita
    #     with open('bd.csv', 'a') as arquivo:
    #         # arquivo.write('Nome,Telefone,CPF,RG,Endereco,Nascimento,E-mail,Upload de Foto\n')
    #         for linha in dados:
    #             arquivo.write(','.join(linha) + '\n')
    if validar_nome(nome) and validar_telefone(telefone) and validar_cpf(cpf) and validar_rg(rg) and validar_email(email) and validar_nascimento(nascimento) and validar_endereco(endereco) and selected_file_path is not None:
        dados = [
            [nome, telefone, cpf, rg, endereco, nascimento, email, selected_file_path]]

        # Abre o arquivo CSV em modo de leitura para determinar o último ID usado
        with open('bd.csv', 'r', newline='') as arquivo_leitura:
            reader = csv.DictReader(arquivo_leitura)
            ids_existentes = set([linha['id'] for linha in reader])

        # Abre o arquivo CSV em modo de escrita e adiciona os novos dados com IDs
        with open('bd.csv', 'a', newline='') as arquivo:
            fieldnames = ['Nome', 'Telefone', 'CPF', 'RG', 'Endereco', 'Nascimento', 'E-mail', 'Upload de Foto','id']
            writer = csv.DictWriter(arquivo, fieldnames=fieldnames)

            # Cria um novo ID único para cada linha de dados e verifica se é único
            for linha in dados:
                novo_id = str(uuid.uuid4())
                while novo_id in ids_existentes:  # Garante que o ID seja único
                    novo_id = str(uuid.uuid4())
                ids_existentes.add(novo_id)

                # Cria um dicionário com os dados e o novo ID
                linha_com_id = {'Nome': linha[0], 'Telefone': linha[1], 'CPF': linha[2], 'RG': linha[3], 'Endereco': linha[4], 'Nascimento': linha[5], 'E-mail': linha[6], 'Upload de Foto': linha[7],'id': novo_id,}
                writer.writerow(linha_com_id)
        #Zera os TextFields
        components['tf_nome'].current.value = ''    
        components['tf_cpf'].current.value = ''
        components['tf_rg'].current.value = ''
        components['tf_telefone'].current.value = ''
        components['tf_endereço'].current.value = ''
        components['tf_nascimento'].current.value = ''
        components['tf_e-mail'].current.value = ''
        selected_file_path = None
        image_holder.visible = False
        c.page.snack_bar = ft.SnackBar(
        ft.Text("Cadastro realizado com sucesso", size=20),
        duration=2000,
        bgcolor="green"
        )
        c.page.snack_bar.open = True
        tela2.atualizar_csv([])
        c.page.update()

# def exibir_snackbar_imagem_salva(selected_file_path):
#     if selected_file_path is None:
#         snack_bar = ft.SnackBar(
#             ft.Text("Você deve escolher uma foto", size=20),
#             duration=800,
#             bgcolor="red"
#         )
#         c.snack_bar.open = True
#     c.page.snack_bar = c.snack_bar

def validar_nome(nome):
    # Verifica se o nome não contém números
    nome_pattern = re.compile(r'^[^\d]+$')
    return bool(nome_pattern.match(nome))

def validar_telefone(telefone):
    # Verifica se o telefone possui o formato (xx)xxxxx-xxxx ou (xx) xxxxx-xxxx
    telefone_pattern = re.compile(r'^\(\d{2}\) ?\d{5}-\d{4}$')
    return bool(telefone_pattern.match(telefone))

def validar_cpf(cpf):
    # Verifica se o CPF possui o formato 111.111.111-11
    cpf_pattern = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
    return bool(cpf_pattern.match(cpf))

def validar_rg(rg):
    # Verifica se o RG possui exatamente 9 dígitos
    rg_pattern = re.compile(r'^\d{7}$')
    return bool(rg_pattern.match(rg))

def validar_email(email):
    email_pattern = re.compile(r'^\S+@\S+\.(com|com\.br)$')
    return bool(email_pattern.match(email))

def validar_nascimento(data):
    # Considerando o formato DD/MM/AAAA
    nascimento_pattern = re.compile(r'^\d{2}/\d{2}/\d{4}$')
    return bool(nascimento_pattern.match(data))

def validar_endereco(endereco):
    # Validação simples de endereço
    return 20 >= len(endereco) >= 5  # Exemplo: endereço deve ter pelo menos 5 caracteres

def error_message(data):
    try:
        if data == 'nome':
            # Validação do nome
            if not validar_nome(components['tf_nome'].current.value) and components['tf_nome'].current.value:
                raise ValueError("O nome não deve conter números")
            elif not components['tf_nome'].current.value:
                raise ValueError("Por favor preencha o seu nome.")
        elif data == 'telefone':
            # Validação do telefone
            if not validar_telefone(components['tf_telefone'].current.value) and components['tf_telefone'].current.value:
                raise ValueError("O telefonde deve ser no formato: (xx) xxxxx-xxxx")
            elif not components['tf_telefone'].current.value:
                raise ValueError("Por favor preencha o telefone.")
        elif data == 'cpf':
            # Validação do CPF
            if not validar_cpf(components['tf_cpf'].current.value) and components['tf_cpf'].current.value:
                raise ValueError("O CPF deve ser no formato: xxx.xxx.xxx-xx")
            elif not components['tf_cpf'].current.value:
                raise ValueError("Por favor preencha o seu CPF.")
        elif data == 'rg':
            # Validação do RG
            if not validar_rg(components['tf_rg'].current.value) and components['tf_rg'].current.value:
                raise ValueError("RG inválido(O RG possui deve exatamente 7 dígitos e não conter letras)")
            elif not components['tf_rg'].current.value:
                raise ValueError("Por favor preencha o seu RG.")
        elif data == 'email':
            # Validação do E-mail
            if not validar_email(components['tf_e-mail'].current.value) and components['tf_e-mail'].current.value:
                raise ValueError("E-mail inválido(formato correto: name@example.com ou name@example.com.br)")
            elif not components['tf_e-mail'].current.value:
                raise ValueError("Por favor preencha o seu email.")
        elif data == 'nascimento':
            # Validação da data de nascimento
            
                    
            if not validar_nascimento(components['tf_nascimento'].current.value) and components['tf_nascimento'].current.value:
                raise ValueError("Data de nascimento inválida(formato: DD/MM/AAAA)")
            elif not components['tf_nascimento'].current.value:
                raise ValueError("Por favor preencha a sua data de nascimento.")
            
            if components['tf_nascimento'].current.value:
                nascimento=components['tf_nascimento'].current.value
                dia=int(nascimento[0]+nascimento[1])
                mes=int(nascimento[3]+nascimento[4])
                ano=int(nascimento[6]+nascimento[7]+nascimento[8]+nascimento[9])
                
                if not (0<dia<32  and 0<mes<13 and 1899<ano<2024):
                    raise ValueError("Data de nascimento impossivel")
                
                
        elif data == 'endereco':
            if not validar_endereco(components['tf_endereço'].current.value) and components['tf_endereço'].current.value:
                raise ValueError("Endereço inválido")
            elif not components['tf_endereço'].current.value:
                raise ValueError("Por favor preencha o seu endereço.")
        else:
            raise ValueError("Data inválida")
    except ValueError as e:
        return str(e)
    else:
        return ''
    
def navigate_to_tela2(e):
    c.menu(e)
    c.page.go('1')