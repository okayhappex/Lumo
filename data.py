import discord

import dotenv
dotenv.load_dotenv()

import os
from deta import Deta

deta = Deta(os.getenv("API_KEY"))
guildBase = deta.Base("guilds")
userBase = deta.Base('users')
objectBase = deta.Base('objects')

def init():
    global config
    global users
    global objects

    guildCount = guildBase.fetch().count
    guildList = guildBase.fetch().items
    config = {}

    for item in range(guildCount):
        guild = guildList[item]
        guildCfg = guild["config"]
        key = guild["key"]

        config[key] = guildCfg

    userCount = userBase.fetch().count
    userList = userBase.fetch().items
    users = {}

    for item in range(userCount):
        user = userList[item]
        key = user["key"]

        users[key] = user

    objCount = objectBase.fetch().count
    objList = objectBase.fetch().items
    objects = {}

    for item in range(objCount):
        obj = objList[item]
        key = obj["key"]

        objects[key] = obj

init()
class User:
    def __init__(self, id: int, name: str | None = None,  money: int | None = None, premium: bool | None = None, blocked: bool | None = None):
        if money is None or premium is None or premium is None or blocked is None:
            if userBase.get(str(id)) is None:
                self.id = id
                if name is None: self.name = "Unknown User"
                else: self.name = name
                self.money = 0
                self.premium = False
                self.blocked = False
            else:
                current_user = userBase.get(str(id))
                self.id = id
                self.name = current_user["_name"]
                self.money = int(current_user["money"])
                self.premium = bool(current_user["premium"])
                if "blocked" in current_user: self.blocked = current_user["blocked"]
                else: self.blocked = False
        else:
            self.id = id
            self.name = name
            self.money = money
            self.premium = premium
            self.blocked = blocked
    
    def save(self):
        if userBase.get(str(self.id)) is None:
            userBase.put({ "_name": str(self.name), "money": str(self.money), "premium": self.premium, "blocked": self.blocked }, str(self.id))
        else:
            userBase.update({ "_name": str(self.name), "money": str(self.money), "premium": self.premium, "blocked": self.blocked }, str(self.id))
    
    def delete(self):
        if userBase.get(str(self.id)) is not None:
            userBase.delete(str(self.id))
        else:
            pass

class Item:
    def __init__(self, id: int, name: str | None = None, value: int | None = None, owner: int | None = None, amount: int | None = None):
        if name is None or value is None or owner is None or amount is None:
            if objectBase.get(str(id)) is None:
                self.id = id
                if name is None: self.name = "Unknown Object"
                else: self.name = name
                self.value = 0
                self.forsale = True
                self.owner = 0
                self.amount = amount

            else:
                obj = objectBase.get(str(id))
                self.id = id
                self.name = obj["_name"]
                self.value = int(obj["value"])
                self.owner = int(obj(["owner"]))
                self.forsale = bool(obj["forsale"])
                self.amount = int(obj["amount"])
        else:
            if id is None: pass
            self.id = id
            self.name = name
            self.value = value
            self.owner = owner
            self.forsale = False
            self.amount = amount
    
    def save(self):
        if objectBase.get(str(self.id)) is None:
            objectBase.put({ "_name": str(self.name), "owner": str(self.owner), "value": str(self.value), "for_sale": self.forsale, "amount": str(self.amount) }, str(self.id))
        else:
            objectBase.update({ "_name": str(self.name), "owner": str(self.owner), "value": str(self.value), "for_sale": self.forsale, "amount": str(self.amount) }, str(self.id))
    
    def sell(self, price):
        self.forsale = True
        self.value = price

        self.save()
    
    def cancel_sale(self):
        self.forsale = False

        self.save()
    
    def destroy(self):
        if objectBase.get(str(self.id)) is not None:
            objectBase.delete(str(self.id))
        else:
            pass

def searchItem(owner: int | None = None, name: str | None = None, maxValue: int | None = None, minValue: int | None = None, forsale: bool | None = None):
    print(name, owner, maxValue, minValue, forsale)

    if type(owner) != type(0): owner = 0
    if type(name) != type(""): name = ""
    if type(maxValue) != type(0): maxValue = -1
    if type(minValue) != type(0): minValue = -1
    if True != forsale != False: forsale = None

    if owner == name == maxValue == minValue == forsale is None:
        return objectBase.fetch().items
    else:
        res = []
        for item in range(objectBase.fetch().count):
            obj = objectBase.fetch().items[item]

            if (int(obj["value"]) <= maxValue or maxValue == -1) and (int(obj["value"]) >= minValue or minValue == -1) and (name == "" or name in obj["_name"]) and (owner == 0 or obj["owner"] == str(owner)) and (forsale is None or obj["for_sale"] is forsale):
                res.append(obj)
        return res