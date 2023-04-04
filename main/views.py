from django.views.generic import TemplateView
from django.http import JsonResponse


def troca_dicio(chave):
    dicionario_antigo = {
    '0': 'A',
    '1': 'B',
    '2': 'C',
    '3': 'D',
    '4': 'E',
    '5': 'F',
    '6': 'G',
    '7': 'H',
    '8': 'I',
    '9': 'J',
    '10': 'K',
    '11': 'L',
    '12': 'M',
    '13': 'N',
    '14': 'O',
    '15': 'P',
    '16': 'Q',
    '17': 'R',
    '18': 'S',
    '19': 'T',
    '20': 'U',
    '21': 'V',
    '22': 'W',
    '23': 'X',
    '24': 'Y',
    '25': 'Z',
    '26': 'Á',
    '27': 'É',
    '28': 'Í',
    '29': 'Ó',
    '30': 'Ú',
    '31': 'Ã',
    '32': 'Õ',
    '33': 'Ẽ',
    '34': '.',
    '35': ',',
    '36': '!',
    '37': '?',
    '38': ' ',
    }
    dicionario_novo = {}
    limite = len(dicionario_antigo)
    if chave > limite:
        chave = chave % limite

    for elemento in dicionario_antigo:
        dicionario_novo[str(chave)] = dicionario_antigo[elemento]
        chave += 1
        if chave >= limite:
            chave = 0

    return dicionario_novo


def maq_cripto(frase_descriptografada, chave):
    dicionario = troca_dicio(chave)
    frase_criptografada = ''
    for elemento in frase_descriptografada.upper():
        for chave in dicionario.keys():
            if elemento == dicionario[chave]:
                frase_criptografada += chave + ' '

    return frase_criptografada


def maq_descripto(frase_criptografada, chave):
    dicionario = troca_dicio(chave)
    frase_descriptografada = ''
    for elemento in frase_criptografada:
        for chave in dicionario.keys():
            if elemento == chave:
                frase_descriptografada += dicionario[chave]

    return frase_descriptografada


def cripto(request):
    return JsonResponse({'mensagem': maq_cripto(request.GET.get('mensagem'), int(request.GET.get('chave')))})


def descripto(request):
    return JsonResponse({'mensagem': maq_descripto(request.GET.get('mensagem').split(), int(request.GET.get('chave')))})


class MainView(TemplateView):
    template_name = 'main.html'
