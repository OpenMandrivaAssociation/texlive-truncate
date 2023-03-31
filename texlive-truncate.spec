Name:		texlive-truncate
Version:	18921
Release:	2
Summary:	Truncate text to a specified width
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/truncate
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/truncate.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/truncate.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package will by default break at word boundaries, but
package options are offered to permit breaks within words.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/truncate/truncate.sty
%doc %{_texmfdistdir}/doc/latex/truncate/miscdoc.sty
%doc %{_texmfdistdir}/doc/latex/truncate/truncate.pdf
%doc %{_texmfdistdir}/doc/latex/truncate/truncate.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
