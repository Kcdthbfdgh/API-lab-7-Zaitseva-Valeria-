#Вариант 7 Лаб 7 Зайцева Валерия 502667
#№1
import requests
import json
#print(requests.__version__)

Api_key = "644cefbbcc19c50f9fd8debd75f1dd87"
city_name = "Tokyo,JP"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={Api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)

    #вывод инф
    print(f"Город: {data['name']}")
    print(f"Страна: {data['sys']['country']}")
    print(f"Погода: {data['weather'][0]['description'].title()}")
    print(f"Температура: {data['main']['temp']} Degrees")
    print(f"Ощущается как: {data['main']['feels_like']} Degrees")
    print(f"Влажность: {data['main']['humidity']}%")
    print(f"Давление: {data['main']['pressure']} hPa")
else:
    print(f"Ошибка: {response.status_code}")
#№2 к сожалению, нет платного доступа, чтобы посмотреть список праздников... поэтому далее сделаю другой вариант.
#Вариант 5 для бесплатного доступа API не нужен ключ
#Ввод слова
word = input("Введите слово для поиска: ").strip()

url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

try:
    response = requests.get(url)
    response.raise_for_status()  #успешен ли запрос
    data = response.json()

    #первый результат
    entry = data[0]

    print(f"\nСлово: {entry.get('word')}")
    print(f"Фонетика: {entry.get('phonetic', 'нет данных')}")

    #первое значение части речи
    meanings = entry.get('meanings', [])
    if meanings:
        first_meaning = meanings[0]
        print(f"Часть речи: {first_meaning.get('partOfSpeech', 'нет данных')}")
        #Определения
        definitions = first_meaning.get('definitions', [])
        if definitions:
            first_def = definitions[0]
            print(f"Определение: {first_def.get('definition', 'нет данных')}")
            print(f"Пример: {first_def.get('example', 'нет данных')}")
            synonyms = first_def.get('synonyms', [])
            print(f"Синонимы: {', '.join(synonyms) if synonyms else 'нет данных'}")
    else:
        print("Нет информации")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP ошибка: {http_err}")
except requests.exceptions.RequestException as err:
    print(f"Ошибка запроса: {err}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
#№3 доп
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
from io import BytesIO


def load_new_image():
    url = "https://nekos.best/api/v2/neko"
    response = requests.get(url).json()

    image_url = response["results"][0]["url"]
    img_response = requests.get(image_url)

    img = Image.open(BytesIO(img_response.content))
    img = img.resize((400, 400))

    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    label.image = photo


root = tk.Tk()
root.title("Генератор аниме")
root.geometry("450x500")

label = Label(root)
label.pack(pady=10)

button = Button(root, text="Следующая картинка", command=load_new_image)
button.pack(pady=10)

load_new_image()

root.mainloop()