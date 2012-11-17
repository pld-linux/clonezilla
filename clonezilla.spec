Summary:	Opensource Clone System (ocs), clonezilla
Name:		clonezilla
Version:	3.1.18
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://free.nchc.org.tw/drbl-core/src/unstable/%{name}-%{version}.tar.bz2
# Source0-md5:	9451285a0f6ec4c5446e4fd2191d4eb6
URL:		http://www.clonezilla.org/
Requires:	bash
Requires:	drbl >= 2.1.33
Requires:	ntfsprogs >= 1.13.1
Requires:	partclone >= 0.2.22
Requires:	partimage >= 0.6.9
Requires:	perl-base
Requires:	psmisc
Requires:	udpcast
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Clonezilla, based on DRBL, Partition Image, ntfsclone, partclone, and
udpcast, allows you to do bare metal backup and recovery. Two types of
Clonezilla are available, Clonezilla live and Clonezilla SE (Server
Edition). Clonezilla live is suitable for single machine backup and
restore. While Clonezilla SE is for massive deployment, it can clone
many (40 plus!) computers simultaneously.

%prep
%setup -q -n %{name}-%{version}

%build
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/AUTHORS doc/ChangeLog.txt doc/VERSION
%dir /etc/drbl
/etc/drbl/*.conf
%attr(755,root,root) /usr/sbin/*
%attr(755,root,root) /usr/bin/*
%defattr(-,root,root)
/usr/share/drbl
