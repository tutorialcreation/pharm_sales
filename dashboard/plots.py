import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scripts.database import DBOps
sns.set()

def view_predictions(page=None,results=None):
    if st.session_state.page_select == page:
        
        st.subheader('Predictions Chart')
        try:
            df = pd.read_csv("data/cleaned_train_batch.csv")
            df.reset_index(drop=True)
            if df.empty:
                st.error("Please upload batch files to view predictions")    
            fig = plt.figure(figsize=(10, 4))
            sns.lineplot(data=df,x='Customers',y='sales_prediction')
            st.pyplot(fig)
        except Exception as e:
            st.error(f'{e} - this means there is no batch prediction you have made start by \
                making uploading a file, make a batch prediction and then come back and view the forecast \
                    you shall find me here waiting for you')