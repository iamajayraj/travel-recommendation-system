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

if st.button('Recommend',type='primary'):
    pack,pos = recommend(selected_package)

    st.header('1. '+pack[0])
    st.image(pos[0])

    with st.expander(f"🌎 {pack[0]} - {data[data['package_name']==pack[0]]['price_per_person'].values[0]}₹  per person"):
        st.write("##### 📅 Stay Duration")
        st.write(f"{data[data['package_name']==pack[0]]['stay_duration'].values[0]} Nights and {data[data['package_name']==pack[0]]['stay_duration'].values[0]+1} Days")

        # Assuming 'cities' is a list of strings for each package
        cities = data[data['package_name']==pack[0]]['cities_covered_with_duration'].values[0]
        # Convert facilities to a Markdown-formatted bullet list
        st.markdown("### 🏙 Cities Covered")
        for city in cities:
            st.markdown(f"- {city}")

        # Assuming 'facilities' is a list of strings for each package
        facilities = data[data['package_name'] == pack[0]]['facilities'].values[0]
        # Convert facilities to a Markdown-formatted bullet list
        st.markdown("### 🛎 Facilities")
        for facility in facilities:
            st.markdown(f"- {facility}")


        # Assuming 'sights' is a list of strings for each package
        sights = data[data['package_name'] == pack[0]]['sights_included'].values[0]
        # Convert sights to a Markdown-formatted bullet list
        st.markdown("### 📸 Sights")
        for sight in sights:
            st.markdown(f"- {sight}")



        col1, col2 = st.columns([2, 1])
        with col1:
            st.write("### 💲 Price Per Person")
            price = data[data['package_name']==pack[0]]['price_per_person'].values[0]
            st.markdown(f"<h4 style='margin-left: 40px;'>{price}₹</h4>", unsafe_allow_html=True)

        with col2:
            st.header(' ')
            st.button('🧳 Book Now',key='package_1')

        st.markdown("---")  # Separator between packages

    st.header(' ')


    st.header('2. '+pack[1])
    st.image(pos[1])
    with st.expander(f"🌎 {pack[1]} - {data[data['package_name']==pack[1]]['price_per_person'].values[0]}₹  per person"):
        st.write("##### 📅 Stay Duration")
        st.write(f"{data[data['package_name']==pack[1]]['stay_duration'].values[0]} Nights and {data[data['package_name']==pack[1]]['stay_duration'].values[0]+1} Days")

        # Assuming 'cities' is a list of strings for each package
        cities = data[data['package_name']==pack[1]]['cities_covered_with_duration'].values[0]
        # Convert facilities to a Markdown-formatted bullet list
        st.markdown("### 🏙 Cities Covered")
        for city in cities:
            st.markdown(f"- {city}")

        # Assuming 'facilities' is a list of strings for each package
        facilities = data[data['package_name'] == pack[1]]['facilities'].values[0]
        # Convert facilities to a Markdown-formatted bullet list
        st.markdown("### 🛎 Facilities")
        for facility in facilities:
            st.markdown(f"- {facility}")


        # Assuming 'sights' is a list of strings for each package
        sights = data[data['package_name'] == pack[1]]['sights_included'].values[0]
        # Convert sights to a Markdown-formatted bullet list
        st.markdown("### 📸 Sights")
        for sight in sights:
            st.markdown(f"- {sight}")



        col1, col2 = st.columns([2, 1])
        with col1:
            st.write("### 💲 Price Per Person")
            price = data[data['package_name']==pack[1]]['price_per_person'].values[0]
            st.markdown(f"<h4 style='margin-left: 40px;'>{price}₹</h4>", unsafe_allow_html=True)

        with col2:
            st.header(' ')
            st.button('🧳 Book Now',key='package_2')

        st.markdown("---")  # Separator between packages
    st.header(' ')


    st.header('3. '+pack[2])
    st.image(pos[2])
    with st.expander(f"🌎 {pack[2]} - {data[data['package_name']==pack[2]]['price_per_person'].values[0]}₹  per person"):
        st.write("##### 📅 Stay Duration")
        st.write(f"{data[data['package_name']==pack[2]]['stay_duration'].values[0]} Nights and {data[data['package_name']==pack[2]]['stay_duration'].values[0]+1} Days")

        # Assuming 'cities' is a list of strings for each package
        cities = data[data['package_name']==pack[2]]['cities_covered_with_duration'].values[0]
        # Convert facilities to a Markdown-formatted bullet list
        st.markdown("### 🏙 Cities Covered")
        for city in cities:
            st.markdown(f"- {city}")

        # Assuming 'facilities' is a list of strings for each package
        facilities = data[data['package_name'] == pack[2]]['facilities'].values[0]
        # Convert facilities to a Markdown-formatted bullet list
        st.markdown("### 🛎 Facilities")
        for facility in facilities:
            st.markdown(f"- {facility}")


        # Assuming 'sights' is a list of strings for each package
        sights = data[data['package_name'] == pack[2]]['sights_included'].values[0]
        # Convert sights to a Markdown-formatted bullet list
        st.markdown("### 📸 Sights")
        for sight in sights:
            st.markdown(f"- {sight}")

        col1,col2 = st.columns([2,1])
        with col1:
            st.write("### 💲 Price Per Person")
            price = data[data['package_name']==pack[2]]['price_per_person'].values[0]
            st.markdown(f"<h4 style='margin-left: 40px;'>{price}₹</h4>", unsafe_allow_html=True)


        with col2:
            st.header(' ')
            st.button('🧳 Book Now',key='package_3')

        st.markdown("---")  # Separator between packages




