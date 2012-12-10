Name:		lightning
# 1.2.c is last release, but use a git snapshot with known bug fixes
Version:	1.2.c.20100903
Release:	2
Summary:	Portable just-in-time compiler library
License:	GPLv3
Group:		Development/Other

# Actually using:
#	http://github.com/pcpa/lightning/archives/master
#	then unpacking/renaming base directory and packing again
Source0:	http://git.savannah.gnu.org/cgit/lightning.git/snapshot/lightning-master.tar.gz
URL:		http://www.gnu.org/software/lightning/

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

%files
%{_bindir}/lightningize
%{_includedir}/%{name}.h
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_datadir}/%{name}/Makefile.am
%{_datadir}/aclocal/%{name}.m4
%{_infodir}/%{name}.info*
%{_mandir}/man1/lightningize.1*


%changelog
* Sat Sep 04 2010 Paulo Andrade <pcpa@mandriva.com.br> 1.2.c.20100903-1mdv2011.0
+ Revision: 575709
+ rebuild (emptylog)

* Fri Aug 27 2010 Paulo Andrade <pcpa@mandriva.com.br> 1.2.c.20100826-1mdv2011.0
+ Revision: 573448
+ rebuild (emptylog)

* Wed Aug 25 2010 Paulo Andrade <pcpa@mandriva.com.br> 1.2.c.20100825-1mdv2011.0
+ Revision: 573350
- Update to a new git snapshot

* Mon Aug 16 2010 Paulo Andrade <pcpa@mandriva.com.br> 1.2.c.20100816-1mdv2011.0
+ Revision: 570583
- Update to latest git master

* Tue Aug 10 2010 Paulo Andrade <pcpa@mandriva.com.br> 1.2.c.20100810-1mdv2011.0
+ Revision: 568838
- Update to new git snapshot

* Fri Jul 30 2010 Paulo Andrade <pcpa@mandriva.com.br> 1.2.c.20100730-1mdv2011.0
+ Revision: 563811
- Update to a newer git snapshot.

* Mon May 10 2010 Paulo Andrade <pcpa@mandriva.com.br> 1.2.c.20091009-2mdv2010.1
+ Revision: 544445
+ rebuild (emptylog)

* Fri Oct 09 2009 Paulo Andrade <pcpa@mandriva.com.br> 1.2.c.20091009-1mdv2010.0
+ Revision: 456467
- Import GNU lightning.
- lightning

