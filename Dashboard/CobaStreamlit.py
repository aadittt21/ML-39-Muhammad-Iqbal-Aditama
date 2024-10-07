# Import library yang diperlukan
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import read_csv

# Membuat judul aplikasi
st.title("Gambar Grafik")
 
col1, col2, col3, col4 = st.columns(4)
 
with col1:
    st.header("Gambar 1")
    st.image("D:\Kuliah\Bangkit\Proyek Dicoding\download (1).png")
    st.caption('Grafik 3D')
with col2:
    st.header("Gambar 2")
    st.image("D:\Kuliah\Bangkit\Proyek Dicoding\download (2).png")
    st.caption('Grafik Cluster')
with col3:
    st.header("Gambar 3")
    st.image("D:\Kuliah\Bangkit\Proyek Dicoding\download (3).png")
    st.caption('Grafik Centroid')
with col4:
    st.header("Gambar 4")
    st.image("D:\Kuliah\Bangkit\Proyek Dicoding\download.png")
    st.caption('Grafik Plot')