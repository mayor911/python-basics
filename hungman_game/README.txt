-> This program simulates the Hugman game.
-> In this two player game, one of the players guesses a word
-> The other player is tasked with finding the letters that make up the word
-> A guess failure results to removal of parts of the hungman
-> If the player wins with no harm to hungman, they are the hungman god.
-> If the player wins but with the hungman devoured, they just win.

-> The devour will be in stages that alter the hungman state
-> State 6 is the best while state 0 is result of drastic failure.

-> This program uses ascii art as its shell based
-> The ascii art is currently stored in hungman_ascii.py
-> The main code is stored in hungman_engine.py
	 
-> In this version, the computer takes the role of the first player
-> The computer randomly chooses a word out of a hardcoded list
-> The hardcoded list is show to the user a.k.a player 2
-> The user might get a clue due to the number of blanks available for filling

	TO PLAY, RUN 
	   $python3 hungman_engine.py
	
	------ ENJOY  PLAYING THE GAME -------------
