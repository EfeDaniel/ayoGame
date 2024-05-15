
import sys;
import  pygame
sys.path.append('./ai');
sys.path.append('./ui');
sys.path.append('./libs');

import Game

def main():
	pygame.mixer.pre_init(44200, 16, 2, 4096)
	pygame.init()
	pygame.mixer.music.load('ui/assets/bgmusic.wav')
	pygame.mixer.music.set_volume(0.5)
	pygame.mixer.music.play(-1)  # -1 to play the music indefinitely

	game = Game.Game();


if __name__ == '__main__':
	main()