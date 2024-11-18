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


# import traci

# # Define the phases (these values are just examples, replace with your actual phase definitions)
# PHASES = {
#     0: "Green for main street",
#     1: "Green for South bound",
#     2: "Yellow for North bound",
# }

# # <tlLogic id="J1" type="static" programID="1" offset="0">
#     #     <phase duration="33" state="rrrrrGGGgrrrGGGg"/>
#     #     <phase duration="3"  state="rrrrryyyyrrryyyy"/>
#     #     <phase duration="3"  state="rrrrrrrrrrrrrrrr"/>
#     #     <phase duration="33" state="GGGGGrrrrrrrrrrr"/>
#     #     <phase duration="3"  state="yyyyyrrrryyyrrrr"/>
#     #     <phase duration="6"  state="rrrrrrrrrGGGrrrr"/>
#     #     <phase duration="3"  state="rrrrrrrrryyyrrrr"/>
#     # </tlLogic>

# # Mapping phase numbers to traffic light program phase indices
# def green_to_yellow(green_phase):
#     yellow_phase = ''
#     for _ in green_phase:
#         if _ in ['G','g']:
#             yellow_phase += 'y'
#         else:
#             yellow_phase += 'r'
#     print("yellow phase from",green_phase,"is",yellow_phase) ##
#     return yellow_phase

# # Function to set traffic light phase
# def set_phase(traffic_light_id, phase_number):
#     if phase_number in PHASE_INDICES:
#         phase_index = PHASE_INDICES[phase_number]
#         traci.trafficlight.setPhase(traffic_light_id, phase_index)
#         print(f"Set traffic light to: {PHASES[phase_number]}")
#     else:
#         print("Invalid phase number. Please enter a number between 0 and 3.")

# # Connect to SUMO
# def main():
    
#     PHASE_INDICES = {
#     0: 'rrrrrGGGgrrrGGGg',  # Phase 0 index
#     1: 'GGGGGrrrrrrrrrrr',  # Phase 1 index
#     2: 'rrrrrrrrrGGGrrrr',  # Phase 2 index
#     3: 'rrrrrrrrrrrrrrrr',  # all red
#     }
    
#     # Replace with your SUMO command or configuration file
#     sumo_cmd = ["sumo-gui", "-c", "1x1_intersection.sumocfg"]
#     traci.start(sumo_cmd)

#     traffic_light_id = "J1"  # Replace with the ID of your traffic light

#     try:
#         while True:
#             # Get player input
#             input_phase = int(input("Enter a green phase number (0-2): "))

#             # Validate input
#             if not (0 <= int(input_phase) <= 2):
#                 print("Invalid input. Please enter a number between 0 and 2.")
#                 input_phase = input("Enter a green phase number (0-2): ")
#                 continue

#             print("input value",input_phase)

#             phase_idx = PHASE_INDICES[input_phase]
#             print("green phase:", phase_idx)

#             green_duration = int(input(f"Enter duration for green phase {input_phase} (seconds, 0 - 60 s): "))
            
#             if (int(green_duration) <= 0 and int(green_duration) >= 60):
#                 print("Invalid duration. Please enter a positive integer. Please not set a phase longer than 60 seconds")
#                 green_duration = input(f"Enter duration for green phase {input_phase} (seconds): ")
#                 continue

#             # Execute each phase
#             #for phase in map(int, input_phases):
#             traci.trafficlight.setRedYellowGreenState(traffic_light_id, phase_idx)
#             traci.simulationStep(green_duration)

#             # Insert yellow phase
#             yellow_duration = 3  # Set yellow phase duration (can be modified)
#             traci.trafficlight.setRedYellowGreenState(traffic_light_id, green_to_yellow(phase_idx))
#             traci.simulationStep(yellow_duration)


#             # Insert red phase
#             red_duration = 2  # Set red phase duration (can be modified)
#             traci.trafficlight.setRedYellowGreenState(traffic_light_id, PHASE_INDICES[3])
#             traci.simulationStep(yellow_duration)

#     except KeyboardInterrupt:
#         print("\nExiting the simulation.")

#     finally:
#         traci.close()

# if __name__ == "__main__":
#     main()
