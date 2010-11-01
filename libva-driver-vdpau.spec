Summary:	VDPAU driver for VAAPI
Summary(pl.UTF-8):	Sterownik VDPAU dla VAAPI
Name:		libva-driver-vdpau
Version:	0.7.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.splitted-desktop.com/~gbeauchesne/vdpau-video/vdpau-video-%{version}.tar.gz
# Source0-md5:	7d8e77a41352ceaa3fc20d137eb4f8b9
URL:		http://www.freedesktop.org/wiki/Software/vaapi
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libva-devel
BuildRequires:	libvdpau-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A VDPAU-based backend for VA API.

%description -l pl.UTF-8
Sterownik oparty na VDPAU dla VAAPI.

%prep
%setup -q -n vdpau-video-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

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
