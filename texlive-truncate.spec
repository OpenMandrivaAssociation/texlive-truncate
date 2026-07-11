%global tl_name truncate
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.6
Release:	%{tl_revision}.1
Summary:	Truncate text to a specified width
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/truncate
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/truncate.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/truncate.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package will by default break at word boundaries, but package
options are offered to permit breaks within words.

