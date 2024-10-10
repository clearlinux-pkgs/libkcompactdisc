#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libkcompactdisc
Version  : 24.08.2
Release  : 73
URL      : https://download.kde.org/stable/release-service/24.08.2/src/libkcompactdisc-24.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.2/src/libkcompactdisc-24.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.2/src/libkcompactdisc-24.08.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
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
BuildRequires : gnupg
BuildRequires : phonon-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n libkcompactdisc-24.08.2
cd %{_builddir}/libkcompactdisc-24.08.2
pushd ..
cp -a libkcompactdisc-24.08.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728578590
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1728578590
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkcompactdisc
cp %{_builddir}/libkcompactdisc-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libkcompactdisc/7c203dee3a03037da436df03c4b25b659c073976 || :
cp %{_builddir}/libkcompactdisc-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/libkcompactdisc/ba8966e2473a9969bdcab3dc82274c817cfd98a1 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libkcompactdisc
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KCompactDisc6/KCompactDisc
/usr/include/KCompactDisc6/kcompactdisc.h
/usr/include/KCompactDisc6/kcompactdisc_export.h
/usr/include/KCompactDisc6/kcompactdisc_version.h
/usr/lib64/cmake/KCompactDisc6/KCompactDisc6Config.cmake
/usr/lib64/cmake/KCompactDisc6/KCompactDisc6ConfigVersion.cmake
/usr/lib64/cmake/KCompactDisc6/KCompactDisc6Targets-relwithdebinfo.cmake
/usr/lib64/cmake/KCompactDisc6/KCompactDisc6Targets.cmake
/usr/lib64/libKCompactDisc6.so
/usr/lib64/qt6/mkspecs/modules/qt_KCompactDisc.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKCompactDisc6.so.5.0.0
/usr/lib64/libKCompactDisc6.so.5
/usr/lib64/libKCompactDisc6.so.5.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkcompactdisc/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/libkcompactdisc/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files locales -f libkcompactdisc.lang
%defattr(-,root,root,-)

