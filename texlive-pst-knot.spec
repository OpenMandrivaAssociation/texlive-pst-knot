# revision 16033
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-knot
# catalog-date 2009-11-14 08:46:33 +0100
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-pst-knot
Version:	0.2
Release:	4
Summary:	PSTricks package for displaying knots
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-knot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-knot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-knot.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package can produce a fair range of knot shapes, with all
the standard graphics controls one expects.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-knot/pst-psm.pro
%{_texmfdistdir}/tex/generic/pst-knot/pst-knot.tex
%{_texmfdistdir}/tex/latex/pst-knot/pst-knot.sty
%doc %{_texmfdistdir}/doc/generic/pst-knot/Changes
%doc %{_texmfdistdir}/doc/generic/pst-knot/README
%doc %{_texmfdistdir}/doc/generic/pst-knot/pst-knot-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-knot/pst-knot-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 755318
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 719362
- texlive-pst-knot
- texlive-pst-knot
- texlive-pst-knot
- texlive-pst-knot

