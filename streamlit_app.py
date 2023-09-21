import streamlit as st
import requests
import json

# 動物の画像を取得する関数
def get_animal_image(animal_name):
    url = "https://api.thecatapi.com/v1/images/search?q=" + animal_name
    response = requests.get(url)
    data = json.loads(response.content)
    return data[0]["url"]

# メイン処理
st.title("いろんな動物を表示するWebアプリケーション")

# 動物名を入力する
animal_name = st.text_input("動物名を入力してください")

# 動物の画像を表示する
if animal_name != "":
    image_url = get_animal_image(animal_name)
    st.image(image_url)

Python
import streamlit as st
import requests
import json

# 動物の画像を取得する関数
def get_animal_image(animal_name):
    url = "https://api.thecatapi.com/v1/images/search?q=" + animal_name
    response = requests.get(url)
    data = json.loads(response.content)
    return data[0]["url"]

# メイン処理
st.title("いろんな犬の種類を表示するWebアプリケーション")

# 犬の種類を選択する
dog_types = ["柴犬", "ゴールデンレトリバー", "チワワ"]
dog_type = st.selectbox("犬の種類を選択してください", dog_types)

# 犬の画像を表示する
if dog_type != "":
    image_url = get_animal_image(dog_type)
    st.image(image_url)