import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="Askeri Araç Tespit", layout="wide")
st.title("🛡️ Askeri Araç Tespit Dashboard")

uploaded_file = st.file_uploader("Fotoğraf seçin...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(image, use_container_width=True, caption="Orijinal Görsel")
    
    if st.button("Tespit Et"):
        with st.spinner('Analiz ediliyor...'):
            img_byte = io.BytesIO()
            image.save(img_byte, format='JPEG')
            
            try:
                res = requests.post("http://localhost:8000/detect/visual", files={'file': img_byte.getvalue()})
                if res.status_code == 200:
                    with col2:
                        st.image(res.content, use_container_width=True, caption="Tespit Sonucu")
                else:
                    st.error("API Hatası!")
            except Exception as e:
                st.error("Bağlantı Hatası: Docker API çalışmıyor olabilir.")
