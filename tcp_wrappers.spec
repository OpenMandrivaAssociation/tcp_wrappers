%define LIB_MAJOR 0
%define LIB_MINOR 7
%define LIB_REL 6

%define _disable_lto 1
%define major %{LIB_MAJOR}
%define libname %mklibname wrap %{major}
%define develname %mklibname wrap -d

Summary:	A security tool which acts as a wrapper for TCP daemons
Name:		tcp_wrappers
Version:	7.6
Release:	66
Group:		System/Servers
License:	BSD
URL:		https://ftp.porcupine.org/pub/security/index.html
Source0:	http://ftp.porcupine.org/pub/security/%{name}_%{version}-ipv6.4.tar.gz
# Borrowed from others
Patch0:		https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcpw7.2-config.patch
Patch1:		https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcpw7.2-setenv.patch
Patch2:		https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcpw7.6-netgroup.patch
Patch3:		https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-bug11881.patch
Patch4:		https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-bug17795.patch
Patch5:		https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-bug17847.patch
Patch6:		https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-fixgethostbyname.patch
Patch7:		https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-docu.patch
Patch9:		https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-man.patch
Patch10:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers.usagi-ipv6.patch
Patch11:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-shared.patch
Patch12:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-sig.patch
Patch14:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-ldflags.patch
Patch15:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-fix_sig-bug141110.patch
Patch16:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-162412.patch
Patch17:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-220015.patch
Patch19:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-siglongjmp.patch
Patch20:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-sigchld.patch
Patch21:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-196326.patch
Patch22:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers_7.6-249430.patch
Patch23:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-inetdconf.patch
Patch24:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-bug698464.patch
Patch25:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-xgets.patch
Patch26:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-initgroups.patch
Patch27:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-warnings.patch
Patch28:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-uchart_fix.patch
Patch29:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-altformat.patch
Patch30:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-7.6-aclexec.patch
Patch31:	https://src.fedoraproject.org/rpms/tcp_wrappers/raw/rawhide/f/tcp_wrappers-inetcf-c99.patch
# OM only
#Patch101:	tcp_wrappers-7.6-netgroup2.patch
Patch102:	tcp_wrappers-7.6-dont-hardcode-compiler.patch
BuildConflicts:	%{name}-devel
BuildRequires:	pkgconfig(libnsl)

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

%description -n %{libname}
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
Obsoletes:	%{mklibname wrap 0 -d} < %{version}-%{release}

%description -n	%{develname}
The tcp_wrappers package provides small daemon programs which can
monitor and filter incoming requests for systat, finger, ftp, telnet,
rlogin, rsh, exec, tftp, talk and other network services.

This package contains the static tcp_wrappers library (libwrap) and
its header files.

%prep
%autosetup -p1 -n %{name}_%{version}-ipv6.4

%build
%make_build CC="%{__cc}" RPM_OPT_FLAGS="%{optflags} -fPIC -DPIC -D_REENTRANT -DHAVE_STRERROR -DACLEXEC" \
    LDFLAGS="%{build_ldflags}" NETGROUP=-DNETGROUP REAL_DAEMON_DIR=%{_sbindir} \
    MAJOR=%{LIB_MAJOR} MINOR=%{LIB_MINOR} REL=%{LIB_REL} linux

%install
install -d %{buildroot}%{_includedir}
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man{3,5,8}

cp -a libwrap.so.* %{buildroot}/%{_libdir}
ln -s libwrap.so.%{LIB_MAJOR}.%{LIB_MINOR}.%{LIB_REL} %{buildroot}%{_libdir}/libwrap.so

install -m644 hosts_access.3 %{buildroot}%{_mandir}/man3
install -m644 hosts_access.5 hosts_options.5 %{buildroot}%{_mandir}/man5
ln hosts_access.5 %{buildroot}%{_mandir}/man5/hosts.allow.5
ln hosts_access.5 %{buildroot}%{_mandir}/man5/hosts.deny.5
install -m644 tcpd.8 tcpdchk.8 tcpdmatch.8 %{buildroot}%{_mandir}/man8

# (tpg) do not install it
#install -m644 libwrap.a %{buildroot}%{_libdir}
install -m644 tcpd.h %{buildroot}%{_includedir}

install -m755 safe_finger %{buildroot}%{_sbindir}
install -m755 tcpd %{buildroot}%{_sbindir}
install -m755 tcpdchk %{buildroot}%{_sbindir}
install -m755 tcpdmatch %{buildroot}%{_sbindir}
install -m755 try-from %{buildroot}%{_sbindir}

%files
%doc BLURB CHANGES README* DISCLAIMER Banners.Makefile
%{_sbindir}/*
%doc %{_mandir}/man*/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc DISCLAIMER
%{_includedir}/*
%{_libdir}/*.so
