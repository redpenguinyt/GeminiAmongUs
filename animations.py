from gemini import Scene, Sprite

def vote_out(player, is_impostor, impostors_left):
	scene = Scene((35,6), children=[
		Sprite((0,0),"""
			.    。    •   ﾟ  。   .
			.      .     。   。 .
			.   。      ඞ 。 .    •     •
			ﾟ   Blue was not An Impostor.  。 .
			'        2 Impostors remain     。
			ﾟ   .   . ,    .  .
		""")
	])
