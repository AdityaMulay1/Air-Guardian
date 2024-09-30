import time
import random

class AirQualityMonitor:
    def __init__(self, data_file):
        self.data_file = data_file

    def collect_data(self):
        """Simulate air quality data collection."""
        while True:
            data = {
                "pm25": round(random.uniform(5, 150), 2),  # PM2.5 value
                "pm10": round(random.uniform(10, 200), 2), # PM10 value
                "co2": round(random.uniform(300, 1000), 2), # CO2 in ppm
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }

            with open(self.data_file, 'a') as file:
                file.write(f"{data}\n")

            print(f"Data collected: {data}")
            time.sleep(10)  # collect data every 10 seconds

if __name__ == "__main__":
    monitor = AirQualityMonitor(data_file='air_quality_data.txt')
    monitor.collect_data()
