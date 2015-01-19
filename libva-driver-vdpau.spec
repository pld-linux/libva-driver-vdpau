Summary:	VDPAU driver for VAAPI
Summary(pl.UTF-8):	Sterownik VDPAU dla VAAPI
Name:		libva-driver-vdpau
Version:	0.7.4
Release:	3
License:	GPL v2+
Group:		Libraries
Source0:	http://www.freedesktop.org/software/vaapi/releases/libva-vdpau-driver/libva-vdpau-driver-%{version}.tar.bz2
# Source0-md5:	5ec6d452d2dd307434ea3d32da49c3e5
Patch0:		%{name}-with-GL_GLEXT_VERSION-85.patch
Patch1:		%{name}-am.patch
Patch2:		%{name}-drop-h264-api.patch
Patch3:		libva-vdpau-driver-0.7.4-fix_type.patch
URL:		http://www.freedesktop.org/wiki/Software/vaapi
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libva-devel
BuildRequires:	libva-glx-devel >= 1.0.9
BuildRequires:	libva-x11-devel >= 1.0.3
BuildRequires:	libvdpau-devel
BuildRequires:	pkgconfig
# more specific than libva package version
BuildRequires:	pkgconfig(libva-x11) >= 0.31.0
BuildRequires:	pkgconfig(libva-glx) >= 0.32.0
Requires:	libva >= 1.0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A VDPAU-based backend for VA API.

%description -l pl.UTF-8
Sterownik oparty na VDPAU dla VAAPI.

%prep
%setup -q -n libva-vdpau-driver-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-glx \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libva/dri/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libva/dri/vdpau_drv_video.so
# symlinks
%attr(755,root,root) %{_libdir}/libva/dri/nvidia_drv_video.so
%attr(755,root,root) %{_libdir}/libva/dri/s3g_drv_video.so
