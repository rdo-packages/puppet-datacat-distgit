%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-datacat
%global commit 5cce8f2389c94c0a96d38c85ebe222a0e400e087
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-datacat
Version:        0.6.2
Release:        1%{?alphatag}%{?dist}
Summary:        Puppet type for handling data fragments
License:        ASL 2.0

URL:            https://github.com/richardc/puppet-datacat

Source0:        http://github.com/richardc/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet >= 2.7.0

%description
Puppet type for handling data fragments

%prep
%setup -q -n %{name}-%{upstream_version}

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
* Fri Apr 01 2022 RDO <dev@lists.rdoproject.org> 0.6.2-1.5cce8f2git
- Update to post 0.6.2 (5cce8f2389c94c0a96d38c85ebe222a0e400e087)



