import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/soupa/jupython/AI/deploy/beanmodel.pkl', 'rb'))


# creating a function for Prediction

def dry_bean(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    return prediction

def main():
    # giving a title
    st.title('Dry Bean Classification Web Application')

    # getting the input data from the user
    Area = st.text_input('Area')
    Perimeter =st.text_input('Perimeter')
    MajorAxisLength = st.text_input('MajorAxisLength')
    MinorAxisLength = st.text_input('MinorAxisLength ')
    AspectRation = st.text_input('AspectRation')
    Eccentricity = st.text_input('Eccentricity')
    ConvexArea = st.text_input('ConvexArea ')
    EquivDiameter = st.text_input('EquivDiameter')
    Extent = st.text_input('Extent')
    Solidity = st.text_input(' Solidity')
    roundness = st.text_input('roundness')
    Compactness = st.text_input('Compactness')
    ShapeFactor1 = st.text_input('ShapeFactor1')
    ShapeFactor2 = st.text_input('ShapeFactor2')
    ShapeFactor3 = st.text_input('ShapeFactor3')
    ShapeFactor4 = st.text_input('ShapeFactor4')


    # code for Prediction
    dry__bean = ' '

    # creating a button for Prediction

    if st.button('PREDICT_BEAN'):
       dry__bean= dry_bean(
            [Area,Perimeter,MajorAxisLength,MinorAxisLength,AspectRation,Eccentricity,ConvexArea,
             EquivDiameter,Extent,Solidity,roundness,Compactness,ShapeFactor1,ShapeFactor2,
             ShapeFactor3,ShapeFactor4])
    st.success(dry__bean)
    st.write('The predicted class of the bean is: ')

if __name__ == '__main__':
    main()