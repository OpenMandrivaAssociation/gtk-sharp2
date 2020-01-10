%define oname	gtk-sharp
%define monodir	%{_prefix}/lib/mono

Summary:	C sharp language binding for the gtk+ toolkit
Name:		gtk-sharp2
Version:	2.12.45
Release:	1
License:	LGPLv2
Group:		System/Libraries
Url:		http://gtk-sharp.sourceforge.net/
Source0:	http://origin-download.mono-project.com/sources/gtk-sharp212/%{oname}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

BuildRequires:	monodoc
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(mono)
Requires:	glib-sharp2 = %{version}

%description
Gtk-sharp is a C sharp language binding for the  gtk+ toolkit.

%package 2.4
Summary:	C sharp language binding for the gtk+-2.4 toolkit
Group:		System/Libraries
Requires:	gtk-sharp2 = %{version}
Conflicts:	gtk-sharp2 < 2.12.10-3

%description 2.4
Gtk-sharp is a C sharp language binding for the gtk+ toolkit.

%package 2.6
Summary:	C sharp language binding for the gtk+-2.6 toolkit
Group:		System/Libraries
Requires:	gtk-sharp2 = %{version}
Conflicts:	gtk-sharp2 < 2.12.10-3

%description 2.6
Gtk-sharp is a C sharp language binding for the gtk+ toolkit.

%package 2.8
Summary:	C sharp language binding for the gtk+-2.8 toolkit
Group:		System/Libraries
Requires:	gtk-sharp2 = %{version}
Conflicts:	gtk-sharp2 < 2.12.10-3

%description 2.8
Gtk-sharp is a C sharp language binding for the gtk+ toolkit.

%package 2.10
Summary:	C sharp language binding for the gtk+-2.10 toolkit
Group:		System/Libraries
Requires:	gtk-sharp2 = %{version}
Conflicts:	gtk-sharp2 < 2.12.10-3

%description 2.10
Gtk-sharp is a C sharp language binding for the gtk+ toolkit.

%package devel
Summary:	C sharp code generation tools for %{name}
Group:		Development/Other

%description devel
This contains the code generation tools of gtk-sharp. It is needed for building
C sharp wrappers for GObject APIs.

%package -n glib-sharp2
Summary:	C sharp binding for glib
Group:		System/Libraries
Requires:	mono

%description -n glib-sharp2
Glib-sharp is a C sharp language binding for glib.

%package -n glib-sharp2-2.4
Summary:	C sharp binding for glib-2.4
Group:		System/Libraries
Requires:	glib-sharp2 = %{version}
Conflicts:	glib-sharp2 < 2.12.10-3

%description -n glib-sharp2-2.4
Glib-sharp is a C sharp language binding for glib.

%package -n glib-sharp2-2.6
Summary:	C sharp binding for glib-2.6
Group:		System/Libraries
Requires:	glib-sharp2 = %{version}
Conflicts:	glib-sharp2 < 2.12.10-3

%description -n glib-sharp2-2.6
Glib-sharp is a C sharp language binding for glib.

%package -n glib-sharp2-2.8
Summary:	C sharp binding for glib-2.8
Group:		System/Libraries
Requires:	glib-sharp2 = %{version}
Conflicts:	glib-sharp2 < 2.12.10-3

%description -n glib-sharp2-2.8
Glib-sharp is a C sharp language binding for glib.

%package -n glib-sharp2-2.10
Summary:	C sharp binding for glib-2.10
Group:		System/Libraries
Requires:	glib-sharp2 = %{version}
Conflicts:	glib-sharp2 < 2.12.10-3

%description -n glib-sharp2-2.10
Glib-sharp is a C sharp language binding for glib.

%package -n glade-sharp2
Summary:	C sharp binding for glade
Group:		System/Libraries
Requires:	%{name} = %{version}

%description -n glade-sharp2
Glade-sharp is a C sharp language binding for glade.

%package -n glade-sharp2-2.4
Summary:	C sharp binding for glib-2.6
Group:		System/Libraries
Requires:	glade-sharp2 = %{version}
Conflicts:	glade-sharp2 < 2.12.10-3

%description -n glade-sharp2-2.4
Glade-sharp is a C sharp language binding for glade.

%package -n glade-sharp2-2.6
Summary:	C sharp binding for glib-2.6
Group:		System/Libraries
Requires:	glade-sharp2 = %{version}
Conflicts:	glade-sharp2 < 2.12.10-3

