%define upstream_name    Encode-Locale
%define upstream_version 1.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    7

Summary:    Determine the locale encoding
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Encode/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Encode)
BuildRequires: perl(Encode::Alias)
BuildRequires: perl(Test)
BuildRequires: perl-devel
BuildArch: noarch

%description
In many applications it's wise to let Perl use Unicode for the strings it
processes. Most of the interfaces Perl has to the outside world is still
byte based. Programs therefore needs to decode byte strings that enter the
program from the outside and encode them again on the way out.

The POSIX locale system is used to specify both the language conventions
requested by the user and the preferred character set to consume and
output. The 'Encode::Locale' module looks up the charset and encoding
(called a CODESET in the locale jargon) and arrange for the the Encode
manpage module to know this encoding under the name "locale". It means
bytes obtained from the environment can be converted to Unicode strings by
calling 'Encode::encode(locale => $bytes)' and converted back again with
'Encode::decode(locale => $string)'.

Where file systems interfaces pass file names in and out of the program we
also need care. The trend is for operating systems to use a fixed file
encoding that don't actually depend on the locale; and this module
determines the most appropriate encoding for file names. The the Encode
manpage module will know this encoding under the name "locale_fs". For
traditional Unix systems this will be an alias to the same encoding as
"locale".

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.20.0-4mdv2012.0
+ Revision: 765198
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.20.0-3
+ Revision: 763714
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.20.0-2
+ Revision: 763060
- rebuild

* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.20.0-1
+ Revision: 662537
- import perl-Encode-Locale

