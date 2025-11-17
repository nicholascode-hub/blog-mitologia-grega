# Arquivo: mitologia_grega/views.py

from django.shortcuts import render, Http404
from django.http import HttpResponse # Adicione esta importação para respostas simples

# 1. Função chamada por path('', views.lista_deuses, ...)
def lista_deuses(request):
    # Por enquanto, retorne uma resposta HTTP simples para evitar erros.
    return HttpResponse("Página da Lista de Deuses.")

# 2. Função chamada por path('deus/<int:deus_id>/', views.detalhe_deus, ...)
def detalhe_deus(request, deus_id):
    # O nome aqui DEVE ser detalhe_deus
    # Ela precisa aceitar o 'request' e o argumento da URL 'deus_id'.
    return HttpResponse(f"Detalhe do Deus ID: {deus_id}")

# 3. Função chamada por path('contact/', views.contact, ...)
def contact(request):
    return HttpResponse("Página de Contato.")

# Dicionário com informações de todos os deuses
DEUSES = {
    'zeus': {
        'nome': 'Zeus',
        'emoji': '⚡',
        'titulo': 'Rei dos Deuses',
        'dominio': 'Rei dos deuses, senhor dos céus e do trovão',
        'simbolos': 'Raio, águia, cetro, carvalho',
        'genealogia': 'Filho mais novo de Cronos e Reia',
        'caracteristicas': 'Governante supremo do Monte Olimpo, conhecido por suas muitas relações amorosas e filhos. Na mitologia romana: Júpiter.',
        'descricao': 'Zeus é a figura máxima do panteão grego, representando a autoridade e a justiça divina. Seu poder está ligado ao céu e ao trovão, sendo temido e respeitado por todos os outros deuses e mortais.'
    },
    'hera': {
        'nome': 'Hera',
        'emoji': '👑',
        'titulo': 'Deusa do Casamento',
        'dominio': 'Rainha dos deuses, deusa do casamento e da família',
        'simbolos': 'Pavão, diadema, romã',
        'genealogia': 'Irmã e esposa de Zeus',
        'caracteristicas': 'Protetora das mulheres casadas, conhecida por seu temperamento forte e ciúmes das amantes de Zeus. Na mitologia romana: Juno.',
        'descricao': 'Hera simboliza a fidelidade conjugal e a proteção da instituição do casamento, embora sua personalidade possua aspectos fortes e de vingança contra as infidelidades de seu marido.'
    },
    'poseidon': {
        'nome': 'Poseidon',
        'emoji': '🌊',
        'titulo': 'Deus dos Mares',
        'dominio': 'Senhor dos mares, oceanos e terremotos',
        'simbolos': 'Tridente, cavalo, golfinho',
        'genealogia': 'Irmão de Zeus e Hades, filho de Cronos e Reia',
        'caracteristicas': 'Temperamento instável como as ondas do mar, responsável por tempestades e terremotos. Na mitologia romana: Netuno.',
        'descricao': 'Poseidon governa todos os corpos de água e é reverenciado pelos navegantes. Sua ira pode causar terríveis tempestades, enquanto sua benevolência garante mares calmos e viagens seguras.'
    },
    'atena': {
        'nome': 'Atena',
        'emoji': '🦉',
        'titulo': 'Deusa da Sabedoria',
        'dominio': 'Deusa da sabedoria, estratégia militar e civilização',
        'simbolos': 'Coruja, oliveira, capacete, escudo',
        'genealogia': 'Nascida da cabeça de Zeus',
        'caracteristicas': 'Guerreira estrategista, padroeira de Atenas, protetora dos heróis. Na mitologia romana: Minerva.',
        'descricao': 'Atena representa a sabedoria prática e a guerra justa. Nasceu completamente armada da cabeça de Zeus, simbolizando a razão que emerge do poder supremo.'
    },
    'ares': {
        'nome': 'Ares',
        'emoji': '⚔️',
        'titulo': 'Deus da Guerra',
        'dominio': 'Deus da guerra, violência e derramamento de sangue',
        'simbolos': 'Lança, escudo, capacete, cães, abutre',
        'genealogia': 'Filho de Zeus e Hera',
        'caracteristicas': 'Impulsivo e sanguinário, representa o aspecto brutal da guerra. Na mitologia romana: Marte.',
        'descricao': 'Ares personifica a face violenta e caótica do conflito armado, diferente de Atena que representa a estratégia. Apesar de sua força, era frequentemente derrotado por outros deuses e heróis mais astutos.'
    },
    'demeter': {
        'nome': 'Deméter',
        'emoji': '🌾',
        'titulo': 'Deusa da Colheita',
        'dominio': 'Deusa da agricultura, colheita e fertilidade da terra',
        'simbolos': 'Espigas de trigo, tocha, foice',
        'genealogia': 'Irmã de Zeus, filha de Cronos e Reia',
        'caracteristicas': 'Mãe dedicada de Perséfone, responsável pelos ciclos das estações. Na mitologia romana: Ceres.',
        'descricao': 'Deméter controla a fertilidade da terra. Quando sua filha Perséfone foi raptada por Hades, sua tristeza causou o inverno, e sua alegria no retorno da filha traz a primavera.'
    },
    'apolo': {
        'nome': 'Apolo',
        'emoji': '☀️',
        'titulo': 'Deus do Sol',
        'dominio': 'Deus do sol, música, profecia, medicina e poesia',
        'simbolos': 'Lira, arco e flechas, coroa de louros, cisne',
        'genealogia': 'Filho de Zeus e Leto, irmão gêmeo de Ártemis',
        'caracteristicas': 'O mais belo dos deuses, patrono das artes e da verdade. Mesmo nome na mitologia romana.',
        'descricao': 'Apolo é um deus multifacetado, representando a luz da razão, a beleza das artes e o poder da profecia. Seu oráculo em Delfos era o mais importante da Grécia antiga.'
    },
    'artemis': {
        'nome': 'Ártemis',
        'emoji': '🌙',
        'titulo': 'Deusa da Caça',
        'dominio': 'Deusa da caça, animais selvagens, virgindade e lua',
        'simbolos': 'Arco e flechas, veado, lua crescente',
        'genealogia': 'Filha de Zeus e Leto, irmã gêmea de Apolo',
        'caracteristicas': 'Protetora das jovens mulheres e animais selvagens, feroz defensora da castidade. Na mitologia romana: Diana.',
        'descricao': 'Ártemis é uma deusa independente e poderosa, que escolheu permanecer virgem e livre. Protege tanto os animais quanto aqueles que caçam com respeito, punindo severamente quem desrespeita a natureza.'
    },
    'hefesto': {
        'nome': 'Hefesto',
        'emoji': '🔨',
        'titulo': 'Deus da Forja',
        'dominio': 'Deus do fogo, metalurgia, artesanato e forja',
        'simbolos': 'Martelo, bigorna, fogo, tenaz',
        'genealogia': 'Filho de Zeus e Hera (ou apenas de Hera)',
        'caracteristicas': 'Único deus olimpiano com defeito físico (coxo), artesão incomparável. Na mitologia romana: Vulcano.',
        'descricao': 'Hefesto é o ferreiro divino, criador das armas dos deuses e de objetos maravilhosos. Apesar de sua aparência, é casado com Afrodite e respeitado por suas habilidades únicas.'
    },
    'afrodite': {
        'nome': 'Afrodite',
        'emoji': '💖',
        'titulo': 'Deusa do Amor',
        'dominio': 'Deusa do amor, beleza, sexualidade e fertilidade',
        'simbolos': 'Rosa, pomba, cisne, espelho, concha',
        'genealogia': 'Nascida da espuma do mar',
        'caracteristicas': 'A mais bela das deusas, capaz de fazer qualquer um se apaixonar. Na mitologia romana: Vênus.',
        'descricao': 'Afrodite personifica a beleza e o desejo. Nascida da espuma do mar, ela tem o poder de influenciar os corações de deuses e mortais, causando tanto alegrias quanto tragédias amorosas.'
    },
    'hermes': {
        'nome': 'Hermes',
        'emoji': '🕊️',
        'titulo': 'Mensageiro dos Deuses',
        'dominio': 'Mensageiro dos deuses, comércio, viajantes e ladrões',
        'simbolos': 'Caduceu, sandálias aladas, capacete alado',
        'genealogia': 'Filho de Zeus e da ninfa Maia',
        'caracteristicas': 'Rápido e astuto, guia das almas ao submundo, protetor dos comerciantes. Na mitologia romana: Mercúrio.',
        'descricao': 'Hermes é o mais esperto dos deuses, conhecido por sua velocidade e engenhosidade. Como mensageiro divino, transita livremente entre o Olimpo, a Terra e o Submundo.'
    },
    'dionisio': {
        'nome': 'Dionísio',
        'emoji': '🍇',
        'titulo': 'Deus do Vinho',
        'dominio': 'Deus do vinho, festividades, teatro e êxtase',
        'simbolos': 'Uvas, vinha, tirso, pantera',
        'genealogia': 'Filho de Zeus e da mortal Sêmele',
        'caracteristicas': 'Único deus olimpiano nascido de mãe mortal, patrono do teatro e da alegria. Na mitologia romana: Baco.',
        'descricao': 'Dionísio representa a libertação dos sentidos e o êxtase. Inventor do vinho, ele traz tanto alegria quanto loucura, simbolizando a dualidade entre prazer e perigo.'
    },
    'hades': {
        'nome': 'Hades',
        'emoji': '💀',
        'titulo': 'Deus do Submundo',
        'dominio': 'Senhor do submundo e dos mortos',
        'simbolos': 'Capacete da invisibilidade, cetro, Cérbero',
        'genealogia': 'Irmão mais velho de Zeus, filho de Cronos e Reia',
        'caracteristicas': 'Governante do mundo dos mortos, justo mas inflexível. Mesmo nome na mitologia romana.',
        'descricao': 'Hades não é um deus do mal, mas o guardião imparcial do reino dos mortos. Raramente deixa seu domínio e é temido mais por seu poder sobre a morte do que por crueldade.'
    }
}


def index(request):
    """View para a página inicial"""
    return render(request, 'index.html')


def detalhes_deus(request, nome_deus):
    """View para os detalhes de cada deus"""
    nome_deus = nome_deus.lower()
    
    if nome_deus not in DEUSES:
        raise Http404("Deus não encontrado")
    
    deus = DEUSES[nome_deus]
    
    context = {
        'deus': deus
    }
    
    return render(request, 'deuses/detalhes.html', context)