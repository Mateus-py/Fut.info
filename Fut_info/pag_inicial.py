import flet as ft
import requests_app

try:
    num_rod_atual = requests_app.info_r_a[0][0]
    status_rod_atual = requests_app.info_r_a[0][1]
    num_rod_next = requests_app.info_p_r[0][0]
    status_rod_next = requests_app.info_p_r[0][1]
except:
    print('ERRO!! SEM CONEXAO COM A INTERNET')

def main(page: ft.Page):
    
    def Exit(e):
        btn_Exit.visible = False
        search.visible = False
        btn_search_mn.visible = False
        cont_search.visible = False
        page.update()
    # - colors 
    
    def get_nome_mandante(e):
        g_nome_mandante = search.value
        dados = requests_app.get_partida_ao_vivo(requests_app.name_to_id(g_nome_mandante.upper()),'test_aa5063def6ce2aadc5f17a73d11fd5')
        # - Getter do placar
        placar_mandante.value = dados[1]
        nome_mandante.value = dados[0]
        placar_visitante.value = dados[3]
        nome_visitante.value = dados[2]
        tempo.value = dados[4]
        page.update()
        # - Getter das infos dos times
        dados_time_mandante = requests_app.get_squad_info(requests_app.name_to_id_api_dt(g_nome_mandante.upper()))
        Equipe = dados_time_mandante[1]
        info_time_mandante.controls.append(ft.Text(f'Tecnico: {dados_time_mandante[0]}'))
        info_time_mandante.controls.append(ft.Divider())
        for jogador in range(len(Equipe)):
            info_time_mandante.controls.append(ft.Divider())
            info_time_mandante.controls.append(ft.Text(f'Jogador: {dados_time_mandante[1][jogador][0]}\nPos: {dados_time_mandante[1][jogador][1]}\nNac: {dados_time_mandante[1][jogador][2]}'))
        page.update()
        
        
    verde = '#2FAD2F'
    verde_cinza = '#4C7D5B'
    
    # - fonts
    
    page.fonts = {
        'Ysabeau' : '/fonts/Ysabeau/Ysabeau-VariableFont_wght.ttf',
        'Josefin_Sans' : '/fonts/Josefin_Sans/JosefinSans-Bold.ttf'
    }
    page.title = 'Fut.info'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.scroll = True
    page.bgcolor = verde_cinza
    page.padding = 20
    
    try:
        l_rodada_atual = ft.ListView(controls=[ft.Text(f'{num_rod_atual}ª Rodada\n\nStatus: {status_rod_atual}',font_family='Josefin_Sans',color='#000000')],padding=10,spacing=30)
        for i in range(0,10):
            l_rodada_atual.controls.append(ft.Text(f'{requests_app.info_r_a[1][i]}',font_family='Josefin_Sans',color='#000000'))
            l_rodada_anterior = ft.ListView(controls=[ft.Text(f'{num_rod_next}ª Rodada\n\nStatus: {status_rod_next}',font_family='Josefin_Sans',color='#000000')],padding=10,spacing=30)
        for i in range(0,10):
            l_rodada_anterior.controls.append(ft.Text(f'{requests_app.info_p_r[1][i]}',font_family='Josefin_Sans',color='#000000'))
    except:
        print('ERRO SEM CONEXAO !!')
        
        
    info_rodada_atual = ft.Container(
        width=300,
        bgcolor=verde,
        content=ft.Row(
            [
                l_rodada_atual,
            ],
        )
    )

    info_rodada_anterior = ft.Container(
        width=300,
        bgcolor=verde,
        content=ft.Row(
            [
                l_rodada_anterior,
            ],
        )
    )
    
    page_info = ft.Container(
        width=300,
        bgcolor=verde,
        content=ft.Column(
            [
                ft.Divider(),
                info_rodada_atual,
                ft.Divider(),
                info_rodada_anterior,
                ft.Divider(),
                ],
            alignment='center',
        ),
        border=ft.border.all(1,'#000000')
    )
    
    placar_mandante = ft.Text('2',size=25,text_align='center')
    placar_visitante = ft.Text('0',size=25,text_align='center')
    
    Time1 = ft.Container(
            width=35,
            height=35,
            bgcolor='#FFFFFF',
            border=ft.border.all(1,'#000000'),
            border_radius=10,
            content=placar_mandante,
        )
        
    Time2 = ft.Container(
            width=35,
            height=35,
            bgcolor='#FFFFFF',
            border_radius=10,
            border=ft.border.all(1,'#000000'),
            content=placar_visitante,
        )
        
    info_time_mandante = ft.ListView()
    cont_info_m = ft.Container(
        content=info_time_mandante
    )
    
    def back(e):
        body_app.content = body
        btn_search.visible = False
        btn_Exit.visible = False
        page.update()
        
    def open_search_bar(e):
        cont_search.visible = True
        search.visible = True
        btn_search_mn.visible = True
        btn_Exit.visible = True
        page.update()
    
    
    search = ft.TextField(tooltip='Pesquise os jogadores do Time',focused_border_color=verde_cinza,color='#000000',visible=False)
    btn_search_mn = ft.ElevatedButton('Pesquisar',bgcolor=verde,visible=False,on_click=get_nome_mandante)
    cont_search = ft.Container(
        padding=ft.padding.all(30),
        width=300,
        bgcolor=verde,
        content=ft.ResponsiveRow([search,btn_search_mn]),
        visible=False
    )
    
    nome_mandante = ft.Text('Flamengo',text_align='center',font_family='Josefin_Sans',color='#000000')
    nome_visitante = ft.Text('Manchester U',text_align='center',font_family='Josefin_Sans',color='#000000')
    tempo = ft.Text(f'00:00',text_align='center',font_family='Josefin_Sans',color='#000000')
    pag_jogos = ft.Container(
            width=300,
            bgcolor=verde,
            border_radius=10,
            content=ft.Column(
                [
                    cont_search,
                    ft.Divider(),
                    ft.ResponsiveRow([
                    ft.ResponsiveRow([nome_mandante,Time1,ft.Text('X',text_align='center',size=40),tempo,Time2,nome_visitante,ft.Text('obs:Clique no botao de pesquisa para obter informaçoes',size=10,text_align='center')]), 
                    ],
                    alignment='center',),
                    ft.Divider(),
                    ft.ResponsiveRow([cont_info_m,ft.Divider()]),
                    ft.Divider(),
                    ft.ResponsiveRow([ft.Text('@mateusxavier6 partidas ao vivo temporariamente desabilitado',text_align='center')],
                        )
                ],
            ),
            border=ft.border.all(1,'#000000'),
        )
    
    
    
    def change1(e):
        body_app.content = pag_jogos
        btn_search.visible = True
        if btn_search == True:
            btn_Exit.visible = True
        page.update()
        
    def change2(e):
        body_app.content = page_info
        page.update()
    
    btn_1 = ft.ElevatedButton(text='Acompanhe um jogo ao vivo',bgcolor=verde_cinza,color='#000000',on_click=change1)
    btn_2 = ft.ElevatedButton(text='Info rodada',bgcolor=verde_cinza,color='#000000',on_click=change2)
    body = ft.Container(
        width=300,
        bgcolor=verde,
        border=ft.border.all(1,"#000000"),
        content=ft.Column(
            [
                ft.Image(src='/images/banner.png'),
                ft.Text(value='Informaçoes sobre o Brasileirao e Copa Do Brasil em tempo real.',size=20,font_family='Ysabeau'),
                ft.Divider(),
                ft.Row(
                    [
                        btn_1,
                    ],
                    alignment='center'
                ),
                ft.Divider(),
                ft.Row(
                    [
                        btn_2
                    ],
                    alignment='center',
                ),
                ft.Divider(),
                ft.Text('@mateusxavier6 v1.0(Atualizado dia 05/05/2023 as 11:32)',
                                    text_align='center',)
                ],
            alignment='center',
            )
        )
    

    
    body_app = ft.Container(
        content=body
    )
    
    btn_Exit = ft.IconButton(icon=ft.icons.ARROW_BACK,visible=False,tooltip='Fechar barra de pesquisa',on_click=Exit)
    btn_search = ft.IconButton(icon=ft.icons.SEARCH,visible=False,tooltip='Pesquisar Time mandante',on_click=open_search_bar)
    page.add(
        ft.AppBar(bgcolor=verde,color='#000000',leading=btn_Exit,title=ft.Text('Fut.Info',font_family='Ysabeau',text_align='center'),
                  leading_width=40,center_title=True,actions=[btn_search,ft.IconButton(icon=ft.icons.HOME,tooltip='Voltar para HOME',on_click=back)]),
        body_app,
    )
    

    
ft.app(target=main,assets_dir='assets')