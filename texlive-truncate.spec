# revision 18921
# category Package
# catalog-ctan /macros/latex/contrib/truncate
# catalog-date 2010-06-06 13:50:32 +0200
# catalog-license pd
# catalog-version 3.6
Name:		texlive-truncate
Version:	3.6
Release:	4
Summary:	Truncate text to a specified width
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/truncate
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/truncate.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/truncate.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.6-2
+ Revision: 757138
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.6-1
+ Revision: 719809
- texlive-truncate
- texlive-truncate
- texlive-truncate

