'''
	Markers:
		'1' represents X
		'-1' represents O
	
	Flags:
		for CURRENT_PLAYER: '1' represents Player 1 and '-1' represents Player 2
'''

import os
from random import randint
import numpy as np

CURRENT_PLAYER=0

def clear_screen():
	os.system('clear')
	print 'Welcome to Tic Tac Toe'
	print '\nThe Board Positions corrospond to Numeric Keypad\n\n'

def get_Input(board,player_marker):
	'''
		gets Input from the user
	'''
	global CURRENT_PLAYER
	if CURRENT_PLAYER==1:
		while True:
			x=int(raw_input("Player A: Enter Move: "))
			print x
			if x>=1 and x<=9 and board[x-1]==0:
				board[x-1]=player_marker['A']
				break
			else:
				print 'Invalid Position.'
				continue
	elif CURRENT_PLAYER==-1:
		while True:
			x=int(raw_input("Player B: Enter Move: "))
			print x
			if x>=1 and x<=9 and board[x-1]==0:
				board[x-1]=player_marker['B']
				break
			else:
				print 'Invalid move'
				continue
	else:
		pass
	return board

def choose_Player():
	'''
		Randomly chooses which Player goes First
	'''
	global CURRENT_PLAYER
	player_number=randint(0,1)
	if player_number==0:
		CURRENT_PLAYER+=1
		return 'A'
	else:
		CURRENT_PLAYER+=-1
		return 'B'

def getPlayerMarker():
	'''
		Keeps Track of Markers associated with the Players
	'''
	player=choose_Player()
	while True:
		player__Marker=raw_input("Player %s, Choose a Marker: 'X' , 'O': " %player)
		if player__Marker=='X' or player__Marker=='O':
			break
		else:
			print 'Invalid Marker. Choose again'
			continue
	if player=='A':
		if player__Marker=='X':
			marker_list={'A':1, 'B':-1}
		else:
			marker_list={'A':-1, 'B':1}
	else:
		if player__Marker=='X':
			marker_list={'A':-1, 'B':1}
		else:
			marker_list={'A':1, 'B':-1}
	return marker_list

def win_Check(board,playerMarker,win_flag):
	'''
		Check for winning Player
		Returns: "1" if Player "A" wins or "-1" if Player "B" wins else "0" for No Win
	'''
	if board[0]==board[1]==board[2]==1 or board[0]==board[1]==board[2]==-1:
		if (playerMarker['A']==1 and board[0]==1) or (playerMarker['A']==-1 and board[0]==-1):
				win_flag=1
		else: 
			win_flag=-1
	elif board[3]==board[4]==board[5]==1 or board[3]==board[4]==board[5]==-1:
		if (playerMarker['A']==1 and board[3]==1) or (playerMarker['A']==-1 and board[3]==-1):
				win_flag=1
		else: 
			win_flag=-1
	elif board[6]==board[7]==board[8]==1 or board[6]==board[7]==board[8]==-1:
		if (playerMarker['A']==1 and board[6]==1) or (playerMarker['A']==-1 and board[6]==-1):
				win_flag=1
		else: 
			win_flag=-1
	elif board[0]==board[3]==board[6]==1 or board[0]==board[3]==board[6]==-1:
		if (playerMarker['A']==1 and board[0]==1) or (playerMarker['A']==-1 and board[0]==-1):
				win_flag=1
		else: 
			win_flag=-1
	elif board[1]==board[4]==board[7]==1 or board[1]==board[4]==board[7]==-1:
		if (playerMarker['A']==1 and board[1]==1) or (playerMarker['A']==-1 and board[1]==-1):
				win_flag=1
		else: 
			win_flag=-1
	elif board[2]==board[5]==board[8]==1 or board[2]==board[5]==board[8]==-1:
		if (playerMarker['A']==1 and board[2]==1) or (playerMarker['A']==-1 and board[2]==-1):
				win_flag=1
		else: 
			win_flag=-1
	elif board[0]==board[4]==board[8]==1 or board[0]==board[4]==board[8]==-1:
		if (playerMarker['A']==1 and board[0]==1) or (playerMarker['A']==-1 and board[0]==-1):
				win_flag=1
		else: 
			win_flag=-1
	elif board[2]==board[4]==board[6]==1 or board[2]==board[4]==board[6]==-1:
		if (playerMarker['A']==1 and board[2]==1) or (playerMarker['A']==-1 and board[2]==-1):
				win_flag=1
		else: 
			win_flag=-1
	else:
		win_flag=0
	return win_flag

def checkBoard(board,flags,playerMarker):
	'''
		Checks for Status of the game
	'''
	flags['Winner']=win_Check(board,playerMarker,flags['Winner'])
	if board.count(0)==0:
		flags['FullBoard']=1
		if flags['Winner']==0:
			flags['Tie']=1
	else:	
		if flags['Winner']!=0:
			flags['Ongoing']=0
	return flags

def normalize_board(board):
	'''
		This Function makes board corrospond to Numpad
	'''
	x=[]
	for i in xrange(0,9,3):
		x.append(board[i:i+3])
	x2=[]
	for i in xrange(2,-1,-1):
		for j in xrange(3):
			x2.append(x[i][j])     
	return x2

def printBoard(board):
	pos=0
	boardpos=normalize_board(board)
	for i in xrange(13):
		for j in xrange(13):
			if i%4==0:
				if j%4==0:
					print '+',
				else:
					print '-',
			elif i%2==0 and i%4!=0:
				if j%2==0 and j%4!=0:
					markerValue=boardpos[pos]
					if markerValue==1:
						print 'X',
					elif markerValue==-1:
						print 'O',
					else:
						print ' ',
					pos+=1
				elif j%4==0:
					print '|',
				else:
					print ' ',
			else:
				if j%4==0:
					print '|',
				else:
					print ' ',
		print ''


while True:
	clear_screen()
	board=[0]*9
	Flags={'Ongoing':1,'Tie':0,'Winner':0,'FullBoard':0}
	player_Marker=getPlayerMarker()
	printBoard(board)
	while Flags['Ongoing']==1 and Flags['FullBoard']==0:
		board=get_Input(board,player_Marker)
		clear_screen()
		printBoard(board)
		Flags=checkBoard(board,Flags,player_Marker)
		if Flags['Tie']:
			print 'Board Full!! The Game is Tied'
			break
		elif Flags['Winner']==1:
			print 'Player A Wins!!'
			break
		elif Flags['Winner']==-1:
			print 'Player B Wins!!'
			break
		CURRENT_PLAYER=np.negative(CURRENT_PLAYER)
	
	next_Play=raw_input("Do you want to Play again? Yes/No ")
	if next_Play.lower()=='yes' or next_Play=='y':
		CURRENT_PLAYER=0
		continue
	else:
		break 

