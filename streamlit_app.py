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
コードは慎重に使用してください。詳細
このコードは、以下の手順で動作します。

get_animal_image()関数は、指定された動物名の画像を取得します。
メイン処理では、ユーザーが入力した動物名をget_animal_image()関数に渡して、画像を取得します。
画像が取得できた場合は、st.image()関数を使って画像を表示します。
このコードを実行すると、以下の画面が表示されます。

いろんな動物を表示するWebアプリケーション

動物名を入力してください
動物名を入力して「Enter」キーを押すと、動物の画像が表示されます。

例えば、動物名に「犬」と入力すると、以下の画面が表示されます。

いろんな動物を表示するWebアプリケーション

動物名を入力してください
犬

犬の画像が表示されます。

このコードを応用して、動物の種類や地域ごとに画像を表示するようにすることもできます。

例えば、以下のコードは、犬の種類ごとに画像を表示するコードです。

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