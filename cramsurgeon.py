# ---------- Replacement. ----------
ouid = name_to_uid("High Explosive Pellets")
nuid = name_to_uid("Heavy Barrel End (4m)")

blockids = bp["Blueprint"]["BlockIds"]
bp["Blueprint"]["BlockIds"] = replace(blockids, ouid, nuid)

for i, sc in enumerate(bp["Blueprint"]["SCs"]):
    blockids = sc["BlockIds"]
    bp["Blueprint"]["SCs"][i]["BlockIds"] = replace(blockids, ouid, nuid)


blockdata = bp["Blueprint"]["BlockData"]
#print(base64.b64decode(blockdata))