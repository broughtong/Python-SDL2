from cffi import FFI
ffibuilder = FFI()

# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
ffibuilder.cdef("""
#define SDL_INIT_TIMER          0x00000001u
#define SDL_INIT_AUDIO          0x00000010u
#define SDL_INIT_VIDEO          0x00000020u
#define SDL_INIT_JOYSTICK	0x00000200u
#define SDL_INIT_HAPTIC         0x00001000u
#define SDL_INIT_GAMECONTROLLER 0x00002000u
#define SDL_INIT_EVENTS         0x00004000u
//#define SDL_INIT_SENSOR         0x00008000u
#define SDL_INIT_NOPARACHUTE    0x00100000u
#define SDL_INIT_EVERYTHING		0x0010f231u
/*#define SDL_INIT_EVERYTHING ( \
                SDL_INIT_TIMER | SDL_INIT_AUDIO | SDL_INIT_VIDEO | SDL_INIT_EVENTS | \
                SDL_INIT_JOYSTICK | SDL_INIT_HAPTIC | SDL_INIT_GAMECONTROLLER | SDL_INIT_SENSOR \
            )*/

int SDL_Init(uint32_t flags);
int SDL_InitSubSystem(uint32_t flags);
void SDL_QuitSubSystem(uint32_t flags);
uint32_t SDL_WasInit(uint32_t flags);
void SDL_Quit();
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
