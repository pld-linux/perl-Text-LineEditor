%include	/usr/lib/rpm/macros.perl
Summary:	Text-LineEditor perl module
Summary(pl):	Modu³ perla Text-LineEditor
Name:		perl-Text-LineEditor
Version:	0.03
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-LineEditor-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-LineEditor - simple line editor.

%description -l pl
Text-LineEditor - prosty edytor liniowy.

%prep
%setup -q -n Text-LineEditor-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz example.pl
%{perl_sitelib}/Text/LineEditor.pm
%{_mandir}/man3/*
