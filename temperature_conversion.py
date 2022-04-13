#Written by Sahil Patel
#this program converts between celsius and fahrenheit with input given as an integer or a floating number following letter f (for fahrenheit) or c (for celsius)

def run():
    def temp_conversion():
        temperature = input("Enter temperature in degrees and letter f or c to represent fahrenheit and celsius respectively : ")

        if("f" in temperature or "F" in temperature):
            fahrenheit_to_celsius(float(temperature[:-1]))
        elif("c" in temperature or "C" in temperature):
            celsius_to_fahrenheit(float(temperature[:-1]))

    def celsius_to_fahrenheit(temperature):
        print(temperature, "celsius : ", round((temperature * (9/5) + 32),2), " fahrenheit")
        #print((temperature * (9/5)) + 32) #convert to fahrenheit
        return round((temperature * (9/5)) + 32,2)

    def fahrenheit_to_celsius(temperature):
        print(temperature, " fahrenheit :", round((temperature - 32) * 5/9,2), " celsius")
        #print((temperature - 32) * 5/9) #convert to celsius
        return round((temperature - 32) * 5/9,2)

    key = input("Enter r to run or q to quit : ")
    while(key.lower() == "r"):
        temp_conversion()
        key = input("Enter r to run again or q to quit : ")
    
run()