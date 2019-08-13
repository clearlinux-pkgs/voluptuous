#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : voluptuous
Version  : 0.11.7
Release  : 25
URL      : https://files.pythonhosted.org/packages/24/3b/fe531688c0d9e057fccc0bc9430c0a3d4b90e0d2f015326e659c2944e328/voluptuous-0.11.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/24/3b/fe531688c0d9e057fccc0bc9430c0a3d4b90e0d2f015326e659c2944e328/voluptuous-0.11.7.tar.gz
Summary  : # Voluptuous is a Python data validation library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: voluptuous-license = %{version}-%{release}
Requires: voluptuous-python = %{version}-%{release}
Requires: voluptuous-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : setuptools-python

%description
# Voluptuous is a Python data validation library
[![Build Status](https://travis-ci.org/alecthomas/voluptuous.svg)](https://travis-ci.org/alecthomas/voluptuous)
[![Coverage Status](https://coveralls.io/repos/github/alecthomas/voluptuous/badge.svg?branch=master)](https://coveralls.io/github/alecthomas/voluptuous?branch=master) [![Gitter chat](https://badges.gitter.im/alecthomas.svg)](https://gitter.im/alecthomas/Lobby)

%package license
Summary: license components for the voluptuous package.
Group: Default

%description license
license components for the voluptuous package.


%package python
Summary: python components for the voluptuous package.
Group: Default
Requires: voluptuous-python3 = %{version}-%{release}

%description python
python components for the voluptuous package.


%package python3
Summary: python3 components for the voluptuous package.
Group: Default
Requires: python3-core

%description python3
python3 components for the voluptuous package.


%prep
%setup -q -n voluptuous-0.11.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565734756
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/voluptuous
cp COPYING %{buildroot}/usr/share/package-licenses/voluptuous/COPYING
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/voluptuous/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
