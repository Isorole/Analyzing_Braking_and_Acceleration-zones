import fastf1
import matplotlib.pyplot as plt

# Enable cache for faster data loading
fastf1.Cache.enable_cache("E:\\Python codes\\cache")  # Set cache directory

# Load F1 session (Example: 2023 Belgian GP, Qualifying)
session = fastf1.get_session(2023, "Belgian Grand Prix", "Q")
session.load()

# Select a driver (Example: Max Verstappen)
lap = session.laps.pick_driver("HAM").pick_fastest()  # Get fastest lap data

# Extract telemetry (speed, throttle, brake, and position data)
telemetry = lap.get_car_data().merge(lap.get_pos_data(), left_index=True, right_index=True)

# Create figure
plt.figure(figsize=(10, 6))

# Scatter plot with color mapping for braking & acceleration
sc = plt.scatter(telemetry["X"], telemetry["Y"], c=telemetry["Brake"], cmap="coolwarm", edgecolors='none')

# Add colorbar
plt.colorbar(sc, label="Brake Pressure")

# Customize plot
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.title("Braking & Acceleration Zones - Belgian GP 2023 (HAM)")
plt.grid(True)

# Show the plot
plt.show()
