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


# Initialize all checkpoints
a = Checkpoint('You encounter a fork. Go right (1) or left(2) ?', [1,2], False)
b = Checkpoint('You have found the treasure. Go back? (0)', [0], False)
c = Checkpoint('You have fallen into a pit.', [0], True)


# Setup the game
end = False
current = a

while not end:
  response = current.prompt_options()
  end = current.should_end(response)
  current = current.progress(int(response))
