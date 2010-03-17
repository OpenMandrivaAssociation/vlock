Name:           vlock
Version:        2.2.2
Release:        %mkrel 5
Epoch:          0
Summary:        Program to lock one or more sessions on the Linux console
License:        GPL
Group:          Terminals
URL:            http://cthulhu.c3d2.de/~toidinamai/vlock/vlock.html
Source0:        http://cthulhu.c3d2.de/~toidinamai/vlock/archive/vlock-%{version}.tar.bz2
Source1:        http://cthulhu.c3d2.de/~toidinamai/vlock/archive/vlock-%{version}.tar.bz2.md5
Source2:        http://cthulhu.c3d2.de/~toidinamai/vlock/archive/vlock-%{version}.tar.bz2.sha1
Source3:        %{name}.pamd
Requires:       pam
BuildRequires:  pam-devel
Obsoletes:      %{mklibname vlock 0} <= %{epoch}:%{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The vlock program locks one or more sessions on the console.  Vlock
can lock the current terminal (local or remote) or the entire virtual
console system, which completely disables all console access.  The
vlock program unlocks when either the password of the user who started
vlock or the root password is typed.

Install vlock if you need to disable access to one console or to all
virtual consoles.

%prep
%setup -q
%{__sed} -i -e 's/\$(VLOCK_GROUP)/root/g;' -e 's/\$(ROOT_GROUP)/root/g;' -e 's/ -o root -g root//g;' Makefile
%{__sed} -i -e 's/\$(VLOCK_GROUP)/root/g;' -e 's/\$(MODULE_GROUP)/root/g;' -e 's/ -o root -g root//g;' modules/Makefile

%build
./configure --prefix=%{_usr}\
	--bindir=%{_bindir}\
	--sbindir=%{_sbindir}\
	--libdir=%{_libdir}\
	--mandir=%{_mandir}
%{make} CFLAGS="%{optflags} -std=gnu99"

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%{__mkdir_p} %{buildroot}%{_sysconfdir}/pam.d
%{__cp} -p %{SOURCE3} %{buildroot}%{_sysconfdir}/pam.d/%{name}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc ChangeLog COPYING PLUGINS README README.X11 SECURITY STYLE TODO
%attr(0755,root,root) %{_bindir}/vlock
%attr(4711,root,root) %{_sbindir}/vlock-main
%{_libdir}/%{name}
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
