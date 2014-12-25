import re

class Checkpoint:
  checkpoints = []

  def __init__(self, text, rooms, end):
    self.text   = text
    self.rooms  = rooms
    self.end    = end
    Checkpoint.checkpoints.append(self)

  def prompt_options(self):
    return raw_input(self.text)

  def should_end(self, response):
    if(re.match(r'QUIT', response) or self.end):
      return True
    else:
      return False

  def progress(self, target):
    if target in self.rooms and Checkpoint.checkpoints[target]:
      return Checkpoint.checkpoints[target]
    else:
      return False
