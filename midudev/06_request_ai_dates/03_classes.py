# 1. Introducción a las Clases en Python
# Las clases son plantillas para crear objetos. Un objeto es una instancia de una clase.
# Nos permite agrupar datos (atributos o propiedades) y funciones (métodos) en un solo lugar.

OPENAI_KEY = ""
DEEPSEEK_API_KEY = ""

class Car:
    car_type = "This is a car"
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def drive(self):
      print(f"Driving {self.brand} {self.model} {self.year}")

car1 = Car("Toyota", "Corolla", 2020)
car1.drive()

car2 = Car("Ford", "Mustang", 2021)
car2.drive()

car3 = Car("Chevrolet", "Camaro", 2022)
car3.drive()

print(car1.car_type)
print(car2.car_type)
print(car3.car_type)


# Encapsulación: es ocultar los detalles internos de una clase y exponer solo la interfaz pública

# Crear una clase para llamar a la AI de OpenAI, DeepSeek O LO QUE SEA

import requests

class AI_API:
  def __init__(self, api_key, url, model):
    self.api_key = api_key
    self.url = url
    self.model = model

  def call(self, prompt):
    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {self.api_key}"
    }
    data = {
      "model": self.model,
      "messages": [{"role": "user", "content": prompt}]
    }

    try:
      response = requests.post(self.url, json=data, headers=headers)
      res_json = response.json()
      print(res_json["choices"][0]["message"]["content"])
    except requests.exceptions.RequestException as e:
      print(f"Error en la solicitud: {e}")
      return None

print("\nOPEN_AI:")
openai_api = AI_API(OPENAI_KEY, "https://api.openai.com/v1/chat/completions", "gpt-4o-mini")

openai_api.call("Escribe un breve poema sobre la programación")

print("\nDEEPSEEK:")
deepseek_api = AI_API(DEEPSEEK_API_KEY, "https://api.deepseek.com/chat/completions", "deepseek-chat")

deepseek_api.call("Escribe un breve poema sobre la programación")