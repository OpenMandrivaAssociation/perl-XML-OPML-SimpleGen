%define upstream_name    XML-OPML-SimpleGen
%define upstream_version 0.07
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Create OPML using XML::Simple
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/XML/XML-OPML-SimpleGen-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(DateTime)
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(XML::Simple)
BuildRequires:	perl(version)
# These requires are not detected automatically.
Requires:	perl(Class::Accessor)
Requires:	perl(XML::Simple)
BuildArch:	noarch

%description
XML::OPML::SimpleGen lets you simply generate OPML documents without having
too much to worry about. It is a drop-in replacement for XML::OPML in
regards of generation. As this module uses XML::Simple it is rather
generous in regards of attribute or element names.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.40.0-3mdv2011.0
+ Revision: 656979
- rebuild for updated spec-helper

* Wed Dec 15 2010 Shlomi Fish <shlomif@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 622190
- Add Requires: that were not detected

* Fri Dec 03 2010 Shlomi Fish <shlomif@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 607885
- import perl-XML-OPML-SimpleGen



