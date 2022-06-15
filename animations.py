from gemini import Scene, AnimatedSprite, Sprite, sleep

player_voted_out = """
.    。    •   ﾟ  。   ..   。
.      .     。   。 .   . ,
.   .    ,    '  .    •     •
ﾟ       '   ,  .   .      。.
'   .    ˘    ,     .  ,   。
ﾟ   .   . ,    .  . 。 .    •
.      .     。   。 .   . ,
.   .    ,    '  .    •     •
"""

def vote_out(user, is_impostor, max_impostors, impostors_left):
	announcement1 = f"{user.name} was {'not' if is_impostor else ''} {'an' if max_impostors > 1 else 'the'} Impostor"
	announcement2 = f"{impostors_left} Impostor{'' if impostors_left == 1 else 's'} remain{'s' if impostors_left == 1 else ''}"

	cutscene = Scene((35,7), clear_char=" ", children=[
		Sprite((0,0), player_voted_out), # Background
		txt1 := AnimatedSprite((3,3), [announcement1[:c] for c in range(len(announcement1)+1)], transparent=False), # Text 1
		txt2 := Sprite((6,4), announcement2, hidden=True)
	])

	player = Sprite((-1,2), "ඞ", colour=user.colour, parent=cutscene)
	for i in range(-4,0):
		for _ in range(2):
			player.move(i,0)
			cutscene.render()
			sleep(.2)
	for i in range(len(announcement1)):
		if i % 2 == 0:
			player.move(-1,0)
		txt1.next_frame()
		cutscene.render()
		sleep(.1)
	txt2.hidden = False
	sleep(1)
	cutscene.render()
	sleep(1)