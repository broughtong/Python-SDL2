from ._model import ffi, lib

def getPlatform():
	return ffi.string(lib.SDL_GetPlatform())