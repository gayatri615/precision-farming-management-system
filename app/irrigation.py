
def get_irrigation_recommendation(soil_moisture: float):
    # These thresholds provide a simple first version of the
    # irrigation decision logic. They can be replaced later
    # with crop-specific or ML-based recommendations.

    if soil_moisture < 30:
        return {
            "soil_moisture": soil_moisture,
            "irrigation_required": True,
            "recommendation": "Irrigation required"
        }

    if soil_moisture <= 60:
        return {
            "soil_moisture": soil_moisture,
            "irrigation_required": False,
            "recommendation": "Monitor soil moisture"
        }

    return {
        "soil_moisture": soil_moisture,
        "irrigation_required": False,
        "recommendation": "No irrigation required"
    }
