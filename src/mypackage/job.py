from unicodedata import name
from kivy.app import App
from kivy.uix.label import Label
import json


# Ekrana yazı yazar

class Yazbel(App):
    def build(self):
        yazi = Label(text = "Hello :D",font_size = "25sp",color = [0,.3,.9,1])
        return yazi

Yazbel().run()



# Değer girilip toplamaya yarar ve Json dosyası olarak döndürür

def topla():
    a = int(input("Deger giriniz"))
    b = int(input("Deger giriniz"))
    c = a + b
    x = {
      "name": "Nasuh Eren Demirci",
      "sonuc": c
    }
    y = json.dumps(x)
    print(y)
topla()
