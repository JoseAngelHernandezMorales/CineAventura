from django.test import TestCase
from .models import Pelicula, Genero, Director

class PeliculaModelTest(TestCase):
    def setUp(self):
        # Crear género de prueba
        self.genero = Genero.objects.create(
            nombre="Sci-Fi",
            descripcion="Género ciencia ficción"
        )

        # Crear director de prueba
        self.director = Director.objects.create(
            nombre="Christopher Nolan",
            biografia="Director famoso"
        )

        # Crear película SIN generos aún, porque es ManyToMany
        self.pelicula = Pelicula.objects.create(
            titulo="Interestelar",
            sinopsis="Película espacial",
            año=2014,
            duracion=169,
            pais="USA",
            idioma="Inglés",
            fecha_estreno="2014-11-07",
            presupuesto=160000000.00,
            recaudacion=677471339.00,
            clasificacion="PG-13"
        )

        # Asignar géneros después de crearla:
        self.pelicula.generos.add(self.genero)

    def test_pelicula_creacion(self):
        self.assertEqual(self.pelicula.titulo, "Interestelar")

    def test_pelicula_str(self):
        self.assertIn("Interestelar", str(self.pelicula))