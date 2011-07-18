Summary:	Opensource Clone System (ocs), clonezilla
Name:		clonezilla
Version:	2.3.8
Release:	27.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://free.nchc.org.tw/drbl-core/src/stable/%{name}-%{version}-27.tar.bz2
URL:		http://www.clonezilla.org/
Requires:	bash
Requires:	drbl >= 1.9.9-19
Requires:	ntfsprogs >= 1.13.1
Requires:	partclone >= 0.2.22
Requires:	partimage >= 0.6.9
Requires:	perl-base
Requires:	psmisc
Requires:	udpcast
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		drbldir		%{_libdir}/drbl

%description
Clonezilla, based on DRBL, Partition Image, ntfsclone, partclone, and
udpcast, allows you to do bare metal backup and recovery. Two types of
Clonezilla are available, Clonezilla live and Clonezilla SE (Server
Edition). Clonezilla live is suitable for single machine backup and
restore. While Clonezilla SE is for massive deployment, it can clone
many (40 plus!) computers simultaneously.

%prep
%setup -q -n %{name}-%{version}-27

grep -rl /opt/drbl/ . | xargs sed -i -e 's,/opt/drbl,%{drbldir},g'

%build
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	maindir=%{drbldir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%defattr(-,root,root)
%{drbldir}/bin/*
%{drbldir}/sbin/*
%{drbldir}/conf/*
%{drbldir}/setup/*
%{drbldir}/samples/*
