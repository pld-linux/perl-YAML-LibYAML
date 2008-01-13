#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	YAML
%define	pnam	LibYAML
Summary:	YAML::XS::LibYAML - An XS Wrapper Module of libyaml
#Summary(pl.UTF-8):	
Name:		perl-YAML-LibYAML
Version:	0.26
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/YAML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b2da17e2393888cdc5996dc48fbae71a
# generic URL, check or change before uncommenting
URL:		http://search.cpan.org/dist/YAML-LibYAML/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description


# %description -l pl.UTF-8
# TODO

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/YAML/*.pm
%dir %{perl_vendorarch}/YAML/XS
%{perl_vendorarch}/YAML/XS/LibYAML.pm
%dir %{perl_vendorarch}/auto/YAML/XS/LibYAML
%{perl_vendorarch}/auto/YAML/XS/LibYAML/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/YAML/XS/LibYAML/*.so
%{_mandir}/man3/*