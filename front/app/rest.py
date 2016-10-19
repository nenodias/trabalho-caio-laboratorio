# -*- coding: utf-8 -*-
import json
from app import req, api

class RetornoAPI:

    def __init__(self, operacao=False, response=None):
        self.operacao = operacao
        self.response = response
        self.text = response.text
        try:
            self.dados = response.json()
            try:
                self.pk = self.dados[u'_links'][u'self'][u'href'].split('/')[-1]
            except:
                pass
        except:
            self.dados = None

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
        return RetornoAPI(operacao, res)

Api = API()