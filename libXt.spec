#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x702353E0F7E48EDB (dickey@invisible-island.net)
#
Name     : libXt
Version  : 1.2.0
Release  : 16
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXt-1.2.0.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXt-1.2.0.tar.bz2
Source1 : http://xorg.freedesktop.org/releases/individual/lib/libXt-1.2.0.tar.bz2.sig
Summary  : X Toolkit Library
Group    : Development/Tools
License  : X11
Requires: libXt-lib = %{version}-%{release}
Requires: libXt-license = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glib-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libxslt-bin
BuildRequires : pkg-config
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
------------------------------------
Documentation for this library can be found in the included man pages; and
the libXt spec from the specs directory of the source, also available at:

%package dev
Summary: dev components for the libXt package.
Group: Development
Requires: libXt-lib = %{version}-%{release}
Provides: libXt-devel = %{version}-%{release}
Requires: libXt = %{version}-%{release}

%description dev
dev components for the libXt package.


%package dev32
Summary: dev32 components for the libXt package.
Group: Default
Requires: libXt-lib32 = %{version}-%{release}
Requires: libXt-dev = %{version}-%{release}

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
Requires: libXt-license = %{version}-%{release}

%description lib
lib components for the libXt package.


%package lib32
Summary: lib32 components for the libXt package.
Group: Default
Requires: libXt-license = %{version}-%{release}

%description lib32
lib32 components for the libXt package.


%package license
Summary: license components for the libXt package.
Group: Default

%description license
license components for the libXt package.


