import machine, onewire, time, ds18x20

data = machine.Pin(14)

ds = ds18x20.DS18X20(onewire.OneWire(data))

roms = ds.scan()
rom = roms[0]

ds.convert_temp()
time.sleep_ms(850)
print (ds.read_temp(rom))
