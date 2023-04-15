import pickle
import pandas

def predictI(data):
    with open('file.pkl',"rb") as f:
        model = pickle.load(f)
        var = model.predict(data)
        return var