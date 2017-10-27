#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : neon
Version  : 2.3.0
Release  : 28
URL      : https://github.com/NervanaSystems/neon/archive/v2.3.0.tar.gz
Source0  : https://github.com/NervanaSystems/neon/archive/v2.3.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: neon-bin
Requires: neon-python3
Requires: neon-doc
Requires: neon-python
Requires: Sphinx
Requires: appdirs
Requires: cffi
Requires: flake8
Requires: funcsigs
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
Requires: neon-python3

%description python
python components for the neon package.


%package python3
Summary: python3 components for the neon package.
Group: Default
Requires: python3-core

%description python3
python3 components for the neon package.


%prep
%setup -q -n neon-2.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1509133160
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
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

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
