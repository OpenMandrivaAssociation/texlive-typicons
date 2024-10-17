Name:		texlive-typicons
Version:	37623
Release:	2
Summary:	Font containing a set of web-related icons
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/typicons
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typicons.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typicons.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package grants access to 336 web-related icons provided by
the included "Typicons" free font, designed by Stephen
Hutchings and released under the SIL Open Font License. See
http://www.typicons.com for more details about the font itself.
This package requires the fontspec package and either the
Xe(La)TeX or Lua(La)TeX engine to load the included ttf font.
Once the package is loaded, icons can be accessed through the
general \ticon command, which takes as argument the name of the
desired icon, or through direct commands specific to each icon.
The full list of icon designs, names and direct commands is
showcased in the manual.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/typicons
%{_texmfdistdir}/fonts/truetype/public/typicons
%doc %{_texmfdistdir}/doc/fonts/typicons

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
