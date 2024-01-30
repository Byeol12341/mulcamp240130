# -*- coding:utf-8 -*-

import streamlit as st
import seaborn as sns
import pandas as pd


# 원본 데이터 파일 경로
order_products__prior_path = "order_products__prior.csv/order_products__prior.csv"

# 데이터 읽기
df = pd.read_csv(order_products__prior_path)

# 무작위 샘플 추출 (예: 100개의 행)
sampled_df = df.sample(n=100, random_state=42)

# 새로운 파일로 저장
sampled_file_path = "sampled_data.csv"
sampled_df.to_csv(sampled_file_path, index=False)

@st.cache_data
def load_data():
    df = sns.load_dataset('iris')
    return df

def main():
    st.title("Hello World on Streamlit.io")
    iris = load_data()
    st.table(iris)


if __name__ == "__main__":
    main()

