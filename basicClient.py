
#Wait for server request
If request is 'Status':
 
Elif request is 'Play a card':
 card = waitForUserToPlayCard()
 sendToServer(request, card)
 #wait for server answer
 while answer is not valid:
  card = waitForUserToPlayCard()
  sendToServer(request, card)
  wait for server answer
