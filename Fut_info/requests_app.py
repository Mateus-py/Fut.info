import requests
import json
import datetime


Data_atual = datetime.datetime.now()
hora_atual = Data_atual.time()
hora_atual_formatada = hora_atual.strftime("%H:%M")






api_key = 'live_4cbc8dad8caa1b39d255d72a024aff'

api_key_test = 'test_aa5063def6ce2aadc5f17a73d11fd5'

headers = {'Authorization' : f'Bearer {api_key_test}'}



def get_partida_ao_vivo(time_id,key):
    """_Pega partida ao vivo por ID_

    Args:
        time_id (_INT_): _O ID DO TIME DADO POR API-FUTEBOL_
        key (_STR_): _API-KEY DO API_FUTEBOL_

    Returns:
        _DIC_: _[Time Mandante,Placar Mandante,Time Visitante,Placar Visitante,Hora de inicio jogo]_
    """
    link_p_ao_vivo = f'https://api.api-futebol.com.br/v1/times/{time_id}/partidas/ao-vivo'
    req_p_ao_vivo = requests.get(link_p_ao_vivo,headers={'Authorization' : f'Bearer {key}'})
    req_json = req_p_ao_vivo.json()
    time_mandante = req_json['copa-do-brasil'][0]['time_mandante']['nome_popular']
    placar_mandante = req_json['copa-do-brasil'][0]['placar_mandante']
    time_visitante = req_json['copa-do-brasil'][0]['time_visitante']['nome_popular']
    placar_visitante = req_json['copa-do-brasil'][0]['placar_visitante']
    inicio_jogo = req_json['copa-do-brasil'][0]['hora_realizacao']
    
    dados = [time_mandante,placar_mandante,time_visitante,placar_visitante,inicio_jogo]
    return dados

def get_info_rodada(r,key):
    """_Descriçao_

    Args:
        r (_Int_): _Indicar a rodada equivalente_\n
        key (_API_KEY_): Chave da api

    Returns:
        _Dict_: _Retorna [[Num_rodada_atual,status_rodada_atual],[Jogos da rodada atual(0-10)]]_
    """
    link_rd = f'https://api.api-futebol.com.br/v1/campeonatos/10/rodadas/{r}'
    rod = requests.get(link_rd,headers={'Authorization' : f'Bearer {key}'})
    rod_json = rod.json()
    
    # - Nome , status
    st_rod = [rod_json['rodada'],rod_json['status']]
    part_rod_ante = []
    for i in range(0,10):
        part_rod_ante.append(rod_json['partidas'][i]['placar'])
    
    
    info_needed = [st_rod,part_rod_ante]
    return info_needed
try:
# - Trazendo informaçoes da rodada atual
    info_r_a = get_info_rodada(3,api_key)
# - Trazendo informaçoes da proxima Rodada
    info_p_r = get_info_rodada(4,api_key)
except:
    print('ERRO!! SEM CONEXAO COM A INTERNET')

def name_to_id(time):
    """_Conversor ID_to_string(api_futebol)_

    Args:
        time (_STR_): _Atençao usar .upper apos o argumento senao nao funciona_

    Returns:
        _INT_: _retorna o id do time_
    """
    ID = None
    if time == 'FLAMENGO':
        ID = 18
    elif time == 'BOTAFOGO':
        ID = 22
    elif time == 'FORTALEZA':
        ID = 131
    elif time == 'PALMEIRAS':
        ID = 56
    elif time == 'INTERNACIONAL':
        ID = 44
    elif time == 'FLUMINENSE':
        ID = 26
    elif time == 'CRUZEIRO':
        ID = 37
    elif time == 'GREMIO':
        ID = 45
    elif time == 'SAO PAULO':
        ID = 57
    elif time == 'ATLETICO-MG':
        ID = 30
    elif time == 'SANTOS':
        ID = 63
    elif time == 'BAHIA':
        ID = 68
    elif time == 'GOIAS':
        ID = 115
    elif time == 'CORINTHIANS':
        ID = 65
    elif time == 'CUIABA':
        ID = 204
    elif time == 'VASCO':
        ID = 23
    elif time == 'BRAGANTINO':
        ID = 64
    elif time == 'ATHLETICO-PR':
        ID = 185
    elif time == 'CORITIBA':
        ID = 84

    return ID

def name_to_id_api_dt(time):
    """_Conversor ID_to_string(futebol.data.org)_

    Args:
        time (_STR_): _Atençao usar .upper apos o argumento senao nao funciona_

    Returns:
        _INT_: _retorna o id do time_
    """
    T_ID = None
    if time == 'FLAMENGO':
        T_ID = 1783
    elif time == 'BOTAFOGO':
        T_ID = 1770
    elif time == 'FORTALEZA':
        T_ID = 3984
    elif time == 'PALMEIRAS':
        T_ID = 1769
    elif time == 'INTERNACIONAL':
        T_ID = 6684
    elif time == 'FLUMINENSE':
        T_ID = 1765
    elif time == 'CRUZEIRO':
        T_ID = 1771
    elif time == 'GREMIO':
        T_ID = 1767
    elif time == 'SAO PAULO':
        T_ID = 1776
    elif time == 'ATLETICO-MG':
        T_ID = 1766
    elif time == 'SANTOS':
        T_ID = 6685
    elif time == 'BAHIA':
        T_ID = 1777
    elif time == 'GOIAS':
        T_ID = 4250
    elif time == 'CORINTHIANS':
        T_ID = 1779
    elif time == 'CUIABA':
        T_ID = 4289
    elif time == 'VASCO':
        T_ID = 1780
    elif time == 'BRAGANTINO':
        T_ID = 4286
    elif time == 'ATHLETICO-PR':
        T_ID = 1768
    elif time == 'CORITIBA':
        T_ID = 4241
    elif time == 'AMERICA_MG':
        T_ID = 1838

    return T_ID

def get_squad_info(t_id):
    """_Info do Time_

    Args:
        t_id (_INT_): _ID do Time_

    Returns:
        _DIC_: _Retorna um dicionario com as seguintes infos\n[Tecnico,Equipe[Jogador,Posiçao,Nacionalidade]]_
    """
    url = f'https://api.football-data.org/v4/teams/{t_id}'
    headers = { 'X-Auth-Token': '06ea9151e7ca405280cf1bd43a396a7a' }
    response = requests.get(url, headers=headers)
    req_json = response.json()
    tecnico = req_json['coach']['name']
    Equipe = []
    for item in req_json['squad']:
        Equipe.append([item['name'],item['position'],item['nationality']])
    
    Dados = [tecnico,Equipe]
    
    
    return Dados

