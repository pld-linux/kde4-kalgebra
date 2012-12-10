%define		_state		stable
%define		orgname		kalgebra

Summary:	K Desktop Environment - Mathematical calculator
Name:		kde4-kalgebra
Version:	4.9.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	a40c7a4ab0beb202e455ca35de7d83f6
URL:		http://www.kde.org/
BuildRequires:	OpenGL-devel
BuildRequires:	kde4-analitza-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdeedu-devel >= %{version}
BuildRequires:	readline-devel
Obsoletes:	kde4-kdeedu-kalgebra < 4.6.99
Obsoletes:	kalgebra < 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KAlgebra is a mathematical calculator based on MathML content markup
language.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalgebra
%attr(755,root,root) %{_bindir}/kalgebramobile
%{_desktopdir}/kde4/kalgebra.desktop
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_kalgebra.so
%{_datadir}/kde4/services/kalgebraplasmoid.desktop
%{_iconsdir}/hicolor/*x*/apps/kalgebra.png
%{_iconsdir}/hicolor/scalable/apps/kalgebra.svgz
%{_datadir}/apps/katepart/syntax/kalgebra.xml
%{_desktopdir}/kde4/kalgebramobile.desktop
%{_datadir}/apps/kalgebramobile
