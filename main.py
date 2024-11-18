import traci

# Define the phases
PHASE_INDICES = {
    0: 'rrrrrGGGgrrrGGGg',  # Phase 0 (Main Street Green)
    1: 'GGGGGrrrrrrrrrrr',  # Phase 1 (Side Street Green)
    2: 'rrrrrrrrrGGGrrrr',  # Phase 2 (Left Turn Green)
    3: 'rrrrrrrrrrrrrrrr',  # All Red
}

# Function to convert green phase to yellow phase
def green_to_yellow(green_phase):
    yellow_phase = ''
    for light in green_phase:
        if light in ['G', 'g']:
            yellow_phase += 'y'
        else:
            yellow_phase += 'r'
    return yellow_phase

def set_phase(traffic_light_id, phase_state, duration):
    traci.trafficlight.setRedYellowGreenState(traffic_light_id, phase_state)
    print(f"Set traffic light to: {phase_state} for {duration} seconds.")
    for _ in range(duration):
        traci.simulationStep()

# Main function
def main():
    sumo_cmd = ["sumo-gui", "-c", "1x1_intersection.sumocfg"]
    traci.start(sumo_cmd)

    traffic_light_id = "J1"  # Replace with your traffic light ID

    try:
        while True:
            # Get user input for green phase
            input_phase = input("Enter a green phase number (0-2): ")

            if not input_phase.isdigit() or int(input_phase) not in PHASE_INDICES:
                print("Invalid input. Please enter a number between 0 and 2.")
                continue

            input_phase = int(input_phase)

            # Get green phase duration
            green_duration = input(f"Enter duration for green phase {input_phase} (seconds, 1-60): ")
            if not green_duration.isdigit() or not (1 <= int(green_duration) <= 60):
                print("Invalid duration. Please enter a number between 1 and 60.")
                continue

            green_duration = int(green_duration)

            # Set green phase
            green_phase = PHASE_INDICES[input_phase]
            set_phase(traffic_light_id, green_phase, green_duration)

            # Set yellow phase
            yellow_phase = green_to_yellow(green_phase)
            yellow_duration = 3
            set_phase(traffic_light_id, yellow_phase, yellow_duration)

            # Set red phase
            red_phase = PHASE_INDICES[3]
            red_duration = 2
            set_phase(traffic_light_id, red_phase, red_duration)

    except KeyboardInterrupt:
        print("\nExiting the simulation.")

    finally:
        traci.close()

if __name__ == "__main__":
    main()
