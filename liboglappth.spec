Summary:	Library for portable OpenGL applications
Summary(pl.UTF-8):	Biblioteka dla przenośnych aplikacji OpenGL
Name:		liboglappth
Version:	0.98
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://bioinformatics.org/ghemical/download/current/%{name}-%{version}.tar.gz
# Source0-md5:	dd280286a51fcba6a47264a383a2f1fe
URL:		http://bioinformatics.org/ghemical/ghemical/index.html
BuildRequires:	Mesa-libGLU-devel
BuildRequires:	glut-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for creating portable OpenGL applications with easy-to-code
scene setup and selection operations.

%description -l pl.UTF-8
Biblioteka do tworzenia przenośnych aplikacji OpenGL z łatwymi do
kodowania operacjami tworzenia i wyboru sceny.

%package devel
Summary:	Header files for liboglappth library
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotekliboglappth
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLU-devel
Requires:	OpenGL-glut-devel
Requires:	libstdc++-devel

%description devel
Header files for liboglappth library.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotekliboglappth.

%package static
Summary:	Static liboglappth library
Summary(pl.UTF-8):	Statyczna biblioteka liboglappth
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liboglappth library.

%description static -l pl.UTF-8
Statyczna biblioteka liboglappth.

%prep
%setup -q

%build
%configure
# pass LIBS to override "-L/usr/X11R6/lib" (unwanted especially on archs using lib64)
%{__make} \
	LIBS="-lglut -lGLU -lGL -lm"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/%{name}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}.so
%{_libdir}/%{name}.la
%{_includedir}/oglappth
%{_pkgconfigdir}/%{name}.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/%{name}.a
