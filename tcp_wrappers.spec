%define LIB_MAJOR 0
%define LIB_MINOR 7
%define LIB_REL 6

%define _disable_lto 1
%define	major %{LIB_MAJOR}
%define libname %mklibname wrap %{major}
%define develname %mklibname wrap -d

Summary:	A security tool which acts as a wrapper for TCP daemons
Name:		tcp_wrappers
Version:	7.6
Release:	59
Group:		System/Servers
License:	BSD
URL:		ftp://ftp.porcupine.org/pub/security/index.html
Source0:	http://ftp.porcupine.org/pub/security/%{name}_%{version}.tar.bz2
Patch0:		tcpw7.2-config.patch
Patch1:		tcpw7.2-setenv.patch
Patch2:		tcpw7.6-netgroup.patch
Patch3:		tcp_wrappers-7.6-bug11881.patch
Patch4:		tcp_wrappers-7.6-bug17795.patch
Patch5:		tcp_wrappers-7.6-bug17847.patch
Patch6:		tcp_wrappers-7.6-fixgethostbyname.patch
Patch7:		tcp_wrappers-7.6-docu.patch
Patch9:		tcp_wrappers.usagi-ipv6.patch
Patch10:	tcp_wrappers.ume-ipv6.patch
Patch11:	tcp_wrappers-7.6-shared.patch
Patch12:	tcp_wrappers-7.6-sig.patch
Patch13:	tcp_wrappers-7.6-strerror.patch
Patch14:	tcp_wrappers-7.6-ldflags.patch
Patch15:	tcp_wrappers-7.6-fix_sig-bug141110.patch
Patch16:	tcp_wrappers-7.6-162412.patch
Patch17:	tcp_wrappers-7.6-220015.patch
Patch18:	tcp_wrappers-7.6-restore_sigalarm.patch
Patch19:	tcp_wrappers-7.6-siglongjmp.patch
Patch20:	tcp_wrappers-7.6-sigchld.patch
Patch21:	tcp_wrappers-7.6-196326.patch
Patch22:	tcp_wrappers_7.6-249430.patch
Patch100:	tcp_wrappers-bug41864.diff
Patch101:	tcp_wrappers-7.6-netgroup2.patch
Patch102:	tcp_wrappers-7.6-dont-hardcode-compiler.patch
Patch103:	tcp_wrappers-7.6-clang.patch
BuildConflicts:	%{name}-devel

%description
The tcp_wrappers package provides small daemon programs which can
monitor and filter incoming requests for systat, finger, FTP, telnet,
rlogin, rsh, exec, tftp, talk and other network services.

Install the tcp_wrappers program if you need a security tool for
filtering incoming network services requests.

This version also supports IPv6.

%package -n %{libname}
Summary:	A security library which acts as a wrapper for TCP daemons
Group:		System/Libraries

%description -n	%{libname}
The tcp_wrappers package provides small daemon programs which can
monitor and filter incoming requests for systat, finger, ftp, telnet,
rlogin, rsh, exec, tftp, talk and other network services.

This package contains the shared tcp_wrappers library (libwrap).

%package -n %{develname}
Summary:	A security library which acts as a wrapper for TCP daemons
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libwrap-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	wrap-devel = %{version}-%{release}
Obsoletes:	%{name}-devel < %{version}-%{release}
Obsoletes:	%{mklibname wrap 0 -d}

%description -n	%{develname}
The tcp_wrappers package provides small daemon programs which can
monitor and filter incoming requests for systat, finger, ftp, telnet,
rlogin, rsh, exec, tftp, talk and other network services.

This package contains the static tcp_wrappers library (libwrap) and
its header files.

%prep

%setup -q -n %{name}_%{version}
%patch0 -p1 -b .config
%patch1 -p1 -b .setenv
%patch2 -p1 -b .netgroup
%patch3 -p1 -b .bug11881
%patch4 -p1 -b .bug17795
%patch5 -p1 -b .bug17847
%patch6 -p1 -b .fixgethostbyname
%patch7 -p1 -b .docu
%patch9 -p1 -b .usagi-ipv6
%patch10 -p1 -b .ume-ipv6
%patch11 -p1 -b .shared
%patch12 -p1 -b .sig
%patch13 -p1 -b .strerror
%patch14 -p1 -b .cflags
%patch15 -p1 -b .fix_sig
%patch16 -p1 -b .162412
%patch17 -p1 -b .220015
%patch18 -p1 -b .restore_sigalarm
%patch19 -p1 -b .siglongjmp
%patch20 -p1 -b .sigchld
%patch21 -p1 -b .196326
%patch22 -p1 -b .249430

%patch100 -p0 -b .bug41864
%patch101 -p1 -b .netgroup2~
%patch102 -p1 -b .cc~
%patch103 -p1 -b .clang

%build
%make CC=%{__cc} RPM_OPT_FLAGS="%{optflags} -fPIC -DPIC -D_REENTRANT -DHAVE_STRERROR" \
    LDFLAGS="%{ldflags}" NETGROUP=-DNETGROUP REAL_DAEMON_DIR=%{_sbindir} \
    MAJOR=%{LIB_MAJOR} MINOR=%{LIB_MINOR} REL=%{LIB_REL} linux

%install

install -d %{buildroot}%{_includedir}
install -d %{buildroot}/%{_lib}
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man{3,5,8}

install -m644 hosts_access.3 %{buildroot}%{_mandir}/man3
install -m644 hosts_access.5 hosts_options.5 %{buildroot}%{_mandir}/man5
ln hosts_access.5 %{buildroot}%{_mandir}/man5/hosts.allow.5
ln hosts_access.5 %{buildroot}%{_mandir}/man5/hosts.deny.5
install -m644 tcpd.8 tcpdchk.8 tcpdmatch.8 %{buildroot}%{_mandir}/man8

cp -a libwrap.so.* %{buildroot}/%{_lib}
ln -srf %{buildroot}/%{_lib}/libwrap.so.%{LIB_MAJOR}.%{LIB_MINOR}.%{LIB_REL} %{buildroot}%{_libdir}/libwrap.so

# (tpg) do not install it
#install -m644 libwrap.a %{buildroot}%{_libdir}
install -m644 tcpd.h %{buildroot}%{_includedir}

install -m755 safe_finger %{buildroot}%{_sbindir}
install -m755 tcpd %{buildroot}%{_sbindir}
install -m755 tcpdchk %{buildroot}%{_sbindir}
install -m755 tcpdmatch %{buildroot}%{_sbindir}
install -m755 try-from %{buildroot}%{_sbindir}

# (fg) 20000905 FIXME FIXME FIXME: setenv in libwrap.a is rather strange for
# one, so I remove it here - but will it break anything else?
#(peroyvind): do it with a patch in stead now
#ar d %{buildroot}%{_libdir}/libwrap.a setenv.o

%files
%doc BLURB CHANGES README* DISCLAIMER Banners.Makefile
%{_sbindir}/*
%{_mandir}/man*/*

%files -n %{libname}
/%{_lib}/*.so.%{major}*

%files -n %{develname}
%doc DISCLAIMER
%{_includedir}/*
%{_libdir}/*.so
