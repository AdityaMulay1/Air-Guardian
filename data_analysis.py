import json

class DataAnalysis:
    def __init__(self, data_file):
        self.data_file = data_file

    def read_data(self):
        """Read data from the file."""
        with open(self.data_file, 'r') as file:
            return [json.loads(line.replace("'", "\"")) for line in file.readlines()]

    def analyze_data(self):
        """Analyze air quality data and provide insights."""
        data = self.read_data()
        high_pm25_count = sum(1 for d in data if d['pm25'] > 100)
        high_co2_count = sum(1 for d in data if d['co2'] > 800)

        print(f"Instances with PM2.5 above 100: {high_pm25_count}")
        print(f"Instances with CO2 above 800 ppm: {high_co2_count}")

        if high_pm25_count > 5:
            print("Warning: Poor air quality detected frequently. Consider improving ventilation.")
        if high_co2_count > 3:
            print("Warning: CO2 levels are high. Ensure good ventilation.")

if __name__ == "__main__":
    analyzer = DataAnalysis(data_file='air_quality_data.txt')
    analyzer.analyze_data()
