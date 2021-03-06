Summary:	Python shell
Summary(pl.UTF-8):	Powłoka Pythona
Name:		dreampie
Version:	1.1
Release:	1
License:	GPL v3+
Group:		Development/Languages/Python
Source0:	http://launchpad.net/dreampie/trunk/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	57ced153616069ca6c3c7d37bb30633a
URL:		http://dreampie.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-gtksourceview2
Requires:	python-modules
Requires:	python-pygtk-glade
Requires:	python-pygtk-gtk
Requires:	python-pygtk-pango
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is DreamPie - The Python shell you've always dreamed about!

%description -l pl.UTF-8
Powłoka Pythona z Twoich snów!

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{py_sitescriptdir}/dreampielib
%{_datadir}/%{name}/*
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/*
%{_pixmapsdir}/%{name}*
%{py_sitescriptdir}/dreampielib/*/*.py[co]
%{py_sitescriptdir}/dreampielib/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/dreampie-*.egg-info
%endif
