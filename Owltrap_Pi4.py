### Owl Trap ###

from requests_oauthlib import OAuth1Session

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)                                  # number indicates the GPIO pin for the switch (7)
GPIO.setup(12,GPIO.OUT)                                                             # number indicates the GPIO pin for the servo PWM signal (12)

GPIO.setwarnings(False)
p=GPIO.PWM(12,50)

global owl_count
owl_count = 0

key = '[gatewayapi key]'                                                            # replace [gatewayapi key] with your gatewayapi key
secret = '[gatewayapi secret]'                                                      # replace [gatewayapi secret] with your gatewayapi secret
gwapi = OAuth1Session(key, client_secret=secret) 

def owl(channel):
  while True: 
      if (GPIO.input(7) == GPIO.HIGH):
          p.start(0)
          p.ChangeDutyCycle(5)                                                      # Turns the servo 90deg left 
          sleep(1)                                                                  # Indicates how many seconds before the trap returns to the waiting position
          global owl_count
          owl_count += 1
          print (owl_count)
          p.ChangeDutyCycle(10) 
          sleep(5)                                        
          if owl_count > 1:
            req = {                                                                 #Line 31 - 40 is for the Gateway API, replace this with appropriate code if you use another service
                 'sender': 'OwlTrap',
                 'message': 'You have caught an Owl in trap 1!',                    # The message can be changed
                 'recipients': [{'msisdn': [phone number]}],                        # replace [phone number] with the number that should receive the text message. Include country code (e.g. 44 for UK)
            }
            res = gwapi.post('https://gatewayapi.com/rest/mtsms', json=req)
            res.raise_for_status()
            print(res.json())
            import sys
            sys.exit()

GPIO.add_event_detect(7,GPIO.FALLING,callback=owl)
try:
  while True:
     sleep(1)
except KeyboardInterrupt: