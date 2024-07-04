'''docstring'''
from fastapi import FastAPI, Path, Query #Body
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(
    title ='Aprendiendo FastApi',
    description = 'Primeros pasos de una Api',
    version= '0.0.1',
)

class Movie(BaseModel):
    '''docstring'''
    id: Optional[int] = None
    title: str = Field(default= 'Título de la película', min_length=3, max_length=60)
    overview: str = Field(default= 'Descripción', min_length=5, max_length=60)
    year: int = Field(default= 2023)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=3, max_length=15, default='Categoria')

#    def to_dict(self):
#        return {
#            "id": self.id,
#            "title": self.title,
#            "overview": self.overview,
#            "year": self.year,
#            "rating": self.rating,
#            "category": self.category
#
#        }

movies = [
    {
        'id':1,
        'title': 'El Padrino',
        'overview': 'El Padrino es una película de 1972',
        'year': '1972',
        'rating': 9.2,
        'category': 'Crimen'
    }
]

@app.get('/', tags=['Inicio'])
def read_root():
    '''docstring'''
    return HTMLResponse('<h2> Hola Mundo! </h2>')

@app.get('/movies', tags=['Movies'])
def get_movies():
    '''docstring'''
    return JSONResponse(content=movies)

@app.get('/movies/{id}', tags=['Movies'],status_code=200)
def get_movie(id: int = Path(ge=1, le=100)):
    '''docstring'''
    for item in movies:
        if item["id"] == id:
            return item
    return []

@app.get('/movies/', tags=['Movies'])
def get_movies_by_category(category: str = Query(min_length=3, max_length=15)):
    '''docstring'''
    return category

@app.post('/movies', tags=['Movies'], status_code=201)
def create_movie(movie: Movie):
    '''docstring'''
    movies.append(movie)
    print(movies)
    return JSONResponse(content={'message': 'Se ha cargado una nueva película', 'movie':[movie.dict() for m in movies]})

@app.put('/movies/{id}', tags=['Movies'], status_code=200)
def update_movie(id:int, movie:Movie):
    '''docstring'''
    for item in movies:
        if item["id"] == id:
            item['title'] = movie.title,
            item['overview'] = movie.overview,
            item['year'] = movie.year,
            item['rating'] = movie.rating,
            item['category'] = movie.category,
            return JSONResponse(content={'message':'Se ha actualizado la película'})
        
@app.delete('/movies/{id}', tags=['Movies'], status_code=200)
def delete_movie(id:int):
    '''docstring'''
    for item in movies:
        if item["id"]== id:
            movies.remove(item)
            return JSONResponse(content={'message':'Se ha eliminado la película'})