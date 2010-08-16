Name:		lightning
# 1.2.c is last release, but use a git snapshot with known bug fixes
Version:	1.2.c.20100816
Release:	%mkrel 1
Summary:	Portable just-in-time compiler library
License:	GPLv3
Group:		Development/Other
Source0:	http://git.savannah.gnu.org/cgit/lightning.git/snapshot/lightning-master.tar.gz
URL:		http://www.gnu.org/software/lightning/
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	help2man
BuildRequires:	info-install
BuildRequires:	texinfo

%description
GNU lightning is a library that generates assembly language code at run-time;
it is very fast, making it ideal for Just-In-Time compilers, and it abstracts
over the target CPU, as it exposes to the clients a standardized RISC
instruction set inspired by the MIPS and SPARC chips.

%prep
%setup -q -n %{name}-master

%build
%configure
%make

%check
make check

%install
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/lightningize
%{_includedir}/%{name}.h
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_datadir}/%{name}/Makefile.am
%{_datadir}/aclocal/%{name}.m4
%{_infodir}/%{name}.info*
%{_mandir}/man1/lightningize.1.lzma
