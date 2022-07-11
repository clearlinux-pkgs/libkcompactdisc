#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libkcompactdisc
Version  : 22.04.3
Release  : 40
URL      : https://download.kde.org/stable/release-service/22.04.3/src/libkcompactdisc-22.04.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.04.3/src/libkcompactdisc-22.04.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.04.3/src/libkcompactdisc-22.04.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: libkcompactdisc-lib = %{version}-%{release}
Requires: libkcompactdisc-license = %{version}-%{release}
Requires: libkcompactdisc-locales = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : glibc-dev
BuildRequires : phonon-dev
BuildRequires : qtbase-dev mesa-dev

%description
This directory contains the WorkMan library.
libworkman is a multi-plaform CD-Player library for creating various
CD-Player-UIs.

%package dev
Summary: dev components for the libkcompactdisc package.
Group: Development
Requires: libkcompactdisc-lib = %{version}-%{release}
Provides: libkcompactdisc-devel = %{version}-%{release}
Requires: libkcompactdisc = %{version}-%{release}

%description dev
dev components for the libkcompactdisc package.


%package lib
Summary: lib components for the libkcompactdisc package.
Group: Libraries
Requires: libkcompactdisc-license = %{version}-%{release}

%description lib
lib components for the libkcompactdisc package.


%package license
Summary: license components for the libkcompactdisc package.
Group: Default

%description license
license components for the libkcompactdisc package.


%package locales
Summary: locales components for the libkcompactdisc package.
Group: Default

%description locales
locales components for the libkcompactdisc package.


%prep
%setup -q -n libkcompactdisc-22.04.3
cd %{_builddir}/libkcompactdisc-22.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657557647
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1657557647
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkcompactdisc
cp %{_builddir}/libkcompactdisc-22.04.3/COPYING %{buildroot}/usr/share/package-licenses/libkcompactdisc/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/libkcompactdisc-22.04.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/libkcompactdisc/ba8966e2473a9969bdcab3dc82274c817cfd98a1
pushd clr-build
%make_install
popd
%find_lang libkcompactdisc

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KCompactDisc/KCompactDisc
/usr/include/KF5/KCompactDisc/kcompactdisc.h
/usr/include/KF5/KCompactDisc/kcompactdisc_export.h
/usr/include/KF5/kcompactdisc_version.h
/usr/lib64/cmake/KF5CompactDisc/KF5CompactDiscConfig.cmake
/usr/lib64/cmake/KF5CompactDisc/KF5CompactDiscConfigVersion.cmake
/usr/lib64/cmake/KF5CompactDisc/KF5CompactDiscTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5CompactDisc/KF5CompactDiscTargets.cmake
/usr/lib64/libKF5CompactDisc.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5CompactDisc.so.5
/usr/lib64/libKF5CompactDisc.so.5.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkcompactdisc/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/libkcompactdisc/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files locales -f libkcompactdisc.lang
%defattr(-,root,root,-)

