import streamlit as st
import pytube


st.title('Mp4 Shortcut Downloader')

url=st.text_input("Lütfen İndireceniz video adresi giriniz")


if len(url)>0:

                sonuc=pytube.YouTube(url).streams.first().download()

                with open(sonuc, "rb") as file:
                    btn = st.download_button(
                            label="Videoyu indir",
                            data=file,
                            file_name="video.mp4",
                            mime="video/mp4"
                          )




