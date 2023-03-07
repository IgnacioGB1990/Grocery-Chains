alimentacion = {
    "Shushi":"https://www.alcampo.es/compra-online/frescos/sushi/c/W140502?q=%3Arelevance&page=0"
    "Leche Huevos Yogures y Lácteos": "https://www.alcampo.es/compra-online/alimentacion/leche-huevos-yogures-y-lacteos/c/W16?q=%3Arelevance&page=0",
    "Conservas": "https://www.alcampo.es/compra-online/alimentacion/conservas/c/W1004?q=%3Arelevance&page=0",
    #  "Caldos, Pasta, Arroz Legumbres Puré": "https://www.alcampo.es/compra-online/alimentacion/c/WC10?q=%3Arelevance%3AcategoryChild%3AW140",
    #  "Aceite Vinagre Salsas Especias": "https://www.alcampo.es/compra-online/alimentacion/c/WC10?q=%3Arelevance%3AcategoryChild%3AW18",
    #  "Comida Internacional":"https://www.alcampo.es/compra-online/alimentacion/c/WC10?q=%3Arelevance%3AcategoryChild%3AW9410",
    #  "Azúcar Harina Masas y Pan": "https://www.alcampo.es/compra-online/alimentacion/c/WC10?q=%3Arelevance%3AcategoryChild%3AW1009",
    #  "Desayuno y Merienda": "https://www.alcampo.es/compra-online/alimentacion/c/WC10?q=%3Arelevance%3AcategoryChild%3AW10",
    #  "Aperitivos, aceitunas y frutos secos":"https://www.alcampo.es/compra-online/alimentacion/c/WC10?q=%3Arelevance%3AcategoryChild%3AW120",
    #  "Alimentos Especiales":"https://www.alcampo.es/compra-online/alimentacion/c/WC10?q=%3Arelevance%3AcategoryChild%3AW33",
    #  "Supermercado Ecológico":"https://www.alcampo.es/compra-online/alimentacion/c/WC10?q=%3Arelevance%3AcategoryChild%3AW26112021",
    #  "Nutrición deportiva":"https://www.alcampo.es/compra-online/alimentacion/c/WC10?q=%3Arelevance%3AcategoryChild%3AW12",
    #  "Veganos":"https://www.alcampo.es/compra-online/alimentacion/c/WC10?q=%3Arelevance%3AcategoryChild%3AW09112021",
    #  "Productos sin gluten": "https://www.alcampo.es/compra-online/alimentacion/c/WC10?q=%3Arelevance%3AcategoryChild%3AW8",
    #  "Productos sin lactosa":"https://www.alcampo.es/compra-online/alimentacion/c/WC10?q=%3Arelevance%3AcategoryChild%3AW7"
}

frescos = {
    "Plátanos y Bananas": "https://www.alcampo.es/compra-online/frescos/frutas/c/W1701?q=%3Arelevance%3AcategoryChild%3AW170104",
    "Cítricos": "https://www.alcampo.es/compra-online/frescos/frutas/c/W1701?q=%3Arelevance%3AcategoryChild%3AW170101",
    "Tropicales y Exóticas":"https://www.alcampo.es/compra-online/frescos/frutas/c/W1701?q=%3Arelevance%3AcategoryChild%3AW170106",
    "Fresón y frutas del bosque":"https://www.alcampo.es/compra-online/frescos/frutas/c/W1701?q=%3Arelevance%3AcategoryChild%3AW170109",
    "Frutas de temporada":"https://www.alcampo.es/compra-online/frescos/frutas/c/W1701?q=%3Arelevance%3AcategoryChild%3AW170105",
    "Peras y Manzanas":"https://www.alcampo.es/compra-online/frescos/frutas/c/W1701?q=%3Arelevance%3AcategoryChild%3AW170102001",
    "Sandías y Melones":"https://www.alcampo.es/compra-online/frescos/frutas/c/W1701?q=%3Arelevance%3AcategoryChild%3AW170110",
    "Fruta cortada":"https://www.alcampo.es/compra-online/frescos/frutas/c/W1701?q=%3Arelevance%3AcategoryChild%3AW170105003",
    "Frutas ecológicas":"https://www.alcampo.es/compra-online/frescos/frutas/c/W1701?q=%3Arelevance%3AcategoryChild%3AW170107",
    "Puré y snacks de frutas": "https://www.alcampo.es/compra-online/frescos/frutas/c/W1701?q=%3Arelevance%3AcategoryChild%3AWPureSnacksFrutas",
    "Zumo exprimido": "https://www.alcampo.es/compra-online/frescos/frutas/c/W1701?q=%3Arelevance%3AcategoryChild%3AW12082022",
    "Fruta Premium": "https://www.alcampo.es/compra-online/frescos/frutas/c/W1701?q=%3Arelevance%3AcategoryChild%3AW101020221"
}

generica = "https://www.alcampo.es/compra-online/alimentacion/c/WC10"


import pygame
from pygame import mixer

def playSound():
    mixer.init()
    mixer.music.load("././assets/completed.mp3")
    mixer.music.set_volume(0.4)
    mixer.music.play()


