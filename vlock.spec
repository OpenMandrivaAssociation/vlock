Name:           vlock
Version:        2.2.2
Release:        MERGED INTO KBD PACKAGE
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


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0:2.2.2-7mdv2011.0
+ Revision: 670772
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0:2.2.2-6mdv2011.0
+ Revision: 608130
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0:2.2.2-5mdv2010.1
+ Revision: 524310
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0:2.2.2-4mdv2010.0
+ Revision: 427499
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0:2.2.2-3mdv2009.1
+ Revision: 351438
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0:2.2.2-2mdv2009.0
+ Revision: 265775
- rebuild early 2009.0 package (before pixel changes)

* Mon May 19 2008 David Walluck <walluck@mandriva.org> 0:2.2.2-1mdv2009.0
+ Revision: 209123
- 2.2.2
- back out libname change from last release (these are plugins)
- fix CFLAGS from last release
- fix perms
- add documentation
- remove overloaded macros from last release

  + Erwan Velu <erwan@mandriva.org>
    - 2.2.1

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 22 2007 David Walluck <walluck@mandriva.org> 0:2.1-1mdv2008.1
+ Revision: 92210
- add sources
- 2.1

* Mon Aug 27 2007 David Walluck <walluck@mandriva.org> 0:2.0-2mdv2008.0
+ Revision: 72239
- fix PAM support
- fix BOURNE_SHELL and PREFIX settings in config.mk

* Thu Aug 09 2007 David Walluck <walluck@mandriva.org> 0:2.0-1mdv2008.0
+ Revision: 60927
- 2.0

* Sat Jul 21 2007 David Walluck <walluck@mandriva.org> 1.4-1mdv2008.0
+ Revision: 54362
- 1.4
- fix build to actually use %%{optflags}
- patch to fix install
- Import vlock



* Sun Jul 23 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.3-16mdv2007.0
- Rediff P0 for new PAM
- use mkrel

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.3-15mdk
- Rebuild

* Fri Jan 16 2004 Abel Cheung <deaddog@deaddog.org> 1.3-14mdk
- Update patch0 to really remove hardcoded pam module path (and sync with
  fedora)

* Mon Oct 20 2003 Frederic Lepied <flepied@mandrakesoft.com> 1.3-13mdk
- rebuild for rewriting /etc/pam.d file

* Tue Mar 18 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.3-12mdk
- Patch1: Add missing includes

* Fri Jan 17 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.3-11mdk
- Rebuild

* Thu Dec  6 2001 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.3-10mdk
- Fix no-url-tag

* Tue Aug  7 2001 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.3-9mdk
- Fix invalid-distribution Linux-Mandrake

* Mon Feb 26 2001 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.3-8mdk
- Cleaned up specfile
- Added documenation files
- Pamstackizification

* Thu Jan 11 2001 David BAUDENS <baudens@mandrakesoft.com> 1.3-7mdk
- BuildRequires: pam-devel

* Thu Jul 20 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3-6mdk
- BM, macros and spec-helper

* Mon Apr 10 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.3-5mdk
- Fixed group

* Thu Nov 18 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>

- build release
- bzip2 manpage
- fix compilation for non-root users (bero sucks?)

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Wed Jan 13 1999 Michael Johnson <johnsonm@redhat.com>
- released 1.3

* Thu Mar 12 1998 Michael K. Johnson <johnsonm@redhat.com>
- Does not create a DoS attack if pty is closed (not applicable
  to use on a VC)

* Fri Oct 10 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved to new pam conventions.
- Use pam according to spec, rather than abusing it as before.
- Updated to version 1.1.
- BuildRoot

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Mon Mar 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- moved from pam.conf to pam.d
