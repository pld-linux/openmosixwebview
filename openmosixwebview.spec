Summary:	A PHP script for monitoring an openMosix cluster via the Web
Summary(pl.UTF-8):   openmosixwebview - skrypt PHP monitorujący pracę klastra openMosix
Name:		openmosixwebview
Version:	0.2.13
Release:	4
License:	GPL
Group:		Applications/System
Source0:	http://laurel.datsi.fi.upm.es/~rpons/openmosix/download/%{name}-%{version}.tar.gz
# Source0-md5:	fce2e62f43852ffe2e4f25546179c8a7
URL:		http://laurel.datsi.fi.upm.es/~rpons/openmosix/
Requires:	openmosixview-collector
Requires:	php(gd)
Requires:	webserver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _phpdir     /home/services/httpd/html/mosix

%description
openMosixWebView is a PHP script for monitoring an openMosix cluster
via the Web. It produces Web charts and useful info tables. It uses
openMosixview's openMosixCollector logs and openMosix metainfo.

%description -l pl.UTF-8
openMosixWebView to skrypt pozwalający na monitorowanie klastra
openMosix poprzez interfejs WWW. Wyświetla wykresy oraz przydatne
informacje w formie tabelek. Do zbierania informacji wykorzystuje
openMosixCollector.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpdir}

cp -a . $RPM_BUILD_ROOT%{_phpdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS FAQ
%{_phpdir}/*
