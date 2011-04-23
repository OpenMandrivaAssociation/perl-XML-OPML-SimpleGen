%define upstream_name    XML-OPML-SimpleGen
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Create OPML using XML::Simple
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Test::More)
BuildRequires: perl(XML::Simple)
BuildRequires: perl(version)
# These requires are not detected automatically.
Requires: perl(Class::Accessor)
Requires: perl(XML::Simple)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
XML::OPML::SimpleGen lets you simply generate OPML documents without having
too much to worry about. It is a drop-in replacement for XML::OPML in
regards of generation. As this module uses XML::Simple it is rather
generous in regards of attribute or element names.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


