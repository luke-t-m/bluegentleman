from logger import log, logtag
from data.bp_format_flat import bp_format_flat



# todo: investigate nonetypes in bp. probably ignore them and let it pass.
def check_valid_bp(bp):
    logtag("bpval")
    log("Checking file matches blueprint format...")
    if "Blueprint" not in bp.keys():
        log("File is not a valid blueprint. Missing Blueprint.")
        return False
    flat = flat_blueprint_format(bp)
    if (a := len(flat)) != (b := len(bp_format_flat)):
        log(f"File is not a valid blueprint. Expected {b} sections, found {a}.")
        return False
    for a, b in zip(flat, bp_format_flat):
        if a != b:
            log(f"File is not a valid blueprint. Mismatch: Expected {b}, found {a}")
            return False
    log(f"File is a valid blueprint.")
    return True

def flat_blueprint_format(bp):
    dic_k = lambda dic: list(dic.keys())
    dic_t = lambda dic: [type(dic[k]) for k in dic.keys()]
    formflat = lambda a: list(zip(dic_k(a), dic_t(a)))
    return formflat(bp) + formflat(bp["Blueprint"])

def dump_blueprint_format(bp):
    print("\n\n\nbp_format_flat = [", end="")
    bp_format_flat = flat_blueprint_format(bp)
    for (e, t) in bp_format_flat:
        if t is type(None):
            print(f'("{e}", type(None)), ', end="")
        else:
            print(f'("{e}", {t.__name__}), ', end = "")
    print("]\n\n\n")

def name_to_uid(blocks: dict, name: str) -> str:
    name_uid_map = {inf["Name"] : uid for uid, inf in blocks.items()} #temp, fix.
    if name in name_uid_map:
        return name_uid_map[name]

def uid_to_lid(bp: dict, uid: str) -> int:
    max_lid = 0
    for lid, uid2 in bp["ItemDictionary"].items():
        lid = int(lid)
        max_lid = max(max_lid, lid)
        if uid == uid2:
            return lid
    return max_lid + 1

def replaced(bp: dict, blockids: list, ouid: str, nuid: str) -> list[int]:
    olid = uid_to_lid(ouid)
    nlid = uid_to_lid(nuid)
    if nlid not in bp["ItemDictionary"]:
        bp["ItemDictionary"][nlid] = nuid
    return [nlid if lid == olid else lid for lid in blockids]
