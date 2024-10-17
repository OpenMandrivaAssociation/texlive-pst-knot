Name:		texlive-pst-knot
Version:	16033
Release:	2
Summary:	PSTricks package for displaying knots
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-knot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-knot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-knot.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
