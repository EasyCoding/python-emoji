%global appname emoji

%global appsum Emoji library for Python
%global appdesc Full featured simple emoji library for Python

Name: python-%{appname}
Version: 0.5.1
Release: 1%{?dist}
Summary: %{appsum}

License: BSD
URL: https://pypi.python.org/pypi/%{appname}
Source0: %{pypi_source %{appname}}
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3dist(nose)
BuildRequires: python3dist(coverage)

%description
%{appdesc}.

%package -n python3-%{appname}
Summary: %{appsum}
%{?python_provide:%python_provide python3-%{appname}}

%description -n python3-%{appname}
%{appdesc}.

%prep
%autosetup -n %{appname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{appname}
%license LICENSE.txt
%doc README.rst CHANGES.md
%{python3_sitelib}/%{appname}
%{python3_sitelib}/%{appname}-*.egg-info

%changelog
* Thu Sep 20 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.1-1
- Initial SPEC release.
