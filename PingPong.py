#A game of table tennis almost always sounds like Ping! followed by Pong! Therefore, you know that Player 2 has won if you hear Pong! as the last sound (since Player 1 didn't return the ball back).

#Given a list of Ping!, create a function that inserts Pong! in between each element. Also:

#If win equals True, end the list with Pong!.
#If win equals False, end with Ping! instead.
#Examples
#ping_pong(["Ping!"], True) ➞ ["Ping!", "Pong!"]

#ping_pong(["Ping!", "Ping!"], False) ➞ ["Ping!", "Pong!", "Ping!"]

#ping_pong(["Ping!", "Ping!", "Ping!"], True) ➞ ["Ping!", "Pong!", "Ping!", "Pong!", "Ping!", "Pong!"]
#Notes
#You will always return the ball (i.e. the Pongs are yours).
#Player 1 serves the ball and makes Ping!.
#Return a list of strings.

def ping_pong(lst, win):
	
	for i in range(1,len(lst)*2,2):
		lst.insert(i, "Pong!")
	
	if win == False:
		lst.pop(len(lst)-1)
	
	return lst
