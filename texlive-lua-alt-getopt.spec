Name:		texlive-lua-alt-getopt
Version:	56414
Release:	1
Summary:	Process application arguments the same way as getopt_long
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/lua/lua-alt-getopt
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-alt-getopt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-alt-getopt.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts doc %{buildroot}%{_texmfdistdir}
