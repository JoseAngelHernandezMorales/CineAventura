import pytest
from django.contrib.auth.models import User
from peliculas.models import Genero, Director, Actor, Pelicula

@pytest.mark.django_db
def test_pelicula_generos():
    d = Director.objects.create(nombre="Peter Jackson")
    g = Genero.objects.create(nombre="Fantasía")
    p = Pelicula.objects.create(
        titulo="LOTR",
        sinopsis="Anillo único",
        año=2001,
        duracion=178,
        pais="NZ",
        idioma="English",
        fecha_estreno="2001-12-19",
        director=d
    )
    p.generos.add(g)
    assert p.generos.count() == 1