import streamlit as st
import requests
import json

# Liyuuの画像を取得する関数
def get_liyuu_image(liyuu_name, costume_name):
    url = "https://api.theliyuu.com/v1/images/search?q=" + liyuu_name + "&costume=" + costume_name
    response = requests.get(url)
    data = json.loads(response.content)
    return data[0]["url"]

# メイン処理
st.title("いろんなLiyuuの衣装を表示するWebアプリケーション")

# Liyuuの名前を選択する
liyuu_names = ["李宇春", "虞書欣", "周洁琼"]
liyuu_name = st.selectbox("Liyuuの名前を選択してください", liyuu_names)

# Liyuuの衣装を選択する
costume_names = ["紅装", "白装", "黑装"]
costume_name = st.selectbox("Liyuuの衣装を選択してください", costume_names)

# Liyuuの画像を表示する
if liyuu_name != "" and costume_name != "":
    image_url = get_liyuu_image(liyuu_name, costume_name)
    st.image(image_url)