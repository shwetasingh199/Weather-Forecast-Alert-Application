def generate_alerts(temp, humidity, rain):

    alerts = []

    if temp > 40:
        alerts.append("🔥 High Temperature Alert")

    if humidity > 85:
        alerts.append("💧 High Humidity Alert")

    if rain:
        alerts.append("🌧 Rain Alert")

    return alerts