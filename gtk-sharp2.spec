%define oname gtk-sharp
%define mono 1.0.2
%define monodir %{_prefix}/lib/mono

Summary:	C# language binding for the gtk+ toolkit
Name:		gtk-sharp2
Version:	2.12.11
Release:	4
License:	LGPLv2
Group:		System/Libraries
URL:		http://gtk-sharp.sourceforge.net/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gtk-sharp/%oname-%version.tar.bz2
Patch0:		gtk-sharp-2.12.11-fix-glib-includes.patch
Requires:	glib-sharp2 = %{version}
BuildRequires:	mono-devel >= %{mono}
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	monodoc

%description
Gtk-sharp is a C# language binding for the  gtk+ toolkit.

%package 2.4
Summary:	C# language binding for the gtk+-2.4 toolkit
Group:		System/Libraries
Requires:	gtk-sharp2 = %{version}
Conflicts:	gtk-sharp2 < 2.12.10-3

%description 2.4
Gtk-sharp is a C# language binding for the gtk+ toolkit.

%package 2.6
Summary:	C# language binding for the gtk+-2.6 toolkit
Group:		System/Libraries
Requires:	gtk-sharp2 = %{version}
Conflicts:	gtk-sharp2 < 2.12.10-3

%description 2.6
Gtk-sharp is a C# language binding for the gtk+ toolkit.

%package 2.8
Summary:	C# language binding for the gtk+-2.8 toolkit
Group:		System/Libraries
Requires:	gtk-sharp2 = %{version}
Conflicts:	gtk-sharp2 < 2.12.10-3

%description 2.8
Gtk-sharp is a C# language binding for the gtk+ toolkit.

%package 2.10
Summary:	C# language binding for the gtk+-2.10 toolkit
Group:		System/Libraries
Requires:	gtk-sharp2 = %{version}
Conflicts:	gtk-sharp2 < 2.12.10-3

%description 2.10
Gtk-sharp is a C# language binding for the gtk+ toolkit.

%package devel
Summary:	C# code generation tools for %{name}
Group:		Development/Other

%description devel
This contains the code generation tools of gtk-sharp. It is needed for building
C# wrappers for GObject APIs.

%package -n glib-sharp2
Summary:	C# binding for glib
Group:		System/Libraries
Requires:	mono >= %{mono}

%description -n glib-sharp2
Glib-sharp is a C# language binding for glib.

%package -n glib-sharp2-2.4
Summary:	C# binding for glib-2.4
Group:		System/Libraries
Requires:	glib-sharp2 = %{version}
Conflicts:	glib-sharp2 < 2.12.10-3

%description -n glib-sharp2-2.4
Glib-sharp is a C# language binding for glib.

%package -n glib-sharp2-2.6
Summary:	C# binding for glib-2.6
Group:		System/Libraries
Requires:	glib-sharp2 = %{version}
Conflicts:	glib-sharp2 < 2.12.10-3

%description -n glib-sharp2-2.6
Glib-sharp is a C# language binding for glib.

%package -n glib-sharp2-2.8
Summary:	C# binding for glib-2.8
Group:		System/Libraries
Requires:	glib-sharp2 = %{version}
Conflicts:	glib-sharp2 < 2.12.10-3

%description -n glib-sharp2-2.8
Glib-sharp is a C# language binding for glib.

%package -n glib-sharp2-2.10
Summary:	C# binding for glib-2.10
Group:		System/Libraries
Requires:	glib-sharp2 = %{version}
Conflicts:	glib-sharp2 < 2.12.10-3

%description -n glib-sharp2-2.10
Glib-sharp is a C# language binding for glib.

%package -n glade-sharp2
Summary:	C# binding for glade
Group:		System/Libraries
Requires:	%{name} = %{version}

%description -n glade-sharp2
Glade-sharp is a C# language binding for glade.

%package -n glade-sharp2-2.4
Summary:	C# binding for glib-2.6
Group:		System/Libraries
Requires:	glade-sharp2 = %{version}
Conflicts:	glade-sharp2 < 2.12.10-3

%description -n glade-sharp2-2.4
Glade-sharp is a C# language binding for glade.

%package -n glade-sharp2-2.6
Summary:	C# binding for glib-2.6
Group:		System/Libraries
Requires:	glade-sharp2 = %{version}
Conflicts:	glade-sharp2 < 2.12.10-3

%description -n glade-sharp2-2.6
Glade-sharp is a C# language binding for glade.

%package -n glade-sharp2-2.8
Summary:	C# binding for glib-2.8
Group:		System/Libraries
Requires:	glade-sharp2 = %{version}
Conflicts:	glade-sharp2 < 2.12.10-3

%description -n glade-sharp2-2.8
Glade-sharp is a C# language binding for glade.

