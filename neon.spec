#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : neon
Version  : 2.6.0
Release  : 60
URL      : https://github.com/NervanaSystems/neon/archive/v2.6.0.tar.gz
Source0  : https://github.com/NervanaSystems/neon/archive/v2.6.0.tar.gz
Summary  : HTTP and WebDAV client library with a C interface
Group    : Development/Tools
License  : Apache-2.0
Requires: neon-bin = %{version}-%{release}
Requires: neon-license = %{version}-%{release}
Requires: neon-python = %{version}-%{release}
Requires: neon-python3 = %{version}-%{release}
Requires: Pillow
Requires: PyYAML
Requires: appdirs
Requires: cffi
Requires: h5py
Requires: numpy
Requires: pep8
Requires: posix_ipc
Requires: pylint
Requires: tqdm
BuildRequires : Pillow
BuildRequires : PyYAML
BuildRequires : appdirs
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : h5py
BuildRequires : numpy
BuildRequires : pep8
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pylint
BuildRequires : pytest
BuildRequires : tox
BuildRequires : tqdm
BuildRequires : virtualenv
Patch1: Fix-pip3-check-issue.patch
Patch2: Bugfix-NeonArgParse.patch

%description
###Model
This is a neural machine translation model based on
[Sutskever et al. 2014](http://arxiv.org/pdf/1409.3215v3.pdf).
The model uses a subset of the dataset used in the paper, which is a tokenized, selected
subset of the WMT14 dataset available from
[Schwenk 2013](http://www-lium.univ-lemans.fr/~schwenk/cslm_joint_paper/)

%package bin
Summary: bin components for the neon package.
Group: Binaries
Requires: neon-license = %{version}-%{release}

%description bin
bin components for the neon package.


%package doc
Summary: doc components for the neon package.
Group: Documentation

%description doc
doc components for the neon package.


%package license
Summary: license components for the neon package.
Group: Default

%description license
license components for the neon package.


%package python
Summary: python components for the neon package.
Group: Default
Requires: neon-python3 = %{version}-%{release}

%description python
python components for the neon package.


%package python3
Summary: python3 components for the neon package.
Group: Default
Requires: python3-core

%description python3
python3 components for the neon package.


%prep
%setup -q -n neon-2.6.0
cd %{_builddir}/neon-2.6.0
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583185942
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
mkdir -p %{buildroot}/usr/share/package-licenses/neon
cp %{_builddir}/neon-2.6.0/LICENSE %{buildroot}/usr/share/package-licenses/neon/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/neon-2.6.0/examples/skip-thought/NOTICE %{buildroot}/usr/share/package-licenses/neon/3132ab1954c386e5f42fad018bd2c1d5e49a8d67
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
mkdir -p %{buildroot}/usr/share/doc/neon
cp -a examples  %{buildroot}/usr/share/doc/neon

## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/neon
/usr/bin/nvis

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/neon/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/neon/3132ab1954c386e5f42fad018bd2c1d5e49a8d67
/usr/share/package-licenses/neon/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
