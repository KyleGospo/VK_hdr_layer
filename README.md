## Vulkan Wayland HDR WSI Layer

Implements the following vulkan extensions, if either frog-color-management-v1 or xx-color-management-v4 Wayland protocol is supported by the compositor:
- [VK_EXT_swapchain_colorspace](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VK_EXT_swapchain_colorspace.html)
- [VK_EXT_hdr_metadata](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VK_EXT_hdr_metadata.html)

KWin supports the frog protocol since Plasma 6.0, and xx-color-management-v4 in 6.2.

# Testing with Quake II RTX

Quake II RTX suports HDR when run in Wayland native mode with this Vulkan layer. To do that, put `SDL_VIDEODRIVER=wayland ENABLE_HDR_WSI=1 %command%` into its launch arguments.

### Testing with Wine Wayland

As of [Wine 9.0](https://gitlab.winehq.org/wine/wine/-/releases/wine-9.0), Wine's native wayland mode supports HDR through DXVK.    
To enable it, run `wine reg.exe add HKCU\\Software\\Wine\\Drivers /v Graphics /d x11,wayland` inside your Wine Prefix, Then unset the `DISPLAY` variable and set `DXVK_HDR=1`
Make sure you set `ENABLE_HDR_WSI=1` when running an application or game.

### Testing with Video Players

[mpv](https://mpv.io/) Supports HDR Video playback through Vulkan's HDR Surface.    
To play an HDR video, set `ENABLE_HDR_WSI=1` and run mpv with `--vo=gpu-next --target-colorspace-hint --gpu-api=vulkan --gpu-context=waylandvk`

# Gamescope
Gamescope implements color management protocols directly and this layer should *not* be used with it.
