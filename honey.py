from twilio.rest import Client 
 
account_sid = 'AC708c100bd6e92969a434fc101ea4d91f' 
auth_token = 'def213828937ec289d87ff4e117b1bf6' 
client = Client(account_sid, auth_token) 
def send():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='We are experimenting',      
                              to='whatsapp:+254797578553' 
                          ) 
 
    print(message.sid)