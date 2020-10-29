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
    st.markdown("Find out whether your specialty coffee beans (Arabica & single origin only) are *very good* or *excellent* according to the [Specialty Coffee Association](https://sca.coffee/research/protocols-best-practices).")
   
    # Sidebar
    st.sidebar.title("What is specialty coffee?")
    st.sidebar.markdown("Single-origin arabica coffees are considered 'specialty' grade when given a score of 80 (out of 100) or higher by professional coffee tasters (aka [Q-graders](https://www.coffeeinstitute.org/our-work/a_common_language/what-is-a-q-grader/)). Coffees with a score between 80-84.99 are considered *very good* coffees; coffee scoring 85 or more are considered *excellent* coffees.")

    st.sidebar.title("How does this app work?")
    st.sidebar.markdown("Enter the altitude, region of origin, processing method and variety of your coffee. You can find this info on most specialty coffee bag labels or on the roasters' website (try it out [with this label](https://images.unsplash.com/photo-1592250819999-c00fed586048?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80)!).")
   

    # Input fields
    altitude = st.number_input("Elevation/Altitude", min_value=600)

    region_options = ("North America", "Central America", "South America", "Brazil", "Africa", "Asia Pacific")
    region = st.selectbox("Region", region_options)

    
    processing_options = ("Washed / Wet", "Natural / Dry", "Semi-Washed / Honey", "Other")
    processing = st.selectbox("Processing Method", processing_options)

    variety_options = ("Ethiopian Landrace (e.g., Heirloom, Gesha)", "Typica-Related (e.g., Typica, SL14)", "Bourbon-Related (e.g., Bourbon, Caturra, SL28)", "Bourbon & Typica-Related (e.g., Catuai)", "Catimor", "Others")
    variety = st.selectbox("Arabica Variety", variety_options)
    st.markdown("ℹ️ Can't find your coffee variety on the list? [Look it up in this catalog](https://varieties.worldcoffeeresearch.org/varieties), find its 'Genetic Description' and choose that as your option.")
    
    if st.button("Submit"): 
        result = predict_score(altitude, region, processing, variety)
        if result == np.array(1):
            st.success(f"Wow, you've got EXCELLENT specialty coffee right there!☕🎉")
        elif result == np.array(0):
            st.success(f"That's some VERY GOOD specialty coffee right there!☕")

    st.info("""\
        Made with ☕ by [Marielle Dado](https://www.marielledado.com) | [GitHub Repo](https://github.com/marielledado/PredictingCoffeeGrade_Streamlit) 
        | Data scraped from [Coffee Quality Institute](https://database.coffeeinstitute.org/)
    """)


     
if __name__=='__main__': 
    main() 