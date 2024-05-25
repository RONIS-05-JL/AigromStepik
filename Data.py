import json
from aiogram.types import Message, ContentType


def databaser(message: Message = "", id='', id_data="", returner: bool = False) -> object:
    with open('database.json', 'r') as dates:
        rt = json.load(dates)
        if id:
            rt[id] = id_data
        else:
            id = str(message.from_user.id)
            if id not in rt:
                rt[id] = rt.setdefault(id, {"message": [],
                                            "games": {'tries': 7, 'all games': 0, "in_game": False, "wins": 0,
                                                      "loses": 0}})
            rt[str(id)]["message"].append(message.text)
    if returner:
        return id, rt[id]
    with open('database.json', 'w') as dates:
        json.dump(rt, dates, indent=4)

