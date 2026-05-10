# Aquarium dimensions in cm
length = 100
width = 40
height = 30

# Father Fish Method layers:
# 1. Soil layer (tierra de jardín): ~1 inch (2.5 cm)
# 2. Sand cap (arena de lampa): ~2 inches (5 cm)

soil_depth = 2.5
sand_depth = 5.0

# Volume in cm3 (1000 cm3 = 1 liter)
soil_volume_cm3 = length * width * soil_depth
sand_volume_cm3 = length * width * sand_depth

soil_liters = soil_volume_cm3 / 1000
sand_liters = sand_volume_cm3 / 1000

print(f"{soil_liters=}")
print(f"{sand_liters=}")