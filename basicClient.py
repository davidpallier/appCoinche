
#Wait for server request
if request is 'Status':
 status = waitForUserToUpdateStatus()
 sendToServer(request, status)
 
elif request is 'Play a card':
 card = waitForUserToPlayCard()
 sendToServer(request, card)
 #wait for server answer
 while answer is not valid:
  cardNotValid()
  card = waitForUserToPlayCard()
  sendToServer(request, card)
  #wait for server answer

elif request is 'Make a Bid'
 bidValue = waitForUserToBid()
 sendToServer(request, bidValue)
 #wait for server answer
 while answer is not valid:
  bidNotValid()
  bidValue = waitForUserToBid()
  sendToServer(request, bidValue)
  #wait for server answer