%description -n glade-sharp2-2.6
Glade-sharp is a C sharp language binding for glade.

%package -n glade-sharp2-2.8
Summary:	C sharp binding for glib-2.8
Group:		System/Libraries
Requires:	glade-sharp2 = %{version}
Conflicts:	glade-sharp2 < 2.12.10-3

%description -n glade-sharp2-2.8
Glade-sharp is a C sharp language binding for glade.

%package -n glade-sharp2-2.10
Summary:	C sharp binding for glib-2.10
Group:		System/Libraries
Requires:	glade-sharp2 = %{version}
Conflicts:	glade-sharp2 < 2.12.10-3

%description -n glade-sharp2-2.10
Glade-sharp is a C sharp language binding for glade.

%package doc
Summary:	Documentation for gtk-sharp
Group:		Development/Other
Requires(post): mono-tools >= 1.1.9
Requires(postun): mono-tools >= 1.1.9

%description doc
Gtk-sharp is a C sharp language binding for the  gtk+ toolkit.
This package provides documentation for gtk-sharp. 

%prep
%setup -qn %{oname}-%{version}
%autopatch -p1

%build
%configure
%make_build

%install
%make_install

rm -f sample/valtest/.libs/libvalobj.so
rm -f sample/opaquetest/.libs/libopaque.so

%post doc
%{_bindir}/monodoc --make-index > /dev/null

%postun doc
if [ "$1" = "0" -a -x %{_bindir}/monodoc ]; then %{_bindir}/monodoc --make-index > /dev/null
fi

%files
%{_libdir}/libatksharpglue-2.so
%{_libdir}/libgdksharpglue-2.so
%{_libdir}/libgtksharpglue-2.so
%{_libdir}/libpangosharpglue-2.so
%{_libdir}/pkgconfig/gtk-dotnet-2.0.pc
%{_libdir}/pkgconfig/gtk-sharp-2.0.pc
%{monodir}/gtk-sharp-2.0/atk-sharp.dll
%{monodir}/gtk-sharp-2.0/gdk-sharp.dll
%{monodir}/gtk-sharp-2.0/gtk-dotnet.dll
%{monodir}/gtk-sharp-2.0/gtk-sharp.dll
%{monodir}/gtk-sharp-2.0/pango-sharp.dll
%{monodir}/gac/atk-sharp/2.12.0.0*
%{monodir}/gac/gdk-sharp/2.12.0.0*
%{monodir}/gac/gtk-dotnet/2.12.0.0*
%{monodir}/gac/gtk-sharp/2.12.0.0*
%{monodir}/gac/pango-sharp/2.12.0.0*

%files 2.4
%{monodir}/gtk-sharp-2.0/policy.2.4.atk-sharp.dll
%{monodir}/gtk-sharp-2.0/policy.2.4.gdk-sharp.dll
%{monodir}/gtk-sharp-2.0/policy.2.4.gtk-dotnet.dll
%{monodir}/gtk-sharp-2.0/policy.2.4.gtk-sharp.dll
%{monodir}/gtk-sharp-2.0/policy.2.4.pango-sharp.dll
%{monodir}/gac/policy.2.4.atk-sharp/0.0.0.0*
%{monodir}/gac/policy.2.4.gdk-sharp/0.0.0.0*
%{monodir}/gac/policy.2.4.gtk-dotnet/0.0.0.0*
%{monodir}/gac/policy.2.4.gtk-sharp/0.0.0.0*
%{monodir}/gac/policy.2.4.pango-sharp/0.0.0.0*

%files 2.6
%{monodir}/gtk-sharp-2.0/policy.2.6.atk-sharp.dll
%{monodir}/gtk-sharp-2.0/policy.2.6.gdk-sharp.dll
%{monodir}/gtk-sharp-2.0/policy.2.6.gtk-dotnet.dll
%{monodir}/gtk-sharp-2.0/policy.2.6.gtk-sharp.dll
%{monodir}/gtk-sharp-2.0/policy.2.6.pango-sharp.dll
%{monodir}/gac/policy.2.6.atk-sharp/0.0.0.0*
%{monodir}/gac/policy.2.6.gdk-sharp/0.0.0.0*
%{monodir}/gac/policy.2.6.gtk-dotnet/0.0.0.0*
%{monodir}/gac/policy.2.6.gtk-sharp/0.0.0.0*
%{monodir}/gac/policy.2.6.pango-sharp/0.0.0.0*

