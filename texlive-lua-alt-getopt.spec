# revision 17228
# category Package
# catalog-ctan /support/lua/lua-alt-getopt
# catalog-date 2010-03-13 15:46:59 +0100
# catalog-license other-free
# catalog-version 0.7.0
Name:		texlive-lua-alt-getopt
Version:	0.7.0
Release:	3
Summary:	Process application arguments the same way as getopt_long
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/lua/lua-alt-getopt
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-alt-getopt.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-alt-getopt.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
lua_altgetopt is a MIT-licensed module for Lua, for processing
application arguments in the same way as BSD/GNU getopt_long(3)
functions do. This module is made available for lua script
writers to have consistent command line parsing routines.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/lua-alt-getopt/alt_getopt.lua
%doc %{_texmfdistdir}/doc/support/lua-alt-getopt/ChangeLog
%doc %{_texmfdistdir}/doc/support/lua-alt-getopt/Makefile
%doc %{_texmfdistdir}/doc/support/lua-alt-getopt/NEWS
%doc %{_texmfdistdir}/doc/support/lua-alt-getopt/README
%doc %{_texmfdistdir}/doc/support/lua-alt-getopt/alt_getopt
%doc %{_texmfdistdir}/doc/support/lua-alt-getopt/tests/test.out
%doc %{_texmfdistdir}/doc/support/lua-alt-getopt/tests/test.sh

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.7.0-2
+ Revision: 753579
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.7.0-1
+ Revision: 718918
- texlive-lua-alt-getopt
- texlive-lua-alt-getopt
- texlive-lua-alt-getopt
- texlive-lua-alt-getopt

