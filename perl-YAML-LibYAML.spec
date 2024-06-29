#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define	pdir	YAML
%define	pnam	LibYAML
Summary:	YAML::XS::LibYAML - An XS Wrapper Module of libyaml
Summary(pl.UTF-8):	YAML::XS::LibYAML - moduł wrappera XS dla libyaml
Name:		perl-YAML-LibYAML
Version:	0.89
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/YAML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	295a0fc87a89a9e4a5221d56fc98d8bf
URL:		https://metacpan.org/dist/YAML-LibYAML
BuildRequires:	perl-ExtUtils-MakeMaker
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.90
%endif
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAML::XS is a Perl YAML implementation using XS and libyaml.

YAML::XS::LibYAML is an XS wrapper module for libyaml.

%description -l pl.UTF-8
YAML::XS to perlowa implementacja YAML-a przy użyciu XS i biblioteki
libyaml.

YAML::XS::LibYAML to moduł wrappera XS dla libyaml.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/YAML/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/YAML/LibYAML.pm
%{perl_vendorarch}/YAML/XS.pm
%{perl_vendorarch}/YAML/XS
%dir %{perl_vendorarch}/auto/YAML/XS
%dir %{perl_vendorarch}/auto/YAML/XS/LibYAML
%attr(755,root,root) %{perl_vendorarch}/auto/YAML/XS/LibYAML/LibYAML.so
%{_mandir}/man3/YAML::LibYAML.3pm*
%{_mandir}/man3/YAML::XS.3pm*
%{_mandir}/man3/YAML::XS::LibYAML.3pm*