%prep
%setup -q -n libXt-1.2.0
pushd ..
cp -a libXt-1.2.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568868851
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1568868851
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libXt
cp COPYING %{buildroot}/usr/share/package-licenses/libXt/COPYING
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
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
/usr/share/man/man3/MenuPopdown.3
/usr/share/man/man3/MenuPopup.3
/usr/share/man/man3/XtAddActions.3
/usr/share/man/man3/XtAddCallback.3
/usr/share/man/man3/XtAddCallbacks.3
/usr/share/man/man3/XtAddConverter.3
/usr/share/man/man3/XtAddEventHandler.3
/usr/share/man/man3/XtAddExposureToRegion.3
/usr/share/man/man3/XtAddGrab.3
/usr/share/man/man3/XtAddInput.3
/usr/share/man/man3/XtAddRawEventHandler.3
/usr/share/man/man3/XtAddTimeOut.3
/usr/share/man/man3/XtAddWorkProc.3
/usr/share/man/man3/XtAllocateGC.3
/usr/share/man/man3/XtAppAddActionHook.3
/usr/share/man/man3/XtAppAddActions.3
/usr/share/man/man3/XtAppAddBlockHook.3
/usr/share/man/man3/XtAppAddConverter.3
/usr/share/man/man3/XtAppAddInput.3
/usr/share/man/man3/XtAppAddSignal.3
/usr/share/man/man3/XtAppAddTimeOut.3
/usr/share/man/man3/XtAppAddWorkProc.3
/usr/share/man/man3/XtAppCreateShell.3
/usr/share/man/man3/XtAppError.3
/usr/share/man/man3/XtAppErrorMsg.3
/usr/share/man/man3/XtAppGetErrorDatabase.3
/usr/share/man/man3/XtAppGetErrorDatabaseText.3
/usr/share/man/man3/XtAppGetExitFlag.3
/usr/share/man/man3/XtAppGetSelectionTimeout.3
/usr/share/man/man3/XtAppInitialize.3
/usr/share/man/man3/XtAppLock.3
/usr/share/man/man3/XtAppMainLoop.3
/usr/share/man/man3/XtAppNextEvent.3
/usr/share/man/man3/XtAppPeekEvent.3
/usr/share/man/man3/XtAppPending.3
/usr/share/man/man3/XtAppProcessEvent.3
/usr/share/man/man3/XtAppReleaseCacheRefs.3
/usr/share/man/man3/XtAppSetErrorHandler.3
/usr/share/man/man3/XtAppSetErrorMsgHandler.3
/usr/share/man/man3/XtAppSetExitFlag.3
/usr/share/man/man3/XtAppSetFallbackResources.3
/usr/share/man/man3/XtAppSetSelectionTimeout.3
/usr/share/man/man3/XtAppSetTypeConverter.3
/usr/share/man/man3/XtAppSetWarningHandler.3
/usr/share/man/man3/XtAppSetWarningMsgHandler.3
/usr/share/man/man3/XtAppUnlock.3
/usr/share/man/man3/XtAppWarning.3
/usr/share/man/man3/XtAppWarningMsg.3
/usr/share/man/man3/XtAsprintf.3
/usr/share/man/man3/XtAugmentTranslations.3
/usr/share/man/man3/XtBuildEventMask.3
/usr/share/man/man3/XtCallAcceptFocus.3
/usr/share/man/man3/XtCallActionProc.3
/usr/share/man/man3/XtCallCallbackList.3
/usr/share/man/man3/XtCallCallbacks.3
/usr/share/man/man3/XtCallConverter.3
/usr/share/man/man3/XtCallbackExclusive.3
/usr/share/man/man3/XtCallbackNone.3
/usr/share/man/man3/XtCallbackNonexclusive.3
/usr/share/man/man3/XtCallbackPopdown.3
/usr/share/man/man3/XtCalloc.3
/usr/share/man/man3/XtCancelSelectionRequest.3
/usr/share/man/man3/XtChangeManagedSet.3
/usr/share/man/man3/XtCheckSubclass.3
/usr/share/man/man3/XtClass.3
/usr/share/man/man3/XtCloseDisplay.3
/usr/share/man/man3/XtConfigureWidget.3
/usr/share/man/man3/XtConvert.3
/usr/share/man/man3/XtConvertAndStore.3
/usr/share/man/man3/XtConvertCase.3
/usr/share/man/man3/XtCreateApplicationContext.3
/usr/share/man/man3/XtCreateApplicationShell.3
/usr/share/man/man3/XtCreateManagedWidget.3
/usr/share/man/man3/XtCreatePopupShell.3
/usr/share/man/man3/XtCreateSelectionRequest.3
/usr/share/man/man3/XtCreateWidget.3
/usr/share/man/man3/XtCreateWindow.3
/usr/share/man/man3/XtDatabase.3
/usr/share/man/man3/XtDestroyApplicationContext.3
/usr/share/man/man3/XtDestroyWidget.3
/usr/share/man/man3/XtDirectConvert.3
/usr/share/man/man3/XtDisownSelection.3
/usr/share/man/man3/XtDispatchEvent.3
/usr/share/man/man3/XtDispatchEventToWidget.3
/usr/share/man/man3/XtDisplay.3
/usr/share/man/man3/XtDisplayInitialize.3
/usr/share/man/man3/XtDisplayOfObject.3
/usr/share/man/man3/XtDisplayStringConversionWarning.3
/usr/share/man/man3/XtDisplayToApplicationContext.3
/usr/share/man/man3/XtError.3
/usr/share/man/man3/XtErrorMsg.3
/usr/share/man/man3/XtFindFile.3
/usr/share/man/man3/XtFree.3
/usr/share/man/man3/XtGetActionKeysym.3
/usr/share/man/man3/XtGetActionList.3
/usr/share/man/man3/XtGetApplicationNameAndClass.3
/usr/share/man/man3/XtGetApplicationResources.3
/usr/share/man/man3/XtGetClassExtension.3
/usr/share/man/man3/XtGetConstraintResourceList.3
/usr/share/man/man3/XtGetDisplays.3
/usr/share/man/man3/XtGetErrorDatabase.3
/usr/share/man/man3/XtGetErrorDatabaseText.3
/usr/share/man/man3/XtGetGC.3
/usr/share/man/man3/XtGetKeyboardFocusWidget.3
/usr/share/man/man3/XtGetKeysymTable.3
/usr/share/man/man3/XtGetMultiClickTime.3
/usr/share/man/man3/XtGetResourceList.3
/usr/share/man/man3/XtGetSelectionParameters.3
/usr/share/man/man3/XtGetSelectionRequest.3
/usr/share/man/man3/XtGetSelectionTimeout.3
/usr/share/man/man3/XtGetSelectionValue.3
/usr/share/man/man3/XtGetSelectionValueIncremental.3
/usr/share/man/man3/XtGetSelectionValues.3
/usr/share/man/man3/XtGetSelectionValuesIncremental.3
/usr/share/man/man3/XtGetSubresources.3
/usr/share/man/man3/XtGetSubvalues.3
/usr/share/man/man3/XtGetValues.3
/usr/share/man/man3/XtGrabButton.3
/usr/share/man/man3/XtGrabKey.3
/usr/share/man/man3/XtGrabKeyboard.3
/usr/share/man/man3/XtGrabPointer.3
/usr/share/man/man3/XtHasCallbacks.3
/usr/share/man/man3/XtHooksOfDisplay.3
/usr/share/man/man3/XtInitialize.3
/usr/share/man/man3/XtInitializeWidgetClass.3
/usr/share/man/man3/XtInsertEventHandler.3
/usr/share/man/man3/XtInsertEventTypeHandler.3
/usr/share/man/man3/XtInsertRawEventHandler.3
/usr/share/man/man3/XtInstallAccelerators.3
/usr/share/man/man3/XtInstallAllAccelerators.3
/usr/share/man/man3/XtIsApplicationShell.3
/usr/share/man/man3/XtIsComposite.3
/usr/share/man/man3/XtIsConstraint.3
/usr/share/man/man3/XtIsManaged.3
/usr/share/man/man3/XtIsObject.3
/usr/share/man/man3/XtIsOverrideShell.3
/usr/share/man/man3/XtIsRealized.3
/usr/share/man/man3/XtIsRectObj.3
/usr/share/man/man3/XtIsSensitive.3
/usr/share/man/man3/XtIsSessionShell.3
/usr/share/man/man3/XtIsShell.3
/usr/share/man/man3/XtIsSubclass.3
/usr/share/man/man3/XtIsTopLevelShell.3
/usr/share/man/man3/XtIsTransientShell.3
/usr/share/man/man3/XtIsVendorShell.3
/usr/share/man/man3/XtIsWMShell.3
/usr/share/man/man3/XtIsWidget.3
/usr/share/man/man3/XtKeysymToKeycodeList.3
/usr/share/man/man3/XtLastEventProcessed.3
/usr/share/man/man3/XtLastTimestampProcessed.3
/usr/share/man/man3/XtMainLoop.3
/usr/share/man/man3/XtMakeGeometryRequest.3
/usr/share/man/man3/XtMakeResizeRequest.3
/usr/share/man/man3/XtMalloc.3
/usr/share/man/man3/XtManageChild.3
/usr/share/man/man3/XtManageChildren.3
/usr/share/man/man3/XtMapWidget.3
/usr/share/man/man3/XtMergeArgLists.3
/usr/share/man/man3/XtMoveWidget.3
/usr/share/man/man3/XtName.3
/usr/share/man/man3/XtNameToWidget.3
/usr/share/man/man3/XtNew.3
/usr/share/man/man3/XtNewString.3
/usr/share/man/man3/XtNextEvent.3
/usr/share/man/man3/XtNoticeSignal.3
/usr/share/man/man3/XtNumber.3
/usr/share/man/man3/XtOffset.3
/usr/share/man/man3/XtOffsetOf.3
/usr/share/man/man3/XtOpenApplication.3
/usr/share/man/man3/XtOpenDisplay.3
/usr/share/man/man3/XtOverrideTranslations.3
/usr/share/man/man3/XtOwnSelection.3
/usr/share/man/man3/XtOwnSelectionIncremental.3
/usr/share/man/man3/XtParent.3
/usr/share/man/man3/XtParseAcceleratorTable.3
/usr/share/man/man3/XtParseTranslationTable.3
/usr/share/man/man3/XtPeekEvent.3
/usr/share/man/man3/XtPending.3
/usr/share/man/man3/XtPopdown.3
/usr/share/man/man3/XtPopup.3
/usr/share/man/man3/XtPopupSpringLoaded.3
/usr/share/man/man3/XtProcessEvent.3
/usr/share/man/man3/XtProcessLock.3
/usr/share/man/man3/XtProcessUnlock.3
/usr/share/man/man3/XtQueryGeometry.3
/usr/share/man/man3/XtRealizeWidget.3
/usr/share/man/man3/XtRealloc.3
/usr/share/man/man3/XtRegisterCaseConverter.3
/usr/share/man/man3/XtRegisterDrawable.3
/usr/share/man/man3/XtRegisterExtensionSelector.3
/usr/share/man/man3/XtRegisterGrabAction.3
/usr/share/man/man3/XtReleaseGC.3
/usr/share/man/man3/XtReleasePropertyAtom.3
/usr/share/man/man3/XtRemoveActionHook.3
/usr/share/man/man3/XtRemoveAllCallbacks.3
/usr/share/man/man3/XtRemoveBlockHook.3
/usr/share/man/man3/XtRemoveCallback.3
/usr/share/man/man3/XtRemoveCallbacks.3
/usr/share/man/man3/XtRemoveEventHandler.3
/usr/share/man/man3/XtRemoveEventTypeHandler.3
/usr/share/man/man3/XtRemoveGrab.3
/usr/share/man/man3/XtRemoveInput.3
/usr/share/man/man3/XtRemoveRawEventHandler.3
/usr/share/man/man3/XtRemoveSignal.3
/usr/share/man/man3/XtRemoveTimeOut.3
/usr/share/man/man3/XtRemoveWorkProc.3
/usr/share/man/man3/XtReservePropertyAtom.3
/usr/share/man/man3/XtResizeWidget.3
/usr/share/man/man3/XtResolvePathname.3
/usr/share/man/man3/XtScreen.3
/usr/share/man/man3/XtScreenDatabase.3
/usr/share/man/man3/XtScreenOfObject.3
/usr/share/man/man3/XtSendSelectionRequest.3
/usr/share/man/man3/XtSessionGetToken.3
/usr/share/man/man3/XtSessionReturnToken.3
/usr/share/man/man3/XtSetArg.3
/usr/share/man/man3/XtSetErrorHandler.3
/usr/share/man/man3/XtSetErrorMsgHandler.3
/usr/share/man/man3/XtSetEventDispatcher.3
/usr/share/man/man3/XtSetKeyTranslator.3
/usr/share/man/man3/XtSetKeyboardFocus.3
/usr/share/man/man3/XtSetLanguageProc.3
/usr/share/man/man3/XtSetMappedWhenManaged.3
/usr/share/man/man3/XtSetMultiClickTime.3
/usr/share/man/man3/XtSetSelectionParameters.3
/usr/share/man/man3/XtSetSelectionTimeout.3
/usr/share/man/man3/XtSetSensitive.3
/usr/share/man/man3/XtSetSubvalues.3
/usr/share/man/man3/XtSetTypeConverter.3
/usr/share/man/man3/XtSetValues.3
/usr/share/man/man3/XtSetWMColormapWindows.3
/usr/share/man/man3/XtSetWarningHandler.3
/usr/share/man/man3/XtSetWarningMsgHandler.3
/usr/share/man/man3/XtStringConversionWarning.3
/usr/share/man/man3/XtSuperclass.3
/usr/share/man/man3/XtToolkitInitialize.3
/usr/share/man/man3/XtToolkitThreadInitialize.3
/usr/share/man/man3/XtTranslateCoords.3
/usr/share/man/man3/XtTranslateKeycode.3
/usr/share/man/man3/XtUngrabButton.3
/usr/share/man/man3/XtUngrabKey.3
/usr/share/man/man3/XtUngrabKeyboard.3
/usr/share/man/man3/XtUngrabPointer.3
/usr/share/man/man3/XtUninstallTranslations.3
/usr/share/man/man3/XtUnmanageChild.3
/usr/share/man/man3/XtUnmanageChildren.3
/usr/share/man/man3/XtUnmapWidget.3
/usr/share/man/man3/XtUnrealizeWidget.3
/usr/share/man/man3/XtUnregisterDrawable.3
/usr/share/man/man3/XtVaAppCreateShell.3
/usr/share/man/man3/XtVaAppInitialize.3
/usr/share/man/man3/XtVaCreateArgsList.3
/usr/share/man/man3/XtVaCreateManagedWidget.3
/usr/share/man/man3/XtVaCreatePopupShell.3
/usr/share/man/man3/XtVaCreateWidget.3
/usr/share/man/man3/XtVaGetApplicationResources.3
/usr/share/man/man3/XtVaGetSubresources.3
/usr/share/man/man3/XtVaGetSubvalues.3
/usr/share/man/man3/XtVaGetValues.3
/usr/share/man/man3/XtVaOpenApplication.3
/usr/share/man/man3/XtVaSetSubvalues.3
/usr/share/man/man3/XtVaSetValues.3
/usr/share/man/man3/XtWarning.3
/usr/share/man/man3/XtWarningMsg.3
/usr/share/man/man3/XtWidgetToApplicationContext.3
/usr/share/man/man3/XtWindow.3
/usr/share/man/man3/XtWindowOfObject.3
/usr/share/man/man3/XtWindowToWidget.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libXt.so
/usr/lib32/pkgconfig/32xt.pc
/usr/lib32/pkgconfig/xt.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libXt/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libXt.so.6
/usr/lib64/libXt.so.6.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libXt.so.6
/usr/lib32/libXt.so.6.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libXt/COPYING
