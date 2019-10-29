from cffi import FFI
ffibuilder = FFI()

# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
ffibuilder.cdef("""
typedef enum
{
    /* !!! FIXME: change this to name = (1<<x). */
    SDL_WINDOW_FULLSCREEN = 0x00000001,         /**< fullscreen window */
    SDL_WINDOW_OPENGL = 0x00000002,             /**< window usable with OpenGL context */
    SDL_WINDOW_SHOWN = 0x00000004,              /**< window is visible */
    SDL_WINDOW_HIDDEN = 0x00000008,             /**< window is not visible */
    SDL_WINDOW_BORDERLESS = 0x00000010,         /**< no window decoration */
    SDL_WINDOW_RESIZABLE = 0x00000020,          /**< window can be resized */
    SDL_WINDOW_MINIMIZED = 0x00000040,          /**< window is minimized */
    SDL_WINDOW_MAXIMIZED = 0x00000080,          /**< window is maximized */
    SDL_WINDOW_INPUT_GRABBED = 0x00000100,	/**< window has grabbed input focus */
    SDL_WINDOW_INPUT_FOCUS = 0x00000200,        /**< window has input focus */
    SDL_WINDOW_MOUSE_FOCUS = 0x00000400,        /**< window has mouse focus */
    SDL_WINDOW_FULLSCREEN_DESKTOP = ( SDL_WINDOW_FULLSCREEN | 0x00001000 ),
    SDL_WINDOW_FOREIGN = 0x00000800,            /**< window not created by SDL */
    SDL_WINDOW_ALLOW_HIGHDPI = 0x00002000,	/**< window should be created in high-DPI mode if supported.
                                                     On macOS NSHighResolutionCapable must be set true in the
                                                     application's Info.plist for this to have any effect. */
    SDL_WINDOW_MOUSE_CAPTURE = 0x00004000,	/**< window has mouse captured (unrelated to INPUT_GRABBED) */
    SDL_WINDOW_ALWAYS_ON_TOP = 0x00008000,	/**< window should always be above others */
    SDL_WINDOW_SKIP_TASKBAR  = 0x00010000,	/**< window should not be added to the taskbar */
    SDL_WINDOW_UTILITY       = 0x00020000,	/**< window should be treated as a utility window */
    SDL_WINDOW_TOOLTIP       = 0x00040000,	/**< window should be treated as a tooltip */
    SDL_WINDOW_POPUP_MENU    = 0x00080000,	/**< window should be treated as a popup menu */
    SDL_WINDOW_VULKAN        = 0x10000000	/**< window usable for Vulkan surface */
} SDL_WindowFlags;

typedef struct SDL_Window SDL_Window;



int SDL_GetNumVideoDrivers(void);
const char *SDL_GetVideoDriver(int index);
int SDL_VideoInit(const char *driver_name);
void SDL_VideoQuit(void);
const char *SDL_GetCurrentVideoDriver(void);
int SDL_GetNumVideoDisplays(void);
const char * SDL_GetDisplayName(int displayIndex);
int SDL_GetDisplayBounds(int displayIndex, SDL_Rect * rect);
int SDL_GetDisplayUsableBounds(int displayIndex, SDL_Rect * rect);
int SDL_GetDisplayDPI(int displayIndex, float * ddpi, float * hdpi, float * vdpi);
SDL_DisplayOrientation SDL_GetDisplayOrientation(int displayIndex);
int SDL_GetNumDisplayModes(int displayIndex);
int SDL_GetDisplayMode(int displayIndex, int modeIndex, SDL_DisplayMode * mode);
int SDL_GetDesktopDisplayMode(int displayIndex, SDL_DisplayMode * mode);
int SDL_GetCurrentDisplayMode(int displayIndex, SDL_DisplayMode * mode);
SDL_DisplayMode * SDL_GetClosestDisplayMode(int displayIndex, const SDL_DisplayMode * mode, SDL_DisplayMode * closest);
int SDL_GetWindowDisplayIndex(SDL_Window * window);
int SDL_SetWindowDisplayMode(SDL_Window * window, const SDL_DisplayMode * mode);
int SDL_GetWindowDisplayMode(SDL_Window * window, SDL_DisplayMode * mode);
Uint32 SDL_GetWindowPixelFormat(SDL_Window * window);
SDL_Window * SDL_CreateWindow(const char *title, int x, int y, int w, int h, Uint32 flags);
SDL_Window * SDL_CreateWindowFrom(const void *data);
Uint32 SDL_GetWindowID(SDL_Window * window);
SDL_Window * SDL_GetWindowFromID(Uint32 id);
Uint32 SDL_GetWindowFlags(SDL_Window * window);
void SDL_SetWindowTitle(SDL_Window * window, const char *title);
const char *SDL_GetWindowTitle(SDL_Window * window);
void SDL_SetWindowIcon(SDL_Window * window, SDL_Surface * icon);
void* SDL_SetWindowData(SDL_Window * window, const char *name, void *userdata);
void *SDL_GetWindowData(SDL_Window * window, const char *name);
void SDL_SetWindowPosition(SDL_Window * window,
void SDL_GetWindowPosition(SDL_Window * window,
void SDL_SetWindowSize(SDL_Window * window, int w,
void SDL_GetWindowSize(SDL_Window * window, int *w,
int SDL_GetWindowBordersSize(SDL_Window * window,
void SDL_SetWindowMinimumSize(SDL_Window * window,
void SDL_GetWindowMinimumSize(SDL_Window * window,
void SDL_SetWindowMaximumSize(SDL_Window * window,
void SDL_GetWindowMaximumSize(SDL_Window * window,
void SDL_SetWindowBordered(SDL_Window * window,
void SDL_SetWindowResizable(SDL_Window * window,
void SDL_ShowWindow(SDL_Window * window);
void SDL_HideWindow(SDL_Window * window);
void SDL_RaiseWindow(SDL_Window * window);
void SDL_MaximizeWindow(SDL_Window * window);
void SDL_MinimizeWindow(SDL_Window * window);
void SDL_RestoreWindow(SDL_Window * window);
int SDL_SetWindowFullscreen(SDL_Window * window,
SDL_Surface * SDL_GetWindowSurface(SDL_Window * window);
int SDL_UpdateWindowSurface(SDL_Window * window);
int SDL_UpdateWindowSurfaceRects(SDL_Window * window,
void SDL_SetWindowGrab(SDL_Window * window,
SDL_bool SDL_GetWindowGrab(SDL_Window * window);
SDL_Window * SDL_GetGrabbedWindow(void);
int SDL_SetWindowBrightness(SDL_Window * window, float brightness);
float SDL_GetWindowBrightness(SDL_Window * window);
int SDL_SetWindowOpacity(SDL_Window * window, float opacity);
int SDL_GetWindowOpacity(SDL_Window * window, float * out_opacity);
int SDL_SetWindowModalFor(SDL_Window * modal_window, SDL_Window * parent_window);
int SDL_SetWindowInputFocus(SDL_Window * window);
int SDL_SetWindowGammaRamp(SDL_Window * window,
int SDL_GetWindowGammaRamp(SDL_Window * window,
typedef SDL_HitTestResult (*SDL_HitTest)(SDL_Window *win,
int SDL_SetWindowHitTest(SDL_Window * window,
void SDL_DestroyWindow(SDL_Window * window);
SDL_bool SDL_IsScreenSaverEnabled(void);
void SDL_EnableScreenSaver(void);
void SDL_DisableScreenSaver(void);
int SDL_GL_LoadLibrary(const char *path);
void *SDL_GL_GetProcAddress(const char *proc);
void SDL_GL_UnloadLibrary(void);
SDL_bool SDL_GL_ExtensionSupported(const char
void SDL_GL_ResetAttributes(void);
int SDL_GL_SetAttribute(SDL_GLattr attr, int value);
int SDL_GL_GetAttribute(SDL_GLattr attr, int *value);
SDL_GLContext SDL_GL_CreateContext(SDL_Window *
int SDL_GL_MakeCurrent(SDL_Window * window,
SDL_Window* SDL_GL_GetCurrentWindow(void);
SDL_GLContext SDL_GL_GetCurrentContext(void);
void SDL_GL_GetDrawableSize(SDL_Window * window, int *w,
int SDL_GL_SetSwapInterval(int interval);
int SDL_GL_GetSwapInterval(void);
void SDL_GL_SwapWindow(SDL_Window * window);
void SDL_GL_DeleteContext(SDL_GLContext context);

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
