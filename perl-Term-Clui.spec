%define upstream_name		Term-Clui
%define upstream_version 1.68

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.68
Release:	2

Summary:	%{upstream_name} module for perl
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Term/Term-Clui-1.68.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Term::Clui offers a high-level user interface to give the user of 
command-line applications a consistent "look and feel". Its metaphor 
for the computer is as a human-like conversation-partner, and as each 
question/response is completed it is summarised onto one line, and 
remains on screen, so that the history of the session gradually 
accumulates on the screen and is available for review, or for 
cut/paste. This user interface can therefore be intermixed with 
standard applications which write to STDOUT or STDERR, such as 
make, pgp, rcs etc.

For the user, &choose uses arrow keys (or hjkl) and Return or q; 
also SpaceBar for multiple choices. &confirm expects y, Y, n or N. 
In general, ctrl-L redraws the (currently active bit of the) screen. 
&edit and &view use the default EDITOR and PAGER if possible.

It's fast, simple, and has few external dependencies. It doesn't use curses 
(which is a whole-of-screen interface); it uses a small subset of vt100 
sequences (up down left right normal and reverse) which are very portable.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Term
%{_mandir}/*/*

%changelog
* Sun Nov 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.640.0-1mdv2011.0
+ Revision: 602391
- update to new version 1.64

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.620.0-1mdv2011.0
+ Revision: 596035
- update to new version 1.62

* Fri Oct 22 2010 StÃ©phane TÃ©letchÃ©a <steletch@mandriva.org> 1.610.0-1mdv2011.0
+ Revision: 587322
- Update to version 1.61

* Fri Jun 04 2010 StÃ©phane TÃ©letchÃ©a <steletch@mandriva.org> 1.560.0-1mdv2011.0
+ Revision: 547079
- Update to 1.56

* Fri May 07 2010 StÃ©phane TÃ©letchÃ©a <steletch@mandriva.org> 1.540.0-1mdv2010.1
+ Revision: 543137
- Update to 1.54 (brings mouse support, fixes some bugs
- Spec little cleanup about spaces and tabs

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.440.0-1mdv2010.1
+ Revision: 461029
- update to 1.44

* Mon Oct 05 2009 StÃ©phane TÃ©letchÃ©a <steletch@mandriva.org> 1.430.0-1mdv2010.0
+ Revision: 453864
- New version 1.43

* Sun Sep 27 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.420.0-1mdv2010.0
+ Revision: 449990
- update to 1.42

* Tue Aug 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.410.0-1mdv2010.0
+ Revision: 409023
- rebuild using %%perl_convert_version

* Sun Mar 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.41-1mdv2009.1
+ Revision: 353022
- new version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.40-4mdv2009.0
+ Revision: 258487
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.40-3mdv2009.0
+ Revision: 246515
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.40-1mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 22 2007 StÃ©phane TÃ©letchÃ©a <steletch@mandriva.org> 1.40-1mdv2008.0
+ Revision: 68947
- 1.40

* Thu May 03 2007 Olivier Thauvin <nanardon@mandriva.org> 1.39-1mdv2008.0
+ Revision: 22087
- 1.39


* Sun Nov 12 2006 StÃ©phane TÃ©letchÃ©a <steletch@mandriva.org> 1.37-1mdv2007.0
+ Revision: 83527
- 1.37
- Import perl-Term-Clui

* Tue Aug 22 2006 Stéphane Téletchéa <steletch@mandriva.org> 1.36-1mdv2007
- Version 1.36
- Fix in the source address

* Sat May 06 2006 Stéphane Téletchéa <steletch@mandriva.org> 1.35-2mdk
- Minor fix to better follow Perl Policy

* Thu May 04 2006 Stéphane Téletchéa <steletch@mandriva.org> 1.35-1mdk
- Initial Mandriva release


