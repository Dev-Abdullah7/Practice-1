# Write a program that breaks the loop when a certain condition is met.


counter = 0

while True:
    counter += 1  
    print("Counter:", counter) 

    if counter == 7:
        print("Reached 7 Stopping the loop.")
        break 
