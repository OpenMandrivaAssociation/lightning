%define _disable_ld_no_undefined 1

Name:		lightning
Version:	2.0.0
Release:	1
Summary:	Portable just-in-time compiler library
License:	LGPLv3+
Source0:	ftp://ftp.gnu.org/gnu/lightning/lightning-2.0.0.tar.gz
Source1:	%{name}.rpmlintrc
URL:		http://www.gnu.org/software/lightning/
BuildRequires:	binutils-devel
BuildRequires:	texinfo

%description
GNU lightning is a library that generates assembly language code at run-time;
it is very fast, making it ideal for Just-In-Time compilers, and it abstracts
over the target CPU, as it exposes to the clients a standardized RISC
instruction set inspired by the MIPS and SPARC chips. 

%package	devel
Summary:	Development tools for the GNU lightning
Requires:	%{name} = %{version}-%{release}

%description devel
The libraries, header files and documentation for using GNU lightning.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%check
make check

%files
%doc AUTHORS COPYING COPYING.LESSER NEWS README THANKS
%{_libdir}/lib%{name}.so.*

%files	devel
%doc ChangeLog COPYING.DOC
%{_includedir}/%{name}.h
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_infodir}/%{name}.info*
