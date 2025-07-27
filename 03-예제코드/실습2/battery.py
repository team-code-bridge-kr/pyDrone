from machine import Pin, ADC, Timer

adc = ADC(Pin(2))

def ADC_TEST(tim):
    v = adc.read() / 4095 * 5.02 * 0.96

    print("Battery : " + str('%.2f' % v) + 'V')

tim = Timer(1)
tim.init(period=1000, mode=Timer.PERIODIC, callback=ADC_TEST)