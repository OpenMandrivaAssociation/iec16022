# TODO: shared lib calls exit

%define name	iec16022
%define version	0.2.4
%define rel	2

%define major	0
%define libname	%mklibname %{name}_ %{major}
%define devname	%mklibname %{name} -d

Name:           %{name}
Version:        %{version}
Release:        %mkrel %{rel}
Summary:        Generate ISO/IEC 16022 2D barcodes
Group:          Graphics
License:        GPLv2+
URL:            http://www.datenfreihafen.org/projects/iec16022.html
Source0:        http://www.datenfreihafen.org/~stefan/iec16022/%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}-test-suite-fix.patch

BuildRequires:  popt-devel
BuildRequires:	zlib-devel

%description
iec16022 is a program for producing ISO/IEC 16022 2D barcodes, also
known as Data Matrix.  These barcodes are defined in the ISO/IEC 16022
standard.

%package -n %{libname}
Summary:	ISO/IEC 16022 libraries
Group:		System/Libraries

%description -n %{libname}
Shared libraries for %{name}.

%package -n %{devname}
Summary:	ISO/IEC 16022 development files
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description  -n %{devname}
Development files for %{name}.

%prep
%setup -q
%patch0 -p1 -b .orig

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#we don't want these
rm -f %{buildroot}%{_libdir}/libiec16022.la

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%make -C test check

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/iec16022
%{_mandir}/man1/iec16022.1*

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%{_libdir}/libiec16022.so.%{major}*

%files -n %{devname}
%defattr(-,root,root)
%{_includedir}/iec16022/
%{_libdir}/libiec16022.so
%{_libdir}/pkgconfig/libiec16022.pc
