from microbit import *
from neopixel import NeoPixel

num_pixels = 24
foreground = [0x00, 0x00, 0xFF]  # Hex color - red, green and blue
background = [0x10, 0x10, 0x10]

# 0 is between data in and data out
temperature_leds = [0,1,2,3]
gsr_leds = [12,13,14,15] # ranges from 200 (very sweaty) to 650 (not touching sensor)
sound_leds = [4,5,6,7]
heart_rate_leds = [20,21,22,23]
acc_leds = [8,9,10,11]
mood_leds = [16,17,18,19] # overall mood

ring = NeoPixel(pin2, num_pixels)

while True:
    # Sound LEDs
    sound_level = microphone.sound_level()
    sound_color = None
    
    if sound_level <= 16:
        #blue_component = int(17/(sound_level+1)) * 0xFF
        blue_component = int((sound_level+1)/17) * 0xFF
        sound_color = [0x00, 0x00, int(blue_component/2)]
    elif sound_level <= 32:
        #green_component = int(33/(sound_level+1)) * 0xFF
        green_component = int((sound_level+1))/33 * 0xFF
        sound_color = [0x00, int(green_component/2), int(0xFF/2)]
    elif sound_level <= 48:
        #red_component = int(49/(sound_level+1)) * 0xFF
        red_component = int((sound_level+1)/49) * 0xFF
        sound_color = [int(red_component/2), int(0xFF/2), 0x00]
    else:
        sound_color = [int(0xFF/2), 0x00, 0x00]
    
    for sound_led in sound_leds:
        ring[sound_led] = sound_color
        ring.show()
        sleep(50)
        
        
    # Accelerometer LEDs
    acc_sum = abs(accelerometer.get_x()) + abs(accelerometer.get_y()) + abs(accelerometer.get_z())
    #print("acc_sum: " + str(acc_sum))
    acc_color = None
    
    if acc_sum <= 1000:
        #blue_component = int(1501/(acc_sum+1)) * 0xFF
        blue_component = int((acc_sum+1)/1501) * 0xFF
        acc_color = [0x00, 0x00, int(blue_component/2)]
    elif acc_sum <= 1200:
        #green_component = int(1701/(acc_sum+1)) * 0xFF
        green_component = int((acc_sum+1)/1701) * 0xFF
        acc_color = [0x00, int(green_component/2), int(0xFF/2)]
    elif acc_sum <= 1400:
        #red_component = int(1901/(acc_sum+1)) * 0xFF
        red_component = int((acc_sum+1)/1901) * 0xFF
        acc_color = [red_component, int(0xFF/2), 0x00]
    else:
        acc_color = [int(0xFF/2), 0x00, 0x00]
   
    for acc_led in acc_leds:
        ring[acc_led] = acc_color
        ring.show()
        sleep(50)
        
    # Temperature LEDs
    temp = temperature()
    temp_color = None
    
    if temp <= 24:
        #blue_component = int(25/(temp+1)) * 0xFF
        blue_component = int((temp+1)/25) * 0xFF
        temp_color = [0x00, 0x00, int(blue_component/2)]
    elif temp <= 30:
        #green_component = int(31/(temp+1)) * 0xFF
        green_component = int((temp+1)/31) * 0xFF
        temp_color = [0x00, int(green_component/2), int(0xFF/2)]
    elif temp <= 36:
        #red_component = int(37/(temp+1)) * 0xFF
        red_component = int((temp+1)/37) * 0xFF
        temp_color = [int(red_component/2), int(0xFF/2), 0x00]
    else:
        temp_color = [int(0xFF/2), 0x00, 0x00]
        
    for temp_led in temperature_leds:
        ring[temp_led] = temp_color
        ring.show()
        sleep(50)
        
    # GSR LEDs
    gsr = pin0.read_analog()
    #print("gsr: " + str(gsr))
    gsr_color = None
    
    if gsr <= 200:
        gsr_color = [int(0xFF/2), 0x00, 0x00]
    elif gsr <= 250:
        #red_component = int(251/(gsr+1)) * 0xFF
        red_component = int((gsr+1)/251) * 0xFF
        gsr_color = [int(red_component/2), int(0xFF/2), 0x00]
    elif gsr <= 350:
        #green_component = int(351/(gsr+1)) * 0xFF
        green_component = int((gsr+1)/351) * 0xFF
        gsr_color = [0x00, int(green_component/2), int(0xFF/2)]
    elif gsr <= 500:
        #green_component = int(501/(gsr+1)) * 0xFF
        green_component = int((gsr+1)/501) * 0xFF
        gsr_color = [0x00, int(green_component/2), int(0xFF/2)]
    else:
        #blue_component = int(650/(gsr+1)) * 0xFF
        blue_component = int((gsr+1)/650) * 0xFF
        gsr_color = [0x00, 0x00, int(blue_component/2)]
        
    for gsr_led in gsr_leds:
        ring[gsr_led] = gsr_color
        ring.show()
        sleep(50)
    
    
    # Heart rate LEDs
    #hr = pins.analog_read_pin(AnalogPin.P1)
    hr = pin1.read_analog()
    print("hr: " + str(hr))
    hr_color = None
    
    if hr <= 100:
        blue_component = int((hr+1)/101) * 0xFF
        hr_color = [0x00, 0x00, int(blue_component/2)]
    elif hr <= 500:
        green_component = int((hr+1)/501) * 0xFF
        hr_color = [0x00, int(green_component/2), int(0xFF/2)]
    elif hr <= 900:
        red_component = int((hr+1)/901) * 0xFF
        hr_color = [int(red_component/2), int(0xFF/2), 0x00]
    else:
        hr_color = [int(0xFF/2), 0x00, 0x00]
        
    for hr_led in heart_rate_leds:
        ring[hr_led] = hr_color
        ring.show()
        sleep(50)
        
    
    # Overall mood LEDs
    mood_color = [int((sound_color[0]+acc_color[0]+temp_color[0]+gsr_color[0]+hr_color[0])/10), 
    int((sound_color[1]+acc_color[1]+temp_color[1]+gsr_color[1]+hr_color[1])/10), 
    int((sound_color[2]+acc_color[2]+temp_color[2]+gsr_color[2]+hr_color[2])/10)]
    for mood_led in mood_leds:
        ring[mood_led] = mood_color
        ring.show()
        sleep(50)
        
    
        
    