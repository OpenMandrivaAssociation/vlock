Name:           vlock
Version:        2.0
Release:        %mkrel 1
Epoch:          0
Summary:        Program to lock one or more sessions on the Linux console
License:        GPL
Group:          Terminals
URL:            http://cthulhu.c3d2.de/~toidinamai/vlock/vlock.html
Source0:        http://cthulhu.c3d2.de/~toidinamai/vlock/archive/vlock-%{version}.tar.bz2
Requires:       pam
BuildRequires:  pam-devel
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
%{__sed} -i -e 's/\$(VLOCK_GROUP)/root/g;' -e 's/ -o root -g root//g;' Makefile

%build
%{make} CC=%{__cc} CFLAGS="%{optflags} -DUSE_PAM -Wall"

%install
%{__rm} -rf %{buildroot}

%{makeinstall_std} INSTALL=%{__install} PREFIX=%{_prefix}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc ChangeLog COPYING README SECURITY
%attr(-,root,root) %{_bindir}/*
%attr(-,root,root) %{_sbindir}/*
%{_mandir}/man1/*.1*
%{_mandir}/man8/*.8*
