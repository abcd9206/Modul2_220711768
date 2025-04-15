import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    """
    Load and cache the dataset from file
    """
    df = pd.read_csv('D:\\Kuliah\\Semester 6\\Pengolahan Bahasa Alami\\Modul2_220711768\\multilabel\\data\\train_preprocess.csv')
    return df
