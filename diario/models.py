from django.db import models

class Escritor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Tema(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Entrada(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    escritor = models.ForeignKey(Escritor, on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo
