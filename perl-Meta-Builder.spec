#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Meta-Builder
Version  : 0.004
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Meta-Builder-0.004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Meta-Builder-0.004.tar.gz
Summary  : 'Tools for creating Meta objects to track custom metrics.'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Meta-Builder-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Fennec::Lite)
BuildRequires : perl(Test::Exception)

%description
NAME
Meta::Builder - Tools for creating Meta objects to track custom
metrics.
DESCRIPTION

%package dev
Summary: dev components for the perl-Meta-Builder package.
Group: Development
Provides: perl-Meta-Builder-devel = %{version}-%{release}
Requires: perl-Meta-Builder = %{version}-%{release}

%description dev
dev components for the perl-Meta-Builder package.


%package perl
Summary: perl components for the perl-Meta-Builder package.
Group: Default
Requires: perl-Meta-Builder = %{version}-%{release}

%description perl
perl components for the perl-Meta-Builder package.


%prep
%setup -q -n Meta-Builder-0.004
cd %{_builddir}/Meta-Builder-0.004

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Meta::Builder.3
/usr/share/man/man3/Meta::Builder::Base.3
/usr/share/man/man3/Meta::Builder::Util.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
