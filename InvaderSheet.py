from SpriteSheet import SpriteSheet

ALPHA_KEY = (0,0,0)

class Sprites():
	INVADER_1 = (16, 0, 128, 128)
	INVADER_2 = (160, 0, 128, 128)
	INVADER_3 = (288, 0, 128, 128)
	INVADER_4 = (432, 0, 128, 128)
	INVADER_5 = (16, 128, 128, 96)
	INVADER_6 = (160, 128, 128, 96)
	INVADER_7 = (288, 128, 128, 96)
	INVADER_8 = (416, 128, 128, 96)
	INVADER_9 = (16, 232, 72, 128)
	INVADER_10 = (112, 232, 72, 128)
	INVADER_11 = (200, 232, 96, 128)
	INVADER_12 = (304, 232, 96, 128)
	INVADER_13 = (16, 352, 128, 128)
	INVADER_14 = (140, 352, 128, 128)
	INVADER_15 = (264, 352, 96, 128)
	INVADER_16 = (372, 352, 96, 128)
	PLAYER = (144, 632, 96, 64)
	COLLISION_PARTICLE = (352, 600, 96, 128)


class InvaderSheet:
	def __init__(self):
		self.sheet = SpriteSheet('res/space_invaders.png')

	def get_image(self, rect):
		return self.sheet.image_at(rect, colorkey=ALPHA_KEY)