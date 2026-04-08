import pickle
import pandas as pd

# load trained model
with open("ml/model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_object(speed, altitude, distance, direction):

    # convert direction text to number
    direction_map = {
        "approaching": 1,
        "hovering": 2,
        "leaving": 3
    }

    direction_value = direction_map[direction]

    # create dataframe
    data = pd.DataFrame([{
        "speed": speed,
        "altitude": altitude,
        "distance": distance,
        "direction": direction_value
    }])

    # predict object
    object_type = model.predict(data)[0]

    # confidence between 0 and 1
    confidence = max(model.predict_proba(data)[0])

    return object_type, confidence