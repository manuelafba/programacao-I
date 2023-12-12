import flet as ft
import tela1, tela2, tela3

def init(p):
    global page, telas, cadastros        
    page = p
    cadastros = []    
    telas = {
        '0': tela1.view(),
        '1': tela2.view(),
        '2': tela3.view(),
    }
    

def route_change(route):
    page.views.clear()    
    page.views.append(
        telas[page.route]
    )          
    page.update()



def menu(e):
    tela2.components["tabela"].current.rows = tela2.data_table()
    