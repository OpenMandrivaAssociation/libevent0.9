%define	rname	libevent
%define	name	libevent%{version}
%define	version	0.9

%define	major	0
%define libname	%mklibname event %{version} %{major}

Summary:	Abstract asynchronous event notification library
Name:		%{name}
Version:	%{version}
Release:	9
License:	BSD
Group:		System/Libraries
URL:		https://www.monkey.org/~provos/libevent/
Source0:	%{rname}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The libevent API provides a mechanism to execute a callback function
when a specific event occurs on a file descriptor or after a timeout
has been reached. libevent is meant to replace the asynchronous event
loop found in event driven network servers. An application just needs
to call event_dispatch() and can then add or remove events dynamically
without having to change the event loop.

%package -n	%{libname}
Summary:	Abstract asynchronous event notification library
Group:          System/Libraries

%description -n	%{libname}
The libevent API provides a mechanism to execute a callback function
when a specific event occurs on a file descriptor or after a timeout
has been reached. libevent is meant to replace the asynchronous event
loop found in event driven network servers. An application just needs
to call event_dispatch() and can then add or remove events dynamically
without having to change the event loop.

%package -n	%{libname}-devel
Summary:	Static library and header files for the libevent library
Group:		Development/C
Obsoletes:	%{name}-devel
Provides:	%{name}-devel
Requires:	%{libname} = %{version}-%{release}

%description -n	%{libname}-devel
The libevent API provides a mechanism to execute a callback function
when a specific event occurs on a file descriptor or after a timeout
has been reached. libevent is meant to replace the asynchronous event
loop found in event driven network servers. An application just needs
to call event_dispatch() and can then add or remove events dynamically
without having to change the event loop.

This package contains the static libevent library and its header files
needed to compile applications such as stegdetect, etc.

%prep

%setup -q -n %{rname}-%{version}

%build
%serverbuild
export CFLAGS="%{optflags} -fPIC"
%configure2_5x
%make libevent.a

gcc -Wl,-soname,libevent%{version}.so.%{major} -shared %{optflags} -fPIC \
    -Wl,--as-needed -Wl,--no-undefined -o libevent%{version}.so.%{major}.%{version} *.o

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_includedir}
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_mandir}/man3

install -m0755 libevent%{version}.so.%{major}.%{version} %{buildroot}%{_libdir}/
ln -s libevent%{version}.so.%{major}.%{version} %{buildroot}%{_libdir}/libevent%{version}.so.%{major}
ln -s libevent%{version}.so.%{major}.%{version} %{buildroot}%{_libdir}/libevent%{version}.so

install -m0644 libevent.a %{buildroot}%{_libdir}/libevent%{version}.a
install -m0644 event.h %{buildroot}%{_includedir}/libevent%{version}.h
install -m0644 event.3 %{buildroot}%{_mandir}/man3/libevent%{version}.3

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_mandir}/man3/*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9-8mdv2011.0
+ Revision: 620121
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.9-7mdv2010.0
+ Revision: 429728
- rebuild

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9-6mdv2009.0
+ Revision: 238947
- use -Wl,--as-needed -Wl,--no-undefined

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.9-5mdv2008.1
+ Revision: 140921
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.9-5mdv2008.0
+ Revision: 89834
- rebuild

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9-4mdv2008.0
+ Revision: 83749
- rebuild


* Fri Dec 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9-3mdv2007.0
+ Revision: 93712
- Import libevent0.9

* Fri Dec 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9-3mdv2007.1
- use the %%mkrel macro

* Fri Feb 03 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9-2mdk
- rebuild

* Mon Jan 17 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9-1mdk
- readded under a new name

* Sat Jul 31 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9-1mdk
- 0.9
- nuke redundant provides
- misc spec file fixes

* Mon May 03 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.8-1mdk
- 0.8
- drop the patch, it's included
- use the %%configure2_5x macro

* Tue Feb 24 2004 Pascal Terjan <pterjan@mandrake.org> 0.6-5mdk
- remove Obsoletes on current version

