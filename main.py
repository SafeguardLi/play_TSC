import traci

# Define the phases (these values are just examples, replace with your actual phase definitions)
PHASES = {
    0: "Green for North-South, Red for East-West",
    1: "Green for East-West, Red for North-South",
    2: "Yellow for all directions",
    3: "All Red (stop all traffic)"
}

# Mapping phase numbers to traffic light program phase indices
PHASE_INDICES = {
    0: 0,  # Phase 0 index
    1: 1,  # Phase 1 index
    2: 2,  # Phase 2 index
    3: 3   # Phase 3 index
}

# Function to set traffic light phase
def set_phase(traffic_light_id, phase_number):
    if phase_number in PHASE_INDICES:
        phase_index = PHASE_INDICES[phase_number]
        traci.trafficlight.setPhase(traffic_light_id, phase_index)
        print(f"Set traffic light to: {PHASES[phase_number]}")
    else:
        print("Invalid phase number. Please enter a number between 0 and 3.")

# Connect to SUMO
def main():
    # Replace with your SUMO command or configuration file
    sumo_cmd = ["sumo-gui", "-c", "1x1_intersection.sumocfg"]
    traci.start(sumo_cmd)

    traffic_light_id = "79"  # Replace with the ID of your traffic light

    try:
        while True:
            # Get player input
            input_phases = input("Enter 4 numbers (0-3) separated by spaces (e.g., '0 1 2 3'): ").split()

            # Validate input
            if len(input_phases) != 4 or not all(phase.isdigit() and 0 <= int(phase) <= 3 for phase in input_phases):
                print("Invalid input. Please enter 4 numbers between 0 and 3.")
                continue

            # Execute each phase
            for phase in map(int, input_phases):
                set_phase(traffic_light_id, phase)
                duration = int(input(f"Enter duration for phase {phase} (seconds): "))
                traci.simulationStep(duration)

    except KeyboardInterrupt:
        print("\nExiting the simulation.")

    finally:
        traci.close()

if __name__ == "__main__":
    main()
