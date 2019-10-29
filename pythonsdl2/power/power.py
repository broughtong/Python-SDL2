from ._model import ffi, lib

def getPowerInfo():

	pSecs = ffi.new("int *")
	pPct = ffi.new("int *")

	res = lib.SDL_GetPowerInfo(pSecs, pPct)

	states = [
		"UNKNOWN",
		"ON_BATTERY",
		"NO_BATTERY",
		"CHARGING",
		"CHARGED"
	]

	return (states[res], pSecs[0], pPct[0])