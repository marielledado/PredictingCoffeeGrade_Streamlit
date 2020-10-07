import joblib
import numpy as np
import pandas as pd
import streamlit as st

st.beta_set_page_config(page_title="Predicting Specialty Coffee", page_icon="☕")



def predict_score(altitude, region, processing, variety):
    # Random Forest, Accuracy: 0.86 (CV) 0.88 (Hold-out)
    coffee_clf = joblib.load('./model/coffee_clf.joblib')
    input = pd.DataFrame({"altitude": [altitude], "region": [region], "processing": [processing], "variety": [variety]})
    return coffee_clf.predict(input)

def main():

    st.image('./photo/coffeeheader.jpg')

    # Text main
    st.title("☕ How special is your specialty coffee?")
    st.markdown("Find out if your specialty coffee beans (Arabica & single origin only) are *very good* or *excellent* according to the [Specialty Coffee Association](https://sca.coffee/research/protocols-best-practices).")
    # Sidebar
    st.sidebar.title("What is specialty coffee?")
    st.sidebar.markdown("Coffee is considered 'specialty' grade when professional coffee tasters (aka [Q-graders](https://www.coffeeinstitute.org/our-work/a_common_language/what-is-a-q-grader/)) give it a score of 80 or higher. Specialty coffees scoring between 80-84.99 are considered *very good* coffees; coffee scoring 85 or more are considered *excellent* coffees.")

    st.sidebar.title("How does this app work?")
    st.sidebar.markdown("Enter the altitude, region of origin, processing method and variety of your coffee (you can find this info on most specialty coffee bag labels or on the roasters' website).")

    # Input fields
    altitude = st.number_input("Elevation/Altitude", min_value=600)

    region_options = ("North America", "Central America", "South America", "Brazil", "Africa", "Asia Pacific")
    region = st.selectbox("Region", region_options)

    
    processing_options = ("Washed / Wet", "Natural / Dry", "Semi-Washed / Honey", "Other")
    processing = st.selectbox("Processing Method", processing_options)

    variety_options = ("Ethiopian Varieties", "Typica", "Bourbon", "Bourbon/Typica", "Catimor", "Others")
    variety = st.selectbox("Arabica Variety", variety_options)
    st.markdown("ℹ️ Can't find your coffee variety on the list? [Look it up in this catalog](https://varieties.worldcoffeeresearch.org/varieties), find its 'Genetic Description' and choose that as your option (e.g., [Catuai](https://varieties.worldcoffeeresearch.org/varieties/catuai) is in the 'Bourbon-Typica' group)")
    
    if st.button("Submit"): 
        result = predict_score(altitude, region, processing, variety)
        if result == np.array(1):
            st.success(f"Wow, you've got some EXCELLENT specialty coffee right there!☕🎉")
        elif result == np.array(0):
            st.success(f"That's some VERY GOOD specialty coffee right there!☕")

    st.info("""\
        Made with ☕ by [Marielle Dado](https://www.marielledado.com) | [GitHub Repo](https://www.github.com/marielledado) 
        | Data scraped from [Coffee Quality Institute](https://database.coffeeinstitute.org/)
    """)


     
if __name__=='__main__': 
    main() 