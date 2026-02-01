import time
pin = 6398

   
password = int (input("Enter your password"))

if(pin==password):
    time.sleep(3)
    print("Login success")
    while True:
        print("=======this is my option==========")
        
        print("Enter your choice")
else:
    print("Error")
    