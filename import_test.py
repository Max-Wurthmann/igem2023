from opentrons import protocol_api
import time

metadata = {'apiLevel': '2.13'}

def run(protocol: protocol_api.ProtocolContext):
    # use raillights as sign of beeing active
    protocol.set_rail_lights(True)

    with open("test_input.txt") as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    source, target = lines

    # load hardware
    wellplate = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)

    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', 4)

    pipette = protocol.load_instrument('p300_single', mount='right', tip_racks=[tiprack]) # 30 - 300 µL

    volume = 150 #transfer <volume> ul to the well and back

    pipette.pick_up_tip()

    pipette.aspirate(volume, wellplate[source])
    pipette.dispense(volume, wellplate[target])

    time.sleep(3)

    pipette.aspirate(volume, wellplate[target])
    pipette.dispense(volume, wellplate[source])

    pipette.return_tip()

    protocol.set_rail_lights(False) # signifies: done with protocol


if __name__ == "__main__":
    # simulate this protocol
    from opentrons import simulate
    with open(__file__) as f:
        logs = simulate.simulate(f, log_level="debug") # for less detail: coose higher level
    
    # save the logs
    cleaned_logs = ["{}: {}".format(log["payload"]["text"], log["payload"]) for log in logs[0]]
    with open("input_logs.txt", "w+") as f:
        f.write("\n".join(cleaned_logs))
        