%define _disable_ld_no_undefined 1

%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Portable just-in-time compiler library
Name:		lightning
Version:	2.0.3
Release:	1
License:	LGPLv3+
Group:		Development/Other
Url:		http://www.gnu.org/software/lightning/
Source0:	ftp://ftp.gnu.org/gnu/lightning/%{name}-%{version}.tar.gz
BuildRequires:	texinfo
BuildRequires:	binutils-devel
BuildRequires:	pkgconfig(zlib)

%description
GNU lightning is a library that generates assembly language code at run-time;
it is very fast, making it ideal for Just-In-Time compilers, and it abstracts
over the target CPU, as it exposes to the clients a standardized RISC
instruction set inspired by the MIPS and SPARC chips.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library the GNU lightning
Group:		System/Libraries
Conflicts:	%{name} < 2.0.3
Obsoletes:	%{name} < 2.0.3

%description -n %{libname}
Shared library the GNU lightning.

%files -n %{libname}
%doc AUTHORS COPYING COPYING.LESSER NEWS README THANKS
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for the GNU lightning
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{name} < 2.0.3

%description -n %{devname}
The libraries, header files and documentation for using GNU lightning.

%files -n %{devname}
%doc ChangeLog COPYING.DOC
%{_includedir}/%{name}.h
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_infodir}/%{name}.info*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%check
make check

