%define		php_min_version 5.4.0
%include	/usr/lib/rpm/macros.php
Summary:	Facebook SDK for PHP (v5)
Name:		php-facebook-graph-sdk
Version:	5.5.0
Release:	1
License:	BSD-like
Group:		Development/Languages/PHP
Source0:	https://github.com/facebook/php-graph-sdk/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	56867bb278d6d415f72c0ab202c9cab2
URL:		https://github.com/facebook/php-graph-sdk
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(core) >= %{php_min_version}
Requires:	php(curl)
Requires:	php(hash)
Requires:	php(json)
Suggests:	php(session)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define		_noautoreq_pear base_facebook.php

%description
This package contains the open source PHP SDK that allows you to
access the Facebook Platform from your PHP app.

%prep
%setup -qn php-graph-sdk-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a src/* $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{php_data_dir}/Facebook
