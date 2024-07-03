'''docstring'''
from fastapi import FastAPI

app = FastAPI(
    title ='Aprendiendo FastApi',
    description = 'Primeros pasos de una Api',
    version= '0.0.1',

)

@app.get('/', tags=['Inicio'])
def read_root():
    '''docstring'''
    return{'Hello': 'World'}
