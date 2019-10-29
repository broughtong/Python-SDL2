from ._model import ffi, lib

def init(flags):
	return lib.SDL_Init(flags)

def initSubSystem(flags):
	return lib.SDL_InitSubSystem(flags)

def quitSubSystem(flags):
	lib.SDL_QuitSubSystem(flags)

def wasInit(flags):
	return lib.SDL_WasInit(flags) == flags

def quit():
	lib.SDL_Quit()
