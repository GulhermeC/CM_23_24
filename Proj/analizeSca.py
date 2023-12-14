import re
import pandas as pd
import matplotlib.pyplot as plt

def parse_sca_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    results = {
        "packet_transmission": {},
        "packet_reception": {},
        "packet_drops": {},
        # Other categories as needed
    }

    for line in lines:
        if 'scalar' in line or 'statistic' in line:
            parts = line.split()
            key = ' '.join(parts[1:-1])
            value = parts[-1] if parts[-1] != '-nan' else 'Data Not Available'

            # Example categorization logic (to be adjusted based on actual data)
            if 'sentPacket' in key:
                results["packet_transmission"][key] = value
            elif 'receivedPacket' in key:
                results["packet_reception"][key] = value
            elif 'packetDrop' in key:
                results["packet_drops"][key] = value
            # Add more conditions as necessary

    return results

def summarize_results(results):
    # Example summary logic
    print("Simulation Summary Report:\n")
    for category, data in results.items():
        print(f"{category.replace('_', ' ').title()}:")
        for key, value in data.items():
            friendly_key = key.replace('_', ' ').capitalize()
            print(f"  - {friendly_key}: {value}")
        print()    

# Main function to run the analysis
def main():
    sca_file_path = './results/Standalone/0.sca'
    
    results = parse_sca_file(sca_file_path)

    summarize_results(results)
# Running the main function
if __name__ == "__main__":
    main()

