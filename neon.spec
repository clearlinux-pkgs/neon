#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : neon
Version  : 1
Release  : 17
URL      : http://github.com/NervanaSystems/neon/archive/v1.8.2.tar.gz
Source0  : http://github.com/NervanaSystems/neon/archive/v1.8.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: neon-bin
Requires: neon-python
Requires: neon-doc
Requires: Sphinx
Requires: appdirs
Requires: flake8
Requires: h5py
Requires: numpy
Requires: pep8
Requires: posix_ipc
Requires: pylint
Requires: pytest
Requires: pytest-cov
Requires: tqdm
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
# neon
[neon](https://github.com/NervanaSystems/neon) is Intel Nervana's reference deep learning framework committed to [best performance](https://github.com/soumith/convnet-benchmarks) on all hardware. Designed for ease-of-use and extensibility.

%package bin
Summary: bin components for the neon package.
Group: Binaries

%description bin
bin components for the neon package.


%package doc
Summary: doc components for the neon package.
Group: Documentation

%description doc
doc components for the neon package.


%package python
Summary: python components for the neon package.
Group: Default

%description python
python components for the neon package.


%prep
%setup -q -n neon-1.8.2

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487983480
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1487983480
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
## make_install_append content
mkdir -p %{buildroot}/usr/share/doc/neon
cp -a examples  %{buildroot}/usr/share/doc/neon
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/neon
/usr/bin/nvis

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/neon/*

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
