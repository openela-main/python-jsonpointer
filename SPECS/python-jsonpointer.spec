%global pypi_name jsonpointer
%global github_name python-json-pointer

%if 0%{?fedora} || 0%{?rhel} > 7
# Enable python3 build by default
%bcond_without python3
%else
%bcond_with python3
%endif

%if 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-%{pypi_name}
Version:        1.10
Release:        11%{?dist}
Summary:        Resolve JSON Pointers in Python

License:        BSD
URL:            https://github.com/stefankoegl/%{github_name}
Source0:        https://pypi.io/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch


%description
Library to resolve JSON Pointers according to RFC 6901.

%if %{with python2}
%package -n python2-%{pypi_name}
Summary:        Resolve JSON Pointers in Python

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Library to resolve JSON Pointers according to RFC 6901.
%endif # with python2

%if %{with python3}
%package -n python3-%{pypi_name}
Summary:        Resolve JSON Pointers in Python

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Library to resolve JSON Pointers according to RFC 6901.
%endif # with python3

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py2_build
%endif # with python2
%if %{with python3}
LC_ALL=en_US.UTF-8 %py3_build
%endif # with python3

%install
%if %{with python2}
%py2_install
mv %{buildroot}%{_bindir}/jsonpointer %{buildroot}%{_bindir}/jsonpointer-%{python2_version}
ln -s ./jsonpointer-%{python2_version} %{buildroot}%{_bindir}/jsonpointer-2
%if %{without python3}
ln -s ./jsonpointer-%{python2_version} %{buildroot}%{_bindir}/jsonpointer
%endif # without python3
%endif # with python2

%if %{with python3}
LC_ALL=en_US.UTF-8 %py3_install
mv %{buildroot}%{_bindir}/jsonpointer %{buildroot}%{_bindir}/jsonpointer-%{python3_version}
ln -s ./jsonpointer-%{python3_version} %{buildroot}%{_bindir}/jsonpointer-3
ln -s ./jsonpointer-%{python3_version} %{buildroot}%{_bindir}/jsonpointer
%endif # with python3


%check
%if %{with python3}
%{__python3} tests.py
%endif # with python3
%if %{with python2}
%{__python2} tests.py
%endif # with python2

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.md AUTHORS
%license COPYING
%if %{without python3}
%{_bindir}/jsonpointer
%endif # without python3
%{_bindir}/jsonpointer-2*
%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif # with python2

%if %{with python3}
%files -n python3-%{pypi_name}
%doc README.md AUTHORS
%license COPYING
%{_bindir}/jsonpointer
%{_bindir}/jsonpointer-3*
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py*
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif # with python3

%changelog
* Tue Apr 03 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.10-11
- Conditionalize the Python 2 subpackage and don't build it on EL > 7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.10-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 1.10-8
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.10-5
- Rebuild for Python 3.6

* Mon Sep  5 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.10-4
- Update to latest python guidelines

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 19 2015 Alan Pevec <alan.pevec@redhat.com> 1.10-1
- Update to 1.10

* Sat Nov 14 2015 Tonet Jallo <tonet666p@gmail.com> - 1.9-4
- Moved a line from files section to python3 files section

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Aug 07 2015 Alan Pevec <apevec@gmail.com> - 1.9-2
- Update to 1.9

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 31 2014 Tom Callaway <spot@fedoraproject.org> - 1.0-6
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Feb  5 2014 Thomas Spura <tomspur@fedoraproject.org> - 1.0-3
- add python3 subpackage (#1061622)

* Thu Sep 05 2013 Alan Pevec <apevec@gmail.com> - 1.0-2
- add AUTHORS to docs

* Mon Jul 01 2013 Alan Pevec <apevec@gmail.com> - 1.0-1
- Initial package.
