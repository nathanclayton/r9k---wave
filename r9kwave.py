# Copyright (C) 2009 Nathan Clayton
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
