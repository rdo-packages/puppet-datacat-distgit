Name:           puppet-datacat
Version:        XXX
Release:        XXX
Summary:        Puppet type for handling data fragments
License:        Apache-2.0

URL:            https://github.com/richardc/puppet-datacat

Source0:        http://github.com/richardc/puppet-datacat/archive/%{version}.tar.gz

BuildArch:      noarch

Requires:       puppet >= 2.7.0

%description
Puppet type for handling data fragments

%prep
%setup -q -n %{name}-%{version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/datacat/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/datacat/



%files
%{_datadir}/openstack-puppet/modules/datacat/


%changelog

