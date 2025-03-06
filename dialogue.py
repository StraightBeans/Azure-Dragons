import pygame

class NPC:
  def __init__(self, name):
      self.name = name
      self.dialogue_options = {}

  def add_dialogue(self, trigger, response):
      self.dialogue_options[trigger] = response

  def get_response(self, trigger):
      return self.dialogue_options.get(trigger, "I have nothing to say.")

  #Dialogue Options
  # NPC1
  npc = NPC("Cat")
  npc.add_dialogue("Engage", "Today is the day I vanquish your owner")
  npc.add_dialogue("...", "meow.")
  # NPC2

def interact_with_npc(npc):
  print(f"{npc.name}: ...")
  while True:
      player_input = input("Old Man: ").lower()
      if player_input == "exit":
          print(f"{npc.name}: Meow (That's what I thought)")
          break
      response = npc.get_response(player_input)
      print(f"{npc.name}: {response}")
