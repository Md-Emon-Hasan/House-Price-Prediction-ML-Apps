import numpy as np
import pickle
import streamlit

# loaded the saved model
loaded_model = pickle.load(open("model.pkl",'rb'))

# creating a function for prediction
def house_price_prediction(input_data):
    # changing the input_data to numpu array
    input_data_as_numpy_array = np.array(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    return (f'House Price: {prediction}')
    
def main():
    # giving a title
    streamlit.title('Boston House Price Prediction ML Apps')
    streamlit.write('''***Made By Emon Hasan***''')
    
    # getting the input data from the users
    CRIM = streamlit.number_input('CRIM')
    ZN = streamlit.number_input('ZN')
    INDUS = streamlit.number_input('INDUS')
    CHAS = streamlit.number_input('CHAS')
    NOX = streamlit.number_input('NOX')
    RM = streamlit.number_input('RM')
    AGE = streamlit.number_input('AGE')
    DIS = streamlit.number_input('DIS')
    RAD = streamlit.number_input('RAD')
    TAX = streamlit.number_input('TAX')
    PTRATIO = streamlit.number_input('PTRATIO')
    B = streamlit.number_input('B')
    LSTAT = streamlit.number_input('LSTAT')
    
    # code for prediction
    house_price = ''
    
    if streamlit.button('House Price Prediction'):
        house_price = house_price_prediction([CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT])
    streamlit.success(house_price)
    
if __name__ == '__main__':
    main()