# pylint: disable=unspecified-encoding
from opentrons import protocol_api

metadata = {'apiLevel': '2.13'}

def run(protocol: protocol_api.ProtocolContext):
    # use raillights as sign of beeing active
    protocol.set_rail_lights(True)

    # load hardware
    # ToDo: we need to update the hardware specs
    wellplate = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)

    tiprack20 = protocol.load_labware('opentrons_96_tiprack_20ul', 2)
    tiprack300 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)

    pipette_p10 = protocol.load_instrument('p10_single', mount='left', tip_racks=[tiprack20]) # 1 - 10 µL
    pipette_p300 = protocol.load_instrument('p300_single', mount='right', tip_racks=[tiprack300]) # 30 - 300 µL


    # start protocol
    # picks up and droppes tips more or less automatically, alter default behaivior via kwargs
    # these two commands require 430 microLiter in A1
    pipette_p10.transfer(10,
                         wellplate['A1'],
                         wellplate["B1"],
                         trash=False)  # puts tip back where it got it, default: throw it in the trash at deck slot 12

    pipette_p300.distribute(30,
                            wellplate["A1"],
                            [well for well in wellplate.rows_by_name()["A"]
                             if well != "A1"],
                            trash=False)

    protocol.set_rail_lights(False) # signifies: done with protocol


if __name__ == "__main__":
    # simulate this protocol
    from opentrons import simulate
    with open(__file__) as f:
        logs = simulate.simulate(f, log_level="debug") # for less detail: coose higher level
    
    # save the logs
    cleaned_logs = ["{}: {}".format(log["payload"]["text"], log["payload"]) for log in logs[0]]
    with open("logs.txt", "w+") as f:
        f.write("\n".join(cleaned_logs))
        