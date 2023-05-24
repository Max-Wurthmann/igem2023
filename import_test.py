import opentrons
from opentrons import protocol_api
import time


metadata = {'apiLevel': '2.13'}

def run(protocol: protocol_api.ProtocolContext):
    # use raillights as sign of beeing active
    protocol.set_rail_lights(True)

    file = "/var/lib/jupyter/notebooks/test_input.txt"
    with open(file) as f:
        target = f.read().strip()
    
    # load hardware
    wellplate = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)

    tiprack = protocol.load_labware('opentrons_96_tiprack_20ul', 2)
    
    pipette = protocol.load_instrument('p10_single', mount='left', tip_racks=[tiprack]) # 1 - 10 µL
    
    pipette.pick_up_tip(tiprack[target])
    pipette.home()
    pipette.return_tip()

    time.sleep(3)

    protocol.set_rail_lights(False) # signifies: done with protocol


if __name__ == "__main__":
    # simulate this protocol
    from opentrons import simulate
    with open(__file__) as f:
        logs = simulate.simulate(f, log_level="debug") # for less detail: coose higher level
    
    # save the logs
    cleaned_logs = ["{}: {}".format(log["payload"]["text"], log["payload"]) for log in logs[0]]
    with open("logs/input_logs.txt", "w+") as f:
        f.write("\n".join(cleaned_logs))
        