'''docstring'''
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI(
    title ='Aprendiendo FastApi',
    description = 'Primeros pasos de una Api',
    version= '0.0.1',
)

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
    return movies

@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int):
    '''docstring'''
    for item in movies:
        if item["id"] == id:
            return item
    return []

@app.get('/movies/', tags=['Movies'])
def get_movies_by_category(category: str):
    '''docstring'''
    return category

@app.post('/movies', tags=['Movies'])
def create_movie(
    id: int = Body(),
    title: str = Body(),
    overview: str = Body(),
    year: int = Body(),
    rating: float = Body(),
    category: str = Body()
):
    '''docstring'''
    movies.append({
  "id": id,
  "title": title,
  "overview": overview,
  "year": year,
  "rating": rating,
  "category": category
})
    print(movies)
    return title

@app.put('/movies/{id}', tags=['Movies'])
def update_movie(
    id: int,
    title: str = Body(),
    overview: str = Body(),
    year: int = Body(),
    rating: float = Body(),
    category: str = Body()
):
    '''docstring'''
    for item in movies:
        if item["id"] == id:
            item['title'] = title,
            item['overview'] = overview,
            item['year'] = year,
            item['rating'] = rating,
            item['category'] = category,
            return movies
        
@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id:int):
    '''docstring'''
    for item in movies:
        if item["id"]== id:
            movies.remove(item)
            return movies