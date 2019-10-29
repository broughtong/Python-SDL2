from ._model import ffi, lib

def getCPUCacheLineSize():
	return lib.SDL_GetCPUCacheLineSize()
	
def getCPUCount():
	return lib.SDL_GetCPUCount()

def getSystemRAM():
	return lib.SDL_GetSystemRAM()
	
def has3DNow():
	return bool(lib.SDL_Has3DNow())
	
def hasAVX():
	return bool(lib.SDL_HasAVX())
	
def hasAVX2():
	return bool(lib.SDL_HasAVX2())
	
def hasAltiVec():
	return bool(lib.SDL_HasAltiVec())
	
def hasMMX():
	return bool(lib.SDL_HasMMX())
	
def hasRDTSC():
	return bool(lib.SDL_HasRDTSC())
	
def hasSSE():
	return bool(lib.SDL_HasSSE())
	
def hasSSE2():
	return bool(lib.SDL_HasSSE2())
	
def hasSSE3():
	return bool(lib.SDL_HasSSE3())
	
def hasSSE41():
	return bool(lib.SDL_HasSSE41())
	
def hasSSE42():
	return bool(lib.SDL_HasSSE42())