%package -n glade-sharp2-2.10
Summary:	C# binding for glib-2.10
Group:		System/Libraries
Requires:	glade-sharp2 = %{version}
Conflicts:	glade-sharp2 < 2.12.10-3

%description -n glade-sharp2-2.10
Glade-sharp is a C# language binding for glade.

%package doc
Summary:	Documentation for gtk-sharp
Group:		Development/Other
Requires(post): mono-tools >= 1.1.9
Requires(postun): mono-tools >= 1.1.9

%description doc
Gtk-sharp is a C# language binding for the  gtk+ toolkit.
This package provides documentation for gtk-sharp. 

%prep
%setup -qn %{oname}-%{version}
%apply_patches

%build
%configure2_5x --disable-static
make

%install
%makeinstall_std

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
%defattr(-,root,root)
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

%changelog
* Wed Dec 14 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.11-2mdv2012.0
+ Revision: 740987
- fix glib includes

* Fri Aug 05 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.11-1
+ Revision: 693306
- new version

* Wed May 04 2011 Funda Wang <fwang@mandriva.org> 2.12.10-3
+ Revision: 665385
- split compat packages, now gtk# only provides main api version of assembly

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.12.10-2
+ Revision: 664948
- mass rebuild

* Tue Mar 16 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.10-1mdv2011.0
+ Revision: 521499
- new version

* Fri Dec 11 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.9-2mdv2010.1
+ Revision: 476296
- rebuild for new webkit-sharp

* Wed May 27 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.9-1mdv2010.0
+ Revision: 380298
- update to new version 2.12.9

* Thu Feb 05 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.8-2mdv2009.1
+ Revision: 337727
- rebuild for missing package

* Wed Feb 04 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.8-1mdv2009.1
+ Revision: 337267
- update to new version 2.12.8

* Thu Jan 29 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.7-2mdv2009.1
+ Revision: 335224
- remove doc conflict

* Thu Dec 18 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.7-1mdv2009.1
+ Revision: 315913
- update to new version 2.12.7

* Fri Nov 07 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.6-1mdv2009.1
+ Revision: 300848
- update to new version 2.12.6

* Wed Oct 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.5-1mdv2009.1
+ Revision: 296548
- update to new version 2.12.5

* Wed Sep 24 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.4-1mdv2009.0
+ Revision: 287696
- new version

* Wed Sep 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.3-1mdv2009.0
+ Revision: 283601
- new version
- update license

* Thu Aug 21 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.2-1mdv2009.0
+ Revision: 274496
- new version

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 2.12.1-2mdv2009.0
+ Revision: 264646
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.1-1mdv2009.0
+ Revision: 196695
- new version

* Wed Mar 05 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.0-1mdv2008.1
+ Revision: 179395
- new version
- update file list

* Fri Jan 25 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.11.91-1mdv2008.1
+ Revision: 157849
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Aug 30 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.2-1mdv2008.0
+ Revision: 75598
- new version
- drop patch

* Fri Jul 20 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.1-3mdv2008.0
+ Revision: 53764
- split out devel package

* Fri Jul 20 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.1-2mdv2008.0
+ Revision: 53758
- fix callback generator

* Mon Jun 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.1-1mdv2008.0
+ Revision: 41122
- new version


* Mon Feb 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.0-2mdv2007.0
+ Revision: 122675
- Import gtk-sharp2

* Mon Feb 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.0-2mdv2007.1
- Rebuild

* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 2.10.0-1mdv2007.0
- source URL
- New release 2.10.0

* Wed Aug 09 2006 Götz Waschk <waschk@mandriva.org> 2.9.0-1mdv2007.0
- drop patch
- remove gnome packages
- fix source URL
- New release 2.9.0

* Wed Jul 19 2006 Götz Waschk <waschk@mandriva.org> 2.8.3-2mdv2007.0
- fix postun script

* Sat Jul 08 2006 Götz Waschk <waschk@mandriva.org> 2.8.3-1mdv2007.0
- patch for new vte
- New release 2.8.3

* Sat Jun 24 2006 Götz Waschk <waschk@mandriva.org> 2.8.2-2mdv2007.0
- new vte

* Sun Mar 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.8.2-1mdk
- New release 2.8.2

* Fri Feb 10 2006 Götz Waschk <waschk@mandriva.org> 2.8.1-1mdk
- source URL
- New release 2.8.1

* Wed Jan 25 2006 Götz Waschk <waschk@mandriva.org> 2.8.0-1mdk
- update file list
- New release 2.8.0
- use mkrel

* Wed Nov 09 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.4.0-1mdk
- New release 2.4.0

* Thu Oct 13 2005 Götz Waschk <waschk@mandriva.org> 2.3.92-1mdk
- update file list
- drop merged patch
- New release 2.3.92

