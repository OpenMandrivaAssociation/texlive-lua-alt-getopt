%global tl_name lua-alt-getopt
%global tl_revision 78415

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7.0
Release:	%{tl_revision}.1
Summary:	Process application arguments the same way as getopt_long
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/lualibs/lua-alt-getopt
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-alt-getopt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-alt-getopt.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
lua_altgetopt is a MIT-licensed module for Lua, for processing
application arguments in the same way as BSD/GNU getopt_long(3)
functions do. This module is made available for Lua script writers to
have consistent command line parsing routines.

