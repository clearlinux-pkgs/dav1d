#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
# Source0 file verified with key 0x7180713BE58D1ADC
#
Name     : dav1d
Version  : 1.2.0
Release  : 25
URL      : https://downloads.videolan.org/pub/videolan/dav1d/1.2.0/dav1d-1.2.0.tar.xz
Source0  : https://downloads.videolan.org/pub/videolan/dav1d/1.2.0/dav1d-1.2.0.tar.xz
Source1  : https://downloads.videolan.org/pub/videolan/dav1d/1.2.0/dav1d-1.2.0.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: dav1d-bin = %{version}-%{release}
Requires: dav1d-lib = %{version}-%{release}
Requires: dav1d-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : nasm-bin
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
![dav1d logo](doc/dav1d_logo.png)
# dav1d
**dav1d** is an **AV1** cross-platform **d**ecoder, open-source, and focused on speed and correctness.

%package bin
Summary: bin components for the dav1d package.
Group: Binaries
Requires: dav1d-license = %{version}-%{release}

%description bin
bin components for the dav1d package.


%package dev
Summary: dev components for the dav1d package.
Group: Development
Requires: dav1d-lib = %{version}-%{release}
Requires: dav1d-bin = %{version}-%{release}
Provides: dav1d-devel = %{version}-%{release}
Requires: dav1d = %{version}-%{release}

%description dev
dev components for the dav1d package.


%package lib
Summary: lib components for the dav1d package.
Group: Libraries
Requires: dav1d-license = %{version}-%{release}

%description lib
lib components for the dav1d package.


%package license
Summary: license components for the dav1d package.
Group: Default

%description license
license components for the dav1d package.


%prep
%setup -q -n dav1d-1.2.0
cd %{_builddir}/dav1d-1.2.0
pushd ..
cp -a dav1d-1.2.0 buildavx2
popd
pushd ..
cp -a dav1d-1.2.0 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685494415
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2
CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -Wl,-z,x86-64-v4 -O3 -mprefer-vector-width=512" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -Wl,-z,x86-64-v4 -mprefer-vector-width=512" LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx512
ninja -v -C builddiravx512

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/dav1d
cp %{_builddir}/dav1d-%{version}/COPYING %{buildroot}/usr/share/package-licenses/dav1d/4f6bb845e36328fa89de127c56773dbfd9c90042 || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot}-v4 ninja -C builddiravx512 install
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/dav1d
/V4/usr/bin/dav1d
/usr/bin/dav1d

%files dev
%defattr(-,root,root,-)
/usr/include/dav1d/common.h
/usr/include/dav1d/data.h
/usr/include/dav1d/dav1d.h
/usr/include/dav1d/headers.h
/usr/include/dav1d/picture.h
/usr/include/dav1d/version.h
/usr/lib64/libdav1d.so
/usr/lib64/pkgconfig/dav1d.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libdav1d.so.6.9.0
/V4/usr/lib64/libdav1d.so.6.9.0
/usr/lib64/libdav1d.so.6
/usr/lib64/libdav1d.so.6.9.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dav1d/4f6bb845e36328fa89de127c56773dbfd9c90042
