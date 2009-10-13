from waveapi import events
from waveapi import model
from waveapi import robot
from google.appengine.ext import db

class CompText(db.Model):
	body = db.StringProperty(multiline=True)
  

def OnBlipSubmitted(properties, context):
  """Invoked when a blip has been created"""
  blip = context.GetBlipById(properties['blipId'])
  
  newbliplet = CompText(body = blip.GetDocument().GetText().strip())
  if db.Query(CompText).filter('body = ', newbliplet.body).get() == None:
    newbliplet.put()
  else:
    blip.Delete()

if __name__ == '__main__':
  myRobot = robot.Robot('Robot9k',
      image_url='http://r9kwave.appspot.com/assets/icon.png',
      version='12',
      profile_url='http://r9kwave.appspot.com/')
  myRobot.RegisterHandler(events.BLIP_SUBMITTED, OnBlipSubmitted)
  myRobot.Run()
