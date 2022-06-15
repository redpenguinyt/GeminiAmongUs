from gemini import Scene, Sprite, Camera, txtcolours as tc
import animations

game_map = "map.txt not found"

class Player(Sprite):
	def __init__(self, pos, name: str, colour: str, *args, **kwargs):
		self.name = name
		super().__init__(pos, "ඞ", colour=colour, *args, **kwargs)

scene = Scene((100,100), children=[Sprite((0,0), game_map)])
player1 = Player((10,10), "Red", tc.RED)
player_camera = Camera((0,0), (20,10), focus_object=player1)



animations.vote_out(player1, True, 2, 2)