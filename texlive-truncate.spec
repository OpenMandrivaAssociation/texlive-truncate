# revision 18921
# category Package
# catalog-ctan /macros/latex/contrib/truncate
# catalog-date 2010-06-06 13:50:32 +0200
# catalog-license pd
# catalog-version 3.6
Name:		texlive-truncate
Version:	3.6
Release:	1
Summary:	Truncate text to a specified width
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/truncate
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/truncate.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/truncate.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package will by default break at word boundaries, but
package options are offered to permit breaks within words.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/truncate/truncate.sty
%doc %{_texmfdistdir}/doc/latex/truncate/miscdoc.sty
%doc %{_texmfdistdir}/doc/latex/truncate/truncate.pdf
%doc %{_texmfdistdir}/doc/latex/truncate/truncate.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
