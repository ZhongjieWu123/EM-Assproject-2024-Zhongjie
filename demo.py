import os
from pathlib import Path
import pandas as pd
import numpy as np
import dill
from PIL import Image
import streamlit as st

from assproject.transforms import process_df


path_to_repo = Path(__file__).parent.resolve()
path_to_data = path_to_repo / 'data' / 'transformed'


def display_Quality(index):
    # compute model prediction
    pred_quality = st.session_state.model.predict([st.session_state.X.values[index]])[0]
    pred_quality = int(np.exp(pred_quality))
    true_quality = int(np.exp(st.session_state.y[index]))

    # display actual and predicted prices
    col_pred, col_gold = st.columns(2)
    with col_pred:
        st.subheader('estimated quality')
        st.write(str(pred_quality))
    with col_gold:
        st.subheader('real quality')
        st.write(str(true_quality))
    return


def display_Beers_features(index):
    st.subheader('Beer features')
    feat0, val0, feat1, val1 = st.columns([3.5, 1.5, 3.5, 1.5])
    row = st.session_state.X.values[index]
    location_mapping = {0: 'Electronic City', 1: 'HSR Layout', 2: 'Indiranagar', 
                        3: 'Jayanagar', 4: 'Koramangala', 5: 'Malleswaram', 
                        6: 'Marathahalli', 7: 'Rajajinagar', 
                        8: 'Whitefield', 9: 'Yelahanka'}
    for i, feature in enumerate(st.session_state.X.columns):
        ind = i % 2
        if ind == 0:
            with feat0:
                st.info(feature)
            with val0:
                st.success(str(row[i]))
        elif ind == 1:
            with feat1:
                st.info(feature)
            with val1:
                st.success(str(row[i]))
    return


def init_session_state():
    # session state
    if 'loaded' not in st.session_state:
        # validation set given in notebook
        n_valid = 20000

        # import raw data
        df_raw = pd.read_feather(path_to_data)

        # preprocess data
        X, y, nas = process_df(df_raw, 'Quality_Score')
        X, y = X[n_valid:], y[n_valid:]

        # load regression model
        path_to_model = os.path.join(path_to_repo, 'notebooks', 'RandomForest.pkl')
        with open(path_to_model, 'rb') as file:
            model = dill.load(file)

        # store in cache
        st.session_state.loaded = True
        st.session_state.n_valid = n_valid
        st.session_state.X = X
        st.session_state.y = y
        st.session_state.model = model


def app():
    init_session_state()
    st.title('Choose a BEER')
    options = ['-'] + list(range(1, st.session_state.n_valid + 1))
    index = st.selectbox(label = 'Choose a BEER index', options = options, index = 0)
    if index != '-':
        display_Quality(index)
        display_Beers_features(index)
    return


if __name__ == '__main__':
    app()