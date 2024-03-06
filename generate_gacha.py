from server.constants import CHARACTER_TABLE_URL, CONFIG_JSON_PATH, GACHA_TEMPLATE_JSON_PATH
from server.core.function.update import updateData
from server.utils import read_json, write_json

CHARACTER_TABLE = updateData(CHARACTER_TABLE_URL)
CONFIG = read_json(CONFIG_JSON_PATH)
DATA = read_json(GACHA_TEMPLATE_JSON_PATH)

CHARACTER_KEYS = list(CHARACTER_TABLE.keys())

# GENERATE BANNER STUFFS HERE
for char_key in CHARACTER_KEYS:
    if "char" not in char_key:
        continue

    match CHARACTER_TABLE[char_key]["rarity"]:
        case "TIER_6":
            print(f"{char_key}: Added to 6-star group.")
            DATA["detailInfo"]["availCharInfo"]["perAvailList"][0]["charIdList"].append(char_key)
        case "TIER_5":
            print(f"{char_key}: Added to 5-star group.")
            DATA["detailInfo"]["availCharInfo"]["perAvailList"][1]["charIdList"].append(char_key)
        case "TIER_4":
            print(f"{char_key}: Added to 4-star group.")
            DATA["detailInfo"]["availCharInfo"]["perAvailList"][2]["charIdList"].append(char_key)
        case "TIER_3":
            print(f"{char_key}: Added to 3-star group.")
            DATA["detailInfo"]["availCharInfo"]["perAvailList"][3]["charIdList"].append(char_key)
        case _:
            print(f"{char_key}: Skipped.")

DATA["detailInfo"]["availCharInfo"]["perAvailList"][0]["totalPercent"] = CONFIG["gacha"]["5rarity"]
DATA["detailInfo"]["availCharInfo"]["perAvailList"][1]["totalPercent"] = CONFIG["gacha"]["4rarity"]
DATA["detailInfo"]["availCharInfo"]["perAvailList"][2]["totalPercent"] = CONFIG["gacha"]["3rarity"]
DATA["detailInfo"]["availCharInfo"]["perAvailList"][3]["totalPercent"] = CONFIG["gacha"]["2rarity"]

# GENERATE GACHA OBJECTS HERE
gachaObjList = [
    {"gachaObject": "TEXT", "param": "ODPY BANNER", "type": 0},
    {"gachaObject": "ATTAIN_CHAR", "param": "", "type": 0},
    {"gachaObject": "TEXT", "param": "", "type": 1},
    {"gachaObject": "AVAIL_CHAR", "param": None, "type": 0},
    {"gachaObject": "TEXT", "param": "", "type": 7},
    {"gachaObject": "TEXT", "param": "ODPY BANNER", "type": 5},
]

DATA["detailInfo"]["gachaObjList"].append(gachaObjList)

FILENAME = CONFIG["version"]["android"]["resVersion"] + ".json"
SAVE_LOCATION = "data/gacha/" + FILENAME

write_json(DATA, SAVE_LOCATION)