%files 2.8
%{monodir}/gtk-sharp-2.0/policy.2.8.atk-sharp.dll
%{monodir}/gtk-sharp-2.0/policy.2.8.gdk-sharp.dll
%{monodir}/gtk-sharp-2.0/policy.2.8.gtk-dotnet.dll
%{monodir}/gtk-sharp-2.0/policy.2.8.gtk-sharp.dll
%{monodir}/gtk-sharp-2.0/policy.2.8.pango-sharp.dll
%{monodir}/gac/policy.2.8.atk-sharp/0.0.0.0*
%{monodir}/gac/policy.2.8.gdk-sharp/0.0.0.0*
%{monodir}/gac/policy.2.8.gtk-dotnet/0.0.0.0*
%{monodir}/gac/policy.2.8.gtk-sharp/0.0.0.0*
%{monodir}/gac/policy.2.8.pango-sharp/0.0.0.0*

%files 2.10
%{monodir}/gtk-sharp-2.0/policy.2.10.atk-sharp.dll
%{monodir}/gtk-sharp-2.0/policy.2.10.gdk-sharp.dll
%{monodir}/gtk-sharp-2.0/policy.2.10.gtk-dotnet.dll
%{monodir}/gtk-sharp-2.0/policy.2.10.gtk-sharp.dll
%{monodir}/gtk-sharp-2.0/policy.2.10.pango-sharp.dll
%{monodir}/gac/policy.2.10.atk-sharp/0.0.0.0*
%{monodir}/gac/policy.2.10.gdk-sharp/0.0.0.0*
%{monodir}/gac/policy.2.10.gtk-dotnet/0.0.0.0*
%{monodir}/gac/policy.2.10.gtk-sharp/0.0.0.0*
%{monodir}/gac/policy.2.10.pango-sharp/0.0.0.0*

%files -n glib-sharp2
%{_libdir}/libglibsharpglue-2.so
%{_libdir}/pkgconfig/glib-sharp-2.0.pc
%{monodir}/gtk-sharp-2.0/glib-sharp.dll
%{monodir}/gac/glib-sharp/2.12.0.0*

%files -n glib-sharp2-2.4
%{monodir}/gtk-sharp-2.0/policy.2.4.glib-sharp.dll
%{monodir}/gac/policy.2.4.glib-sharp/0.0.0.0*

%files -n glib-sharp2-2.6
%{monodir}/gtk-sharp-2.0/policy.2.6.glib-sharp.dll
%{monodir}/gac/policy.2.6.glib-sharp/0.0.0.0*

%files -n glib-sharp2-2.8
%{monodir}/gtk-sharp-2.0/policy.2.8.glib-sharp.dll
%{monodir}/gac/policy.2.8.glib-sharp/0.0.0.0*

%files -n glib-sharp2-2.10
%{monodir}/gtk-sharp-2.0/policy.2.10.glib-sharp.dll
%{monodir}/gac/policy.2.10.glib-sharp/0.0.0.0*

%files -n glade-sharp2
%{_libdir}/pkgconfig/glade-sharp-2.0.pc
%{_libdir}/libgladesharpglue-2.so
%{monodir}/gtk-sharp-2.0/glade-sharp.dll
%{monodir}/gac/glade-sharp/2.12.0.0*

%files -n glade-sharp2-2.4
%{monodir}/gtk-sharp-2.0/policy.2.4.glade-sharp.dll
%{monodir}/gac/policy.2.4.glade-sharp/0.0.0.0*

%files -n glade-sharp2-2.6
%{monodir}/gtk-sharp-2.0/policy.2.6.glade-sharp.dll
%{monodir}/gac/policy.2.6.glade-sharp/0.0.0.0*

%files -n glade-sharp2-2.8
%{monodir}/gtk-sharp-2.0/policy.2.8.glade-sharp.dll
%{monodir}/gac/policy.2.8.glade-sharp/0.0.0.0*

%files -n glade-sharp2-2.10
%{monodir}/gtk-sharp-2.0/policy.2.10.glade-sharp.dll
%{monodir}/gac/policy.2.10.glade-sharp/0.0.0.0*

%files doc
%doc ChangeLog README README.generator
#*[^makefile|README]
%doc sample
%{_prefix}/lib/monodoc/sources/gtk*

%files devel
%{_bindir}/*
%{_datadir}/gapi-2.0/
%{_libdir}/pkgconfig/gapi-2.0.pc
%{_prefix}/lib/%{oname}-2.0/

