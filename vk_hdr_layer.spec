Name:           vk_hdr_layer
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Vulkan layer utilizing work-in-progress versions of the color management/representation protocols.

License:        MIT
URL:            https://github.com/Drakulix/VK_hdr_layer
Source:         {{{ git_dir_pack }}}

BuildRequires:  meson >= 0.54.0
BuildRequires:  ninja-build
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(vkroots)

%description
Hacks. Don't use for serious color work. - Vulkan layer utilizing work-in-progress versions of the color management/representation protocols.

%prep
{{{ git_dir_setup_macro }}}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_datadir}/vulkan/implicit_layer.d/*
%{_libdir}/*.so
