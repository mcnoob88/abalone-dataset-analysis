import pickle
import streamlit as st 
import joblib

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("model.pkl","rb")
model=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(length, diameter, height, whole_weight, shucked_weight,
       viscera_weight, shell_weight):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
        -   name: Length
            in: query
            type: number
            required: true
        -   name: Diameter
            in: query
            type: number
            required: true
        -   name: Height
            in: query
            type: number
            required: true
        -   name: Whole_weight
            in: query
            type: number
            required: true
        -   name: Shucked_weight
            in: query
            type: number
            required: true
        -   name: Viscera_weight
            in: query
            type: number
            required: true
        -   name: Shell_weight
            in: query
            type: number
            required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=model.predict([[length, diameter, height, whole_weight, shucked_weight,
       viscera_weight, shell_weight]])
    print(prediction)
    return prediction



def main():
    st.title("Bank Authenticator")

    length = st.text_input("length","Type Here")
    diameter = st.text_input("diameter","Type Here")
    height = st.text_input("height","Type Here")
    whole_weight = st.text_input("whole_weight","Type Here")
    shucked_weight = st.text_input("shucked_weight","Type Here")
    viscera_weight = st.text_input("viscera_weight","Type Here")
    shell_weight = st.text_input("shell_weight","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(length, diameter, height, whole_weight, shucked_weight,
       viscera_weight, shell_weight)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()