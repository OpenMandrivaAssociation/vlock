%define version	1.3
%define release %mkrel 16

Summary:	A program which locks one or more virtual consoles
Name:		vlock
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Terminals

URL:		ftp://tsx-11.mit.edu:/pub/linux/sources/usr.bin/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		vlock-1.3-system-auth.patch
Patch1:		vlock-1.3-includes.patch.bz2

Requires:	pam >= 0.59
BuildRequires:	pam-devel
BuildRoot:	%{_tmppath}/%name-%version-%release-root

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
%patch0 -p1 -b .system-auth
%patch1 -p1 -b .includes

%build
%make RPM_OPT_FLAGS="${RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
install -m 755 -D -s vlock $RPM_BUILD_ROOT%{_bindir}/vlock
install -m 644 -D vlock.1 $RPM_BUILD_ROOT%{_mandir}/man1/vlock.1
install -m 644 -D vlock.pamd $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/vlock

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/pam.d/vlock
%doc COPYING README
%{_bindir}/vlock
%{_mandir}/man1/vlock.1*
