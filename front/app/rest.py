# -*- coding: utf-8 -*-
from pdb import set_trace
import json
from app import req, api

class RetornoAPI:

    def __init__(self, operacao=False, response=None):
        self.operacao = operacao
        self.response = response
        self.text = response.text
        self.pagination = None
        try:
            self.dados = response.json()
            try:
                self.pk = self._get_pk(self.dados)
            except:
                pass
        except:
            self.dados = None

    def _get_pk(self, dados):
        return dados[u'_links'][u'self'][u'href'].split('/')[-1]

    def __bool__(self):
        return self.operacao

    def __nonzero__(self):
        return self.__bool__()

class API:

    def salvar(self, endpoint, dados):
        res = req.post(
            api['host_api']+endpoint,
            data=json.dumps(dados,encoding='utf-8'),
            auth=(api['auth_api']),
            headers=api['headers_api']
            )
        operacao = res.status_code == 200 or res.status_code == 201
        return RetornoAPI(operacao, res)

    def atualizar(self, endpoint, dados):
        res = req.put(
            api['host_api']+endpoint,
            data=json.dumps(dados,encoding='utf-8'),
            auth=(api['auth_api']),
            headers=api['headers_api']
            )
        operacao = res.status_code == 200 or res.status_code == 201
        return RetornoAPI(operacao, res)

    def buscar(self, endpoint):
        res = req.get(
                    api['host_api']+endpoint,
                    auth=(api['auth_api']),
                    headers=api['headers_api']
                    )
        dados = None
        operacao = res.status_code != 404
        retorno = RetornoAPI(operacao, res)
        if retorno.operacao:
            retorno.dados['id'] = retorno._get_pk(retorno.dados)
        return retorno

    def listar(self, endpoint, page=0, size=10, callback=None, param=''):
        if not param:
            param = '?page='+str(page)+'&size='+str(size)
        final_url = api['host_api']+endpoint+param
        res = req.get(
                    final_url,
                    auth=(api['auth_api']),
                    headers=api['headers_api']
                    )
        dados = None
        key = endpoint.split('/')[1]
        operacao = res.status_code != 404
        retorno = RetornoAPI(operacao, res)
        if retorno.operacao:
            retorno.pagination = retorno.dados['page']
            retorno.dados = []
            for dados in retorno.response.json()[u'_embedded'][key]:
                dados['id'] = retorno._get_pk(dados)
                if callback:
                    aux = {'req':req, 'auth':api['auth_api'], 'headers': api['headers_api'] }
                    dados = callback(dados, aux )
                retorno.dados.append( dados )
        return retorno

    def deletar(self, endpoint, pk):
        final_url = api['host_api']+endpoint+str(pk)
        res = req.delete(
                    final_url,
                    auth=(api['auth_api']),
                    headers=api['headers_api']
                    )
        operacao = res.status_code != 404
        retorno = RetornoAPI(operacao, res)
        return retorno
Api = API()