* Thu Sep 29 2005 Götz Waschk <waschk@mandriva.org> 2.3.91-4mdk
- move monodoc files to the doc package
- fix post* scripts

* Mon Sep 12 2005 Götz Waschk <waschk@mandriva.org> 2.3.91-3mdk
- fix post script

* Mon Sep 12 2005 Götz Waschk <waschk@mandriva.org> 2.3.91-2mdk
- update file list
- conflicts with old monodoc
- add monodoc to the post script

* Sun Sep 11 2005 Götz Waschk <waschk@mandriva.org> 2.3.91-1mdk
- add the docs
- New release 2.3.91

* Fri Aug 26 2005 Götz Waschk <waschk@mandriva.org> 2.3.90-1mdk
- bump gtkhtml deps
- remove gda and gnome-db
- New release 2.3.90

* Tue May 24 2005 Götz Waschk <waschk@mandriva.org> 1.9.5-2mdk
- fix deps, mono-find-requires isn't enough

* Sat May 21 2005 Götz Waschk <waschk@mandriva.org> 1.9.5-1mdk
- update file list
- New release 1.9.5

* Tue May 10 2005 Götz Waschk <waschk@mandriva.org> 1.9.3.1-1mdk
- New release 1.9.3.1

* Tue May 03 2005 Götz Waschk <waschk@mandriva.org> 1.9.3-2mdk
- fix build for x86_64

* Sat Apr 23 2005 Götz Waschk <waschk@mandriva.org> 1.9.3-1mdk
- bump gtkhtml deps
- New release 1.9.3

* Wed Mar 09 2005 Götz Waschk <waschk@linux-mandrake.com> 1.9.2-1mdk
- add dotnet dll
- remove panel files, merged into the gnome dll
- New release 1.9.2

* Mon Dec 27 2004 Götz Waschk <waschk@linux-mandrake.com> 1.9.1-1mdk
- spec fixes
- New release 1.9.1

* Wed Nov 10 2004 Götz Waschk <waschk@linux-mandrake.com> 1.9.0-1mdk
- initial package

* Fri Nov 05 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0.4-1mdk
- fix URL
- New release 1.0.4

* Wed Sep 29 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0.2-1mdk
- drop patch, back to gtkhtml-3.0
- New release 1.0.2

* Thu Jul 29 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-4mdk
- rebuild for new rpm

* Mon Jul 12 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0-3mdk
- Add conflicts to ease upgrade from 10.0

* Wed Jul 07 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-2mdk
- update gtkhtml patch and deps

* Fri Jul 02 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-1mdk
- remove docs
- fix source URL
- new version

* Tue Jun 22 2004 Götz Waschk <waschk@linux-mandrake.com> 0.98-2mdk
- fix doc package group

* Thu Jun 17 2004 Götz Waschk <waschk@linux-mandrake.com> 0.98-1mdk
- add libpangosharpglue to libgtksharpglue package
- add installed xml docs
- fix installation
- requires new mono
- fix groups
- new version

* Mon Jun 07 2004 Götz Waschk <waschk@linux-mandrake.com> 0.93-6mdk
- fix devel deps again (no need for vte and gtkhtml, they are only dlopened)
- update patch to really use new gtkhtml

* Sun Jun 06 2004 Marcel Pol <mpol@mandrake.org> 0.93-5mdk
- manually add requires for devel packages
- build against new gtkhtml

* Sat Jun 05 2004 Marcel Pol <mpol@mandrake.org> 0.93-4mdk
- split package
- place gapi files in glib-sharp

* Sat Jun 05 2004 Götz Waschk <waschk@linux-mandrake.com> 0.93-3mdk
- add vte deps (thanks Quel Qun)
- use libgtkhtml-3.1_9

* Fri Jun 04 2004 Götz Waschk <waschk@linux-mandrake.com> 0.93-2mdk
- fix deps

* Thu Jun 03 2004 Götz Waschk <waschk@linux-mandrake.com> 0.93-1mdk
- drop perl files
- requires new mono
- new version

* Thu May 06 2004 Götz Waschk <waschk@linux-mandrake.com> 0.91.1-1mdk
- fix file list
- requires new mono
- buildrequires monodoc
- add source URL
- new version

* Sat Apr 10 2004 Götz Waschk <waschk@linux-mandrake.com> 0.18-2mdk
- rebuild for new croco

* Sun Apr 04 2004 Götz Waschk <waschk@linux-mandrake.com> 0.18-1mdk
- fix doc file listing
- new version

* Fri Mar 12 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.17-2mdk
- Rebuild against latest gtkhtml/gal

* Mon Mar 01 2004 Götz Waschk <waschk@linux-mandrake.com> 0.17-1mdk
- fix some rpmlint warnings
- fix buildrequires
- new version

