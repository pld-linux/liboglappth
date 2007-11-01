Summary:	-
Summary(pl.UTF-8):	-j
Name:		liboglappth
Version:	0.96
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://bioinformatics.org/ghemical/download/current/%{name}-%{version}.tar.gz
# Source0-md5:	babb1907ca0a52c6879c003239701217
URL:		http://bioinformatics.org/ghemical/ghemical/index.html
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
-

%description -l pl.UTF-8
-

%package devel
Summary:	Header files for liboglappth library
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotekliboglappth
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
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
%{__make}

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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}.so
%{_libdir}/%{name}.la
%{_includedir}/oglappth
%{_pkgconfigdir}/%{name}.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/%{name}.a
