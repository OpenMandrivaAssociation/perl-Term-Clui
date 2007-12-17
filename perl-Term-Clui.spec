%define module	Term-Clui
%define name	perl-%{module}
%define version 1.40
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{module} module for perl
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp.perl.org/pub/CPAN/modules/by-module/Term/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Term
%{_mandir}/*/*


