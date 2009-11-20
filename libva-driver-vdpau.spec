Summary:	VDPAU driver for VAAPI
Name:		libva-driver-vdpau
Version:	0.5.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.splitted-desktop.com/~gbeauchesne/vdpau-video/vdpau-video-%{version}.tar.gz
# Source0-md5:	fc88b793d35c4389752a8331a9201778
URL:		http://www.freedesktop.org/wiki/Software/vaapi
BuildRequires:	libva-devel
BuildRequires:	libvdpau-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A VDPAU-based backend for VA API.

%prep
%setup -q -n vdpau-video-%{version}

%build
%configure \
	--with-drivers-path=%{_libdir}/%{name}/dri

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libva/dri/*.so
