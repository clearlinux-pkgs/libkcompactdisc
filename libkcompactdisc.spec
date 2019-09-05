#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : libkcompactdisc
Version  : 19.08.1
Release  : 11
URL      : https://download.kde.org/stable/applications/19.08.1/src/libkcompactdisc-19.08.1.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.1/src/libkcompactdisc-19.08.1.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.1/src/libkcompactdisc-19.08.1.tar.xz.sig
Summary  : A library for interfacing with CDs
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: libkcompactdisc-lib = %{version}-%{release}
Requires: libkcompactdisc-license = %{version}-%{release}
Requires: libkcompactdisc-locales = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
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
%setup -q -n libkcompactdisc-19.08.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567714358
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1567714358
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkcompactdisc
cp COPYING %{buildroot}/usr/share/package-licenses/libkcompactdisc/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/libkcompactdisc/COPYING.LIB
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
/usr/lib64/qt5/mkspecs/modules/qt_KCompactDisc.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5CompactDisc.so.5
/usr/lib64/libKF5CompactDisc.so.5.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkcompactdisc/COPYING
/usr/share/package-licenses/libkcompactdisc/COPYING.LIB

%files locales -f libkcompactdisc.lang
%defattr(-,root,root,-)

