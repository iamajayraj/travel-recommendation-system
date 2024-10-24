import streamlit as st
import pandas as pd
import pickle

packages = pickle.load(open('packages.pkl','rb'))
packages = pd.DataFrame(packages)
similarity = pickle.load(open('similarity.pkl','rb'))
data = pickle.load(open('data.pkl','rb'))
data = pd.DataFrame(data)

no_img = 'https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg'
packages['poster_url'] = packages['poster_url'].fillna(no_img)

def recommend(place):
    index = packages[packages['package_name'] == place].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])

    package = []
    package_poster = []
    for i in distances[1:6]:
        package.append(packages.iloc[i[0]].package_name)
        package_poster.append(packages.iloc[i[0]].poster_url)

    return package,package_poster


st.title('Travel Destinations Recommender')
selected_package = st.selectbox('Please select a package',packages['package_name'])

if st.button('Recommend'):
    pack,pos = recommend(selected_package)


    st.header('1. '+pack[0])
    st.image(pos[0])
    st.header(' ')


    st.header('2. '+pack[1])
    st.image(pos[1])
    st.header(' ')


    st.header('3. '+pack[2])
    st.image(pos[2])



