import pythonsdl2 as sdl

powerStatus = sdl.power.getPowerInfo()

print(f"Battery Status: {powerStatus[0]}")
print(f"Battery Time Left: {powerStatus[1]}s")
print(f"Battery Percent: {powerStatus[2]}%")