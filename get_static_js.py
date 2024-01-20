import json

def getStaticJS():
    with open("config/config.json") as f:
        config = json.load(f)

    print("Config loaded.")

    # Std
    server = config["server"]
    HOST = server["host"]
    PORT = server["port"]
    NO_PROXY = server["noProxy"]
    ACTIVITY_MIN_START_TS = config["userConfig"]["activityMinStartTs"]
    ACTIVITY_MAX_START_TS = config["userConfig"]["activityMaxStartTs"]

    with open("_.js", encoding="utf-8") as f:
        s = f.read()

    s = s.replace(
        "@@@DOCTORATE_HOST@@@", "NO_PROXY" if NO_PROXY else HOST, 1
    ).replace(
        "@@@DOCTORATE_PORT@@@", str(PORT), 1
    ).replace(
        "@@@DOCTORATE_ACTIVITY_MIN_START_TS@@@", str(ACTIVITY_MIN_START_TS), 1
    ).replace(
        "@@@DOCTORATE_ACTIVITY_MAX_START_TS@@@", str(ACTIVITY_MAX_START_TS), 1
    )
    
    print("Script generated.")
    
    return s