Name: libhfi1
Version: 0.5
Release: 23%{?dist}
Summary: Intel Omni-Path HFI Userspace Driver
Group: System Environment/Libraries
License: GPLv2 or BSD
Url: https://github.com/01org/opa-libhfi1verbs
# Source tarball generated with:
# git clone https://github.com/01org/opa-libhfi1verbs.git
# cd opa-libhfi1verbs
# git checkout spec_review_2
# git checkout c8df83205622a21d7062ac68cc8c4238953bba7d
# make dist
Source: %{name}-%{version}.tar.gz
BuildRequires: libibverbs-devel >= 1.2.0
BuildRequires: valgrind-devel
BuildRequires: autoconf automake libtool
ExclusiveArch: x86_64

%description
libhfi1 provides a device-specific userspace driver for Intel Host
Fabric interface cards. This driver is designed for use with the
libibverbs library.

%package static
Summary: Static version of the libhfi1 driver
Group: System Environment/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description static
Static version of libhfi1 that may be linked directly to an application.

%prep
%setup -q

%build
./autogen.sh
%configure --with-valgrind
make %{?_smp_flags}

%install
%make_install
# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.la

%files
%{_libdir}/libhfi1verbs*.so
%doc AUTHORS README
%license COPYING
%{_sysconfdir}/libibverbs.d/hfi1.driver

%files static
%{_libdir}/libhfi1verbs.a

%changelog
* Wed May 25 2016 Honggang Li <honli@redhat.com> -0.5-23
- Rebase to upstream release libhfi1-0.5-23.
  Resolves: bz1273171

* Thu Aug 20 2015 Donald Dutile <ddutile@redhat.com> - 0.2-2
- Initial check-in for rhel-7.2.
  Resolves: rhbz#1251634

* Mon Aug 17 2015 Michal Schmidt <mschmidt@redhat.com> - 0.2-2
- Build with valgrind.

* Wed Aug 12 2015 Michal Schmidt <mschmidt@redhat.com> - 0.2-1
- Initial packaging for RHEL, based on upstream spec file.
