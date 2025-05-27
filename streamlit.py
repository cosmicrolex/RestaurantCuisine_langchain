import streamlit  as st
import langchainfunction

st.title("Restaurant Name")

#the sidebar function returns what you picked.
cuisine = st.sidebar.selectbox("Pick a cuisine" , ("Indian" , "American" , "Italian" , "Mexican" , "French","Taiwanese"))


if cuisine:
    response = langchainfunction.generate_restaurant_name_and_items(cuisine)
    st.header(response['Restaurant_name'])
    menu_items =response['dishes'].split(",")
    st.write("**Menue Items**")
    for item in menu_items:
        st.write("-",item)
