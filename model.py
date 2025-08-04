import random

# Mocked model – you can replace with real model prediction
def diagnose_fish_disease(image_url):
    diseases = [
        "White Spot Disease",
        "Fin Rot",
        "Columnaris",
        "No visible disease",
        "Dropsy",
        "Anchor Worms",
        "Bacterial Hemorrhagic Septicemia"
    ]
    return random.choice(diseases)