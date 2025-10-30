pm = float(input("PM2.5: "))

if 0 <= pm <= 12:
    aqi = "Good"
elif 12 < pm <= 35.4:
    aqi = "Moderate"
elif 35.4 < pm <= 55.4:
    aqi = "Unhealthy for Sensitive Groups"
elif 55.4 < pm <= 150.4:
    aqi = "Unhealthy"
elif 150.4 < pm <= 250.4:
    aqi = "Very Unhealthy"
else:
    aqi = "Hazardous"

print("AQI:", aqi)