import requests
class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.validacao(cep):
            self.cep = cep
        else:
            raise ValueError('aff')

    def __str__(self):
        return self.formatacao()
    def validacao(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def formatacao(self):
        return '{}-{}'.format(self.cep[:5], self.cep[5:])

    def via_cep(self):
        url = 'https://viacep.com.br/ws/{}/json/'.format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (
            dados['localidade'],
            dados['bairro'],
            dados['uf']
        )