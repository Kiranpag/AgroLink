from models.crop_model import load_crop_model

def get_crop_health(sensor_data):
    model = load_crop_model()
    # Example preprocessing of sensor_data
    prediction = model.predict(sensor_data)
    return "Healthy" if prediction > 0.5 else "Unhealthy"
