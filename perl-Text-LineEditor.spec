%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	LineEditor
Summary:	Text-LineEditor perl module
Summary(pl):	Modu³ perla Text-LineEditor
Name:		perl-Text-LineEditor
Version:	0.03
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-LineEditor - simple line editor.

%description -l pl
Text-LineEditor - prosty edytor liniowy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
