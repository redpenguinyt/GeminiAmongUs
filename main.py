from gemini import Scene, Sprite, Camera, txtcolours as tc
import animations

game_map = "map.txt not found"

scene = Scene((100,100), children=[Sprite((0,0), game_map)])
player1 = Sprite((10,10), "", colour=tc.RED)
player_camera = Camera((0,0), (20,10), focus_object=player1)

animations.vote_out(player1, True, 1)