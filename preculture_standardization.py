import pandas as pd
import numpy as np

rows = [chr(x) for x in range(ord("A"), ord("H")+1)] #letters from A to H
cols = list(range(12))

preculture_ODs = pd.read_excel("EmpyPlateTest.xls", index_col=0, names=cols).loc[rows, cols].astype("float")

def get_transfer_volume(preculture_OD, target_OD = 0.05, target_volume=150):
    """for a given preculture OD this returns the transfer volume in microL to obtain an OD of {@param target_OD} with a given {@param target_volume}"""
    transfer_volume = target_volume * target_OD / preculture_OD # volumen * wollen / haben
    return transfer_volume

preculture_transfer_volumes = preculture_ODs.applymap(get_transfer_volume)
media_tranfer_volumes = 150 - preculture_transfer_volumes
media_tranfer_volumes = media_tranfer_volumes.where(media_tranfer_volumes > 0, other=0)


print(preculture_ODs)
print(preculture_transfer_volumes)
print(media_tranfer_volumes)


