from checkpoint import Checkpoint

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
