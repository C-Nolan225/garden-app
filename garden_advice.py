def get_season_advice(season):
    """Return gardening advice for the selected season."""
    if season == "summer":
        return "Water your plants regularly and provide some shade."
    if season == "winter":
        return "Protect your plants from frost with covers."

    return "No advice for this season."


def get_plant_advice(plant_type):
    """Return gardening advice for the selected plant type."""
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    if plant_type == "vegetable":
        return "Keep an eye out for pests!"

    return "No advice for this type of plant."


def generate_advice(season, plant_type):
    """Combine season and plant type advice into one message."""
    return f"{get_season_advice(season)}\n{get_plant_advice(plant_type)}"


season = input("Enter the season: ").strip().lower()
plant_type = input("Enter the plant type: ").strip().lower()

print(generate_advice(season, plant_type))

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
