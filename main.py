from fastapi import FastAPI

#Instanciando a aplicação - motor da API ligando em 321...
app=FastAPI(title="API-Simulador de Emissões ESG")

#Criando a primeira rota - caminho web que recebrá as consultas
@app.get("/")
def leitura_incial():
    return{
        "status":"Sensor Online",
        "projeto" : "Rastreabilidade de Carbono",
        "leitura_atual":{
            "gás":"CO2",
            "vazão_m3_h": 1500,
            "temperatura_chamine_C":180
        }
    }

