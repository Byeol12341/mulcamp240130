# -*- coding:utf-8 -*-

import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
# def load_data():
#     df = pd.read_csv('./data/sampled_data.csv').dropna()
#     return df



# def main():
#     st.title("order_products__prior")
#     df = load_data()
#     st.table(df)

def load_data2():
    df2 = pd.read_csv('./sample_order_products_train.csv').dropna()
    return df2

def main():    
    st.text('products_train')
    df2 = load_data2()
    st.table(df2)

    # 행 추출
    # st.write(df2.loc[df2['product_id']])
    # val = st.selectbox("1개의 product_id를 선택하세요!!", df2.product_id.unique())
    # st.write("선택된 product_id:", val)
    
    # result = df2.loc[df2['product_id'] == val, :].reset_index(drop=True)
    # st.data_editor(result)
    
    cols = st.multiselect("복수의 컬럼을 선택하세요!!", df2.columns)
    st.dataframe(df2.loc[:, cols])
    st.write("add_to_cart_order & reordered")
    fig, ax = plt.subplots() # sidebar 밖에 있는 그림
    ax.scatter(df2['add_to_cart_order'], df2['reordered'])
    st.pyplot(fig)



add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)


with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )


if __name__ == "__main__":
    main()

with st.container():
   container = st.container(border=True)
   container.write("This is inside the container")
   st.write("This is outside the container")