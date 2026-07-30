%define upstream_name    XML-OPML-SimpleGen
%define upstream_version 0.07
Name:		perl-%{upstream_name}
Version:	0.07
Release:	1

Summary:	Create OPML using XML::Simple
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/S/ST/STEPHENCA/XML-OPML-SimpleGen-0.07.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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

