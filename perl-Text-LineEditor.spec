%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	LineEditor
Summary:	Text::LineEditor - simple line editor
Summary(pl.UTF-8):	Text::LineEditor - prosty edytor wierszowy
Name:		perl-Text-LineEditor
Version:	0.03
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	55c2e5c5b5bb89d02e1beeaa0c9f9de0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::LineEditor Perl module implements a -very- simple editor like
Berkeley mail used to use.

%description -l pl.UTF-8
Moduł Perla Text::LineEditor zawiera implementację prostego edytora
wierszowego, podobnego do używanego przez program Berkeley mail.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install example.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Text/LineEditor.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
