from itertools import count
from typing import Optional
from flask import Flask, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel, Field
from tinydb import TinyDB, Query


server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='Live de Python')
spec.register(server)
database = TinyDB('database.json')
c = count()


class Pessoa(BaseModel):
    id: Optional[int] = Field(default_factory=lambda: next(c))
    nome: str
    idade: int

class Pessoas(BaseModel):
    pessoas: list[Pessoa]
    count: int



@server.get('/pessoas')
@spec.validate(resp=Response(HTTP_200=Pessoas))
def buscar_pessoas():
    """Retorna todas as Pessoas da bade de dados"""
    return jsonify(
        Pessoas(
            pessoas=database.all(),
            count= len(database.all())   
        ).dict()
    )



@server.post('/pessoas')
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_200=Pessoa))
def inserir_pessoas():
    """Insere uma Pessoas no banco de dados."""
    body = request.context.body.dict()
    database.insert(body)
    return body




@server.put('/pessoas/<int:id>')
@spec.validate(
    body=Request(Pessoa),
    resp=Response(HTTP_200=Pessoas)
)
def editar_pessoas(id):
    """Editar Pessoas pelo id"""
    Pessoa = Query()
    body = request.context.body.dict()
    database.update(body, Pessoa.id == id)
    return jsonify(body)



@server.delete('/pessoas/<int:id>')
@spec.validate(resp=Response('HTTP_204'))
def deletar_pessoas(id):
    """Excluir Pessoas pelo id"""
    database.remove(Query().id == id)
    return jsonify({})



server.run()
