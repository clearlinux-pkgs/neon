#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : neon
Version  : 1.8.1
Release  : 15
URL      : https://github.com/NervanaSystems/neon/archive/v1.8.1.tar.gz
Source0  : https://github.com/NervanaSystems/neon/archive/v1.8.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: neon-bin
Requires: neon-python
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
[neon](https://github.com/NervanaSystems/neon) is Nervana's Python based
Deep Learning framework and achieves the [fastest performance](https://github.com/soumith/convnet-benchmarks) on modern deep neural networks such as AlexNet, VGG and GoogLeNet. Designed for ease-of-use and extensibility.

%package bin
Summary: bin components for the neon package.
Group: Binaries

%description bin
bin components for the neon package.


%package python
Summary: python components for the neon package.
Group: Default

%description python
python components for the neon package.


%prep
%setup -q -n neon-1.8.1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1485014536
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1485014536
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/neon
/usr/bin/nvis

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
