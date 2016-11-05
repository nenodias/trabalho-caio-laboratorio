# -*- coding:utf-8 -*-
import json
import requests as r

cabecalho = {'Accept':'application/json','Content-Type':'application/json'}

requisicoes_okay = 0

for i in range(100):
    dados = {
        "nome":"Jose %i"%(i),
        "email":"josedasilva%i@gmail.com"%(i),
        "rg": 123456789,
        "telefone":"+55 14 9 1234-5%03d"%(i),
        "endereco":{
            "rua":"Rua dos Bobos%i"%(i),
            "numero":"%i"%(i),
            "bairro":"Nenhum%i"%(i),
            "cidade":"Wherever%i"%(i)
        }
    }

    resp = r.post('http://admin:admin123@localhost:8000/cliente/', headers=cabecalho, data=json.dumps(dados) )
    okay = resp.status_code == 200 or resp.status_code == 201
    if okay:
        requisicoes_okay += 1

print(requisicoes_okay)