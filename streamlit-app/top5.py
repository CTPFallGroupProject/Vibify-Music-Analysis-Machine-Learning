def get_results(df, results, cleaned_X):
    import pandas as pd
    import re

    output_list = []

    for i in results.argsort()[:-6:-1]:
        if results[i] > 0:
            res_string = str("{} with {}% match".format(
                df.loc[i].song_by_artist, round(100*results[i])))
            output_list.append(res_string)
    return output_list


def top5_func(cleaned_X):

    import numpy as np
    import pandas as pd
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.feature_extraction.text import TfidfTransformer
    from sklearn.metrics.pairwise import cosine_similarity
    from scipy import sparse
    from cleaning_data import clean_data
    import pickle

    df = pd.read_csv('https://drive.google.com/file/d/1Txh9TCzWfEc9ermiwQqYAljGyfml1Pxj/view?usp=share_link')
    df.dropna(inplace=True)

    model = pickle.load(open('streamlit-app/top5.pkl', 'rb'))
    query_term_matrix = model.transform([cleaned_X])
    
    tf_idfs = sparse.load_npz('streamlit-app/data/tf_idfs_top5.npz')

    results = cosine_similarity(tf_idfs, query_term_matrix)
    results = results.reshape((-1,))

    output_list = get_results(df, results, cleaned_X)
    return output_list

    
