Name:           vlock
Version:        1.4
Release:        %mkrel 1
Summary:        Locks one or more virtual consoles
License:        GPL
Group:          Terminals
URL:            http://cthulhu.c3d2.de/~toidinamai/vlock/vlock.html
Source0:        http://cthulhu.c3d2.de/~toidinamai/vlock/archive/vlock-%{version}.tar.bz2
Patch0:         vlock-1.3-system-auth.patch
Patch1:         vlock-1.4-install.patch
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
%patch0 -p1
%patch1 -p1

%build
%{make} CC=%{__cc} CFLAGS="%{optflags} -DUSE_PAM -Wall"

%install
%{__rm} -rf %{buildroot}

%{makeinstall} INSTALL=%{__install}

%{__mkdir_p} %{buildroot}%{_sysconfdir}/pam.d
%{__cp} -a vlock.pamd %{buildroot}%{_sysconfdir}/pam.d/vlock

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc COPYING README
%attr(4711,root,root) %{_bindir}/vlock
%{_mandir}/man1/vlock.1*
%config(noreplace) %{_sysconfdir}/pam.d/vlock
