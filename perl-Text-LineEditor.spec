%include	/usr/lib/rpm/macros.perl
Summary:	Text-LineEditor perl module
Summary(pl):	Modu³ perla Text-LineEditor
Name:		perl-Text-LineEditor
Version:	0.03
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-LineEditor-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Text-LineEditor - simple line editor.

%description -l pl
Text-LineEditor - prosty edytor liniowy.

%prep
%setup -q -n Text-LineEditor-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Text/LineEditor
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz example.pl

%{perl_sitelib}/Text/LineEditor.pm
%{perl_sitearch}/auto/Text/LineEditor

%{_mandir}/man3/*
