%define	name	gtk-sharp2
%define oname gtk-sharp
%define release %mkrel 1
%define mono 1.0.2
%define monodir %_prefix/lib/mono

Summary:	C# language binding for the gtk+ toolkit
Name:		%name
Version:	2.12.5
Release:	%release
License:	LGPLv2
Group:		System/Libraries
URL:		http://gtk-sharp.sourceforge.net/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gtk-sharp/%oname-%version.tar.bz2
BuildRoot:	%_tmppath/%name-buildroot
Requires: glib-sharp2 = %version
BuildRequires:	mono-devel >= %mono
BuildRequires:	libglade2.0-devel
BuildRequires:	libxslt-devel
BuildRequires:	monodoc

%description
Gtk-sharp is a C# language binding for the  gtk+ toolkit.


%package devel
Summary: C# code generation tools for %name
Group: Development/Other

%description devel
This contains the code generation tools of gtk-sharp. It is needed for building
C# wrappers for GObject APIs.

%package -n glib-sharp2
Summary:        C# binding for glib
Group:          System/Libraries
Requires:       mono >= %mono

%description -n glib-sharp2
Glib-sharp is a C# language binding for glib.

%package -n glade-sharp2
Summary:        C# binding for glade
Group:          System/Libraries
Requires: %name = %version

%description -n glade-sharp2
Glade-sharp is a C# language binding for glade.


%package doc
Summary:	Documentation for gtk-sharp
Group:		Development/Other
Requires(post): mono-tools >= 1.1.9
Requires(postun): mono-tools >= 1.1.9
Conflicts: monodoc < 1.1.9

%description doc
Gtk-sharp is a C# language binding for the  gtk+ toolkit.
This package provides documentation for gtk-sharp. 

%prep
rm -rf %buildroot

%setup -q -n %oname-%version

%build
%configure2_5x
make

%install
rm -rf %buildroot
%makeinstall

rm -rf %buildroot%_libdir/lib*a

%clean
rm -rf %buildroot

%post doc
%_bindir/monodoc --make-index > /dev/null

%postun doc
if [ "$1" = "0" -a -x %_bindir/monodoc ]; then %_bindir/monodoc --make-index > /dev/null
fi


%files
%defattr(-,root,root)
%monodir/gac/*atk-sharp
%monodir/gac/*gdk-sharp
%monodir/gac/*gtk-dotnet
%monodir/gac/*gtk-sharp
%monodir/gac/*pango-sharp
%monodir/%oname-2.0/*atk-sharp.dll*
%monodir/%oname-2.0/*gdk-sharp.dll*
%monodir/%oname-2.0/*gtk-sharp.dll*
%monodir/%oname-2.0/*gtk-dotnet.dll*
%monodir/%oname-2.0/*pango-sharp.dll*
%_libdir/libatksharpglue-2.so
%_libdir/libgdksharpglue-2.so
%_libdir/libgtksharpglue-2.so
%_libdir/libpangosharpglue-2.so
%_libdir/pkgconfig/gtk-sharp-2.0.pc
%_libdir/pkgconfig/gtk-dotnet-2.0.pc

%files -n glib-sharp2
%defattr(-,root,root)
%monodir/gac/*glib-sharp
%monodir/%oname-2.0/*glib-sharp.dll*
%_libdir/libglibsharpglue-2.so
%_libdir/pkgconfig/glib-sharp-2.0.pc

%files -n glade-sharp2
%defattr(-,root,root)
%monodir/gac/*glade-sharp
%monodir/%oname-2.0/*glade-sharp.dll*
%_libdir/pkgconfig/glade-sharp-2.0.pc
%_libdir/libgladesharpglue-2.so

%files doc
%defattr(-,root,root)
%doc ChangeLog README README.generator
#*[^makefile|README]
%doc sample
%_prefix/lib/monodoc/sources/gtk*

%files devel
%defattr(-,root,root)
%_bindir/*
%_datadir/gapi-2.0/
%_libdir/pkgconfig/gapi-2.0.pc
%_prefix/lib/%oname-2.0/

