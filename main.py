#Made by Oren Lindsey, ©2021

from flask import Flask, render_template
from replit import db
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

#API
items = {
  "xbox-controller": False,
  "nike-blazer": False,
  "denim-jacket": False,
  "laptop-cooling-pad": False,
  "mob-grip": False,
  "icons-book": False,
  "soled-out": False,
  "off-whitebelt": False,
  "Cybertruck-cap": False,
  "battery-day-shirt": False,
  "cybertruck-shirt": False,
  "plaid-shirt": False,
  "decanter": False,
  "vsauce-box": False,
  "jordan-hat": False,
  "crep-kit": False,
  "crep-travel": False,
  "r8-kit": False,
  "EL-kit": False,
  "air-max": False,
  "air-j": False,
  "airpods": False,
  "airpods-pro": False,
  "ipad": False,
  "ipad-mini": False,
  "grid-art": False,
  "homepod-mini": False,
  "smart-bulb": False,
  "skate-bearings": False,
  "supreme-grip": False,
  "supreme-wheels": False,
  "supreme-trucks": False,
  "supreme-deck": False,
  "crocs": False,
  "ultimate-sneaker-bk": False,
  "roadster-dc": False,
  "rr-pen": False,
  "clip-3": False,
  "clip-4": False,
  "af-1": False,
  "watch-modern": False,
  "watch-milanese": False,
  "watch-nike-loop": False,
  "watch-nike-band": False,
  "replit-sub": False,
  "shoedog-bk": False,
  "liftoff-book": False,
  "watch-band": False,
  "beats-buds": False,
  "watch-charger": False,
}
print(items)

db["xbox-controller"] = False
db["nike-blazer"] = False
db["denim-jacket"] = False
db["laptop-cooling-pad"] = False
db["mob-grip"] = False
db["icons-book"] = False
db["soled-out"] = False
db["off-whitebelt"] = False
db["Cybertruck-cap"] = False
db["battery-day-shirt"] = False
db["plaid-shirt"] = False
db["decanter"] = False
db["vsauce-box"] = False
db["jordan-hat"] = False
db["crep-kit"] = False
db["r8-kit"] = False
db["EL-kit"] = False
db["air-max"] = False
db["air-j"] = False
db["airpods"] = False
db["airpods-pro"] = False
db["ipad"] = False
db["ipad-mini"] = False
db["grid-art"] = False
db["homepod-mini"] = False
db["smart-bulb"] = False
db["skate-bearings"] = False
db["supreme-grip"] = False
db["supreme-wheels"] = False
db["supreme-trucks"] = False
db["supreme-deck"] = False
db["crocs"] = False
db["ultimate-sneaker-bk"] = False
db["roadster-dc"] = False
db["rr-pen"] = False
db["clip-3"] = False
db["clip-4"] = False
db["af-1"] = False
db["watch-modern"] = False
db["watch-milanese"] = False
db["watch-nike-loop"] = False
db["watch-nike-band"] = False
db["replit-sub"] = False
db["shoedog-bk"] = False
db["beats-buds"] = False
db["watch-charger"] = False
print(db.all())

@app.route('/api/get-status/')
def returnAllItems():
    itemsJson = json.dumps(items)
    response = itemsJson
    return response

@app.route('/api/toggle-item/<string:itemToSwitch>', methods=['GET','POST'])
def toggleItem(itemToSwitch):
      if itemToSwitch in items:
        if items[itemToSwitch] == True:
          items[itemToSwitch]  =  False
          response = "Toggled to false"
          return response
        elif items[itemToSwitch] == False:
          items[itemToSwitch]  =  True
          response = "Toggled to true"
          return "Toggled to true"
        else:
          return "Error - It seems that the item was neither true nor false. It should be one or the other"
      else:
        return "That item doesn't exist"

@app.route('/sizes')
def sizes():
    return render_template("sizes.html")

@app.route('/list')
def list():
    return render_template("list.html")

@app.route('/sitemap')
def sitemap():
    return render_template("siteMap.html")

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('pageNotFound.html'), 404

print("Starting up")
app.run(host='0.0.0.0', port=8080)
