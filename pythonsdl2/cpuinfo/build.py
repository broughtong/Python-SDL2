from cffi import FFI
ffibuilder = FFI()

# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
ffibuilder.cdef("""
typedef enum
{
    SDL_FALSE = 0,
    SDL_TRUE = 1
} SDL_bool;

int SDL_GetCPUCacheLineSize(void);
int SDL_GetCPUCount(void);
int SDL_GetSystemRAM(void);
SDL_bool SDL_Has3DNow(void);
SDL_bool SDL_HasAVX(void);
SDL_bool SDL_HasAVX2(void);
SDL_bool SDL_HasAltiVec(void);
SDL_bool SDL_HasMMX(void);
SDL_bool SDL_HasRDTSC(void);
SDL_bool SDL_HasSSE(void);
SDL_bool SDL_HasSSE2(void);
SDL_bool SDL_HasSSE3(void);
SDL_bool SDL_HasSSE41(void);
SDL_bool SDL_HasSSE42(void);
""")

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source("_model",
"""
#include "SDL2/SDL.h"
""",
	libraries=['SDL2'])

ffibuilder.compile(verbose=True)
