#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libXt
Version  : 1.1.5
Release  : 12
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXt-1.1.5.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXt-1.1.5.tar.bz2
Summary  : X Toolkit Library
Group    : Development/Tools
License  : ICU
Requires: libXt-lib
Requires: libXt-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glib-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(32ice)
BuildRequires : pkgconfig(32kbproto)
BuildRequires : pkgconfig(32sm)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(32xproto)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(kbproto)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
BuildRequires : xmlto

%description
libXt - X Toolkit Intrinsics library
Documentation for this library can be found in the included man pages;
the libXt spec from the specs directory of the source, also available at:

%package dev
Summary: dev components for the libXt package.
Group: Development
Requires: libXt-lib
Provides: libXt-devel

%description dev
dev components for the libXt package.


%package dev32
Summary: dev32 components for the libXt package.
Group: Default
Requires: libXt-lib32

%description dev32
dev32 components for the libXt package.


%package doc
Summary: doc components for the libXt package.
Group: Documentation

%description doc
doc components for the libXt package.


%package lib
Summary: lib components for the libXt package.
Group: Libraries

%description lib
lib components for the libXt package.


%package lib32
Summary: lib32 components for the libXt package.
Group: Default

%description lib32
lib32 components for the libXt package.


%prep
%setup -q -n libXt-1.1.5
pushd ..
cp -a libXt-1.1.5 build32
popd

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/CallbackI.h
/usr/include/X11/Composite.h
/usr/include/X11/CompositeP.h
/usr/include/X11/ConstrainP.h
/usr/include/X11/Constraint.h
/usr/include/X11/ConvertI.h
/usr/include/X11/Core.h
/usr/include/X11/CoreP.h
/usr/include/X11/CreateI.h
/usr/include/X11/EventI.h
/usr/include/X11/HookObjI.h
/usr/include/X11/InitialI.h
/usr/include/X11/Intrinsic.h
/usr/include/X11/IntrinsicI.h
/usr/include/X11/IntrinsicP.h
/usr/include/X11/Object.h
/usr/include/X11/ObjectP.h
/usr/include/X11/PassivGraI.h
/usr/include/X11/RectObj.h
/usr/include/X11/RectObjP.h
/usr/include/X11/ResConfigP.h
/usr/include/X11/ResourceI.h
/usr/include/X11/SelectionI.h
/usr/include/X11/Shell.h
/usr/include/X11/ShellI.h
/usr/include/X11/ShellP.h
/usr/include/X11/StringDefs.h
/usr/include/X11/ThreadsI.h
/usr/include/X11/TranslateI.h
/usr/include/X11/VarargsI.h
/usr/include/X11/Vendor.h
/usr/include/X11/VendorP.h
/usr/include/X11/Xtos.h
/usr/lib64/libXt.so
/usr/lib64/pkgconfig/xt.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libXt.so
/usr/lib32/pkgconfig/32xt.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libXt/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libXt.so.6
/usr/lib64/libXt.so.6.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libXt.so.6
/usr/lib32/libXt.so.6.0.0
