Name: runc
Version: %{version}
Release: %{commit}%{?dist}
Summary: runc is a CLI tool for spawning and running containers according to the OCI specification

Group: Development/GAIA
License: Apache
Source: runc.tar.gz

Requires: systemd-units
Requires: libseccomp

%define pkgname  %{name}-%{version}-%{release}

%description
lighthouse plugin

%prep
%setup -n runc-%{version}

%build
make runc
make man

%install
install -d $RPM_BUILD_ROOT/%{_bindir}
install -d $RPM_BUILD_ROOT/%{_unitdir}

install -p -m 755 runc  $RPM_BUILD_ROOT/%{_bindir}/runc
install -D -m 644 man/man8/*.8 %{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files

/%{_bindir}/runc
