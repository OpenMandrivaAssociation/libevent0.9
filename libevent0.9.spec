%define	rname	libevent
%define	name	libevent%{version}
%define	version	0.9

%define	major	0
%define libname	%mklibname event %{version} %{major}

Summary:	Abstract asynchronous event notification library
Name:		%{name}
Version:	%{version}
Release:	%mkrel 5
License:	BSD
Group:		System/Libraries
URL:		http://www.monkey.org/~provos/libevent/
Source0:	%{rname}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{rname}-%{version}-root

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

gcc -Wl,-soname,libevent%{version}.so.%{major} -shared %{optflags} -fPIC -o libevent%{version}.so.%{major}.%{version} *.o

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_mandir}/man3/*
