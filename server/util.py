# import json
# import pickle
# import numpy as np

# locations = None
# __data_columns = None
# __model = None

# def get_estimated_price(location, sqft, bhk, bath):
#     """
#     Predicts the estimated price of a property based on the location, square footage,
#     number of bedrooms, and number of bathrooms.

#     Args:
#     location (str): The location of the property.
#     sqft (float): The total square footage of the property.
#     bhk (int): The number of bedrooms.
#     bath (int): The number of bathrooms.

#     Returns:
#     float: The estimated price of the property.
#     """
#     try:
#         # Find the index of the location in data columns
#         loc_index = __data_columns.index(location.lower())
#     except ValueError:
#         # If location not found, set loc_index to -1
#         loc_index = -1

#     # Create an input array initialized to zero
#     x = np.zeros(len(__data_columns))
#     x[0] = sqft  # Set square footage
#     x[1] = bath  # Set number of bathrooms
#     x[2] = bhk   # Set number of bedrooms

#     # If location exists in columns, set its position to 1
#     if loc_index >= 0:
#         x[loc_index] = 1

#     # Return the prediction rounded to two decimal places
#     return round(__model.predict([x])[0], 2)

# def get_location_names():
#     """
#     Returns the list of location names from the dataset.

#     Returns:
#     list: List of location names.
#     """
#     return __locations

# def load_saved_artifacts():
#     """
#     Loads the saved artifacts (model and column data) required for predictions.
#     """
#     print("Loading saved artifacts...")
#     global __data_columns
#     global __locations
#     global __model

#     with open("./artifacts/columns.json", 'r') as f:
#         __data_columns = json.load(f)['data_columns']
#         __locations = __data_columns[3:]  # Extract location names starting from index 3

#     with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
#         __model = pickle.load(f)
#     print("Loading saved artifacts done.")

# if __name__ == '__main__':
#     # Load the saved artifacts
#     load_saved_artifacts()
#  # Print all available locations
#     print("Available Locations:", get_location_names())
import json
import pickle
import numpy as np

locations = None
__data_columns = None
__model = None
__locations = None  # Ensure this is initialized

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())  # Find the index of the location in data columns
    except ValueError:
        loc_index = -1  # If location not found, set loc_index to -1

    x = np.zeros(len(__data_columns))  # Create an input array initialized to zero
    x[0] = sqft  # Set square footage
    x[1] = bath  # Set number of bathrooms
    x[2] = bhk   # Set number of bedrooms

    if loc_index >= 0:
        x[loc_index] = 1  # If location exists in columns, set its position to 1

    return round(__model.predict([x])[0], 2)  # Return the prediction rounded to two decimal places

def get_location_names():
    # Ensure that the locations are loaded before returning
    if __locations is None:
        raise ValueError("Location data is not loaded. Please load the saved artifacts first.")
    return __locations

def load_saved_artifacts():
    print("Loading saved artifacts...")
    global __data_columns
    global __locations
    global __model

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # Extract location names starting from index 3

    with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)

    print("Loading saved artifacts done.")

if __name__ == '__main__':
    load_saved_artifacts()  # Ensure that the artifacts are loaded before calling functions

    print("Available Locations:", get_location_names())  # This should print locations correctly
    print("Estimated Price:", get_estimated_price('2nd stage nagarbhavi', 1000, 2, 2))
  

    # Call get_estimated_price with inputs
    print("Estimated Price:", get_estimated_price('2nd stage nagarbhavi',1000, 2, 2))
    print("Estimated Price:", get_estimated_price('whitefield',1000, 2, 2))
    print("Estimated Price:", get_estimated_price('yelahanka',1000, 2, 2))
    print("Estimated Price:", get_estimated_price('rayasandra',1000, 2, 2))
