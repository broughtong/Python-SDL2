from ._model import ffi, lib

def createWindow(title, x, y, w, h, flags=0):

	if flags == None:
		flags = 0

	res = lib.SDL_CreateWindow(ffi.new("char[]", title.encode('utf-8')), x, y, w, h, flags)
	return res

