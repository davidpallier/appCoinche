
#Wait for server request
If request is 'Status':
 status = waitForUserToUpdateStatus()
 sendToServer(request, status)
 
Elif request is 'Play a card':
 card = waitForUserToPlayCard()
 sendToServer(request, card)
 #wait for server answer
 while answer is not valid:
  cardNotValid()
  card = waitForUserToPlayCard()
  sendToServer(request, card)
  #wait for server answer
