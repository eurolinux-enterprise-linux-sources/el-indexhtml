Summary: Browser default start page for EuroLinux
Name: el-indexhtml
Version: 7
Release: 7%{?dist}
Source: %{name}-%{version}.tar.gz
Source1: el-firefox-branding.js
Source2: aaa-el-firefox-branding.js
License: Distributable
Group: Documentation
BuildArch: noarch
Obsoletes: indexhtml <= 2:5-1
Provides: redhat-indexhtml
Patch0: remove-community-links.patch

%description
The indexhtml package contains the welcome page shown by your Web browser,
which you'll see after you've successfully installed EuroLinux

%prep
%setup -q 
%patch0 -p2

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML
cp -par HTML/* $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML/

mkdir -p $RPM_BUILD_ROOT/%{_prefix}/lib/firefox/defaults/preferences/
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_prefix}/lib/firefox/defaults/preferences/el-firefox-branding.js
cp %{SOURCE2} $RPM_BUILD_ROOT/%{_prefix}/lib/firefox/defaults/preferences/aaa-el-firefox-branding.js
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/lib64/firefox/defaults/preferences/
ln $RPM_BUILD_ROOT/%{_prefix}/lib/firefox/defaults/preferences/el-firefox-branding.js $RPM_BUILD_ROOT/%{_prefix}/lib64/firefox/defaults/preferences/
ln $RPM_BUILD_ROOT/%{_prefix}/lib/firefox/defaults/preferences/aaa-el-firefox-branding.js $RPM_BUILD_ROOT/%{_prefix}/lib64/firefox/defaults/preferences/

%files
%defattr(644, root, root, 755)
%{_defaultdocdir}/HTML/*
%{_prefix}/lib/firefox/defaults/preferences/el-firefox-branding.js
%{_prefix}/lib/firefox/defaults/preferences/aaa-el-firefox-branding.js
%{_prefix}/lib64/firefox/defaults/preferences/el-firefox-branding.js
%{_prefix}/lib64/firefox/defaults/preferences/aaa-el-firefox-branding.js
%changelog
* Mon Dec 23 2019 Aleksander Baranowski <aleksander.baranowski@euro-linux.com> 7.7.el7
- Version for new build system.

* Tue Jul 30 2019 Cezary Drak <cd@euro-linux.com> 7-3.3.el7.1
- Remove broken community list link

* Wed Aug 12 2015 Alex Baranowski <aleksander.baranowski@euro-linux.com> 7-3.3
- Firefox 38 branding fix

* Wed Jul 15 2015 Alex Baranowski <aleksander.baranowski@yahoo.pl> 7-3.2
- Firefox.Branding.js changed

* Mon Feb 23 2015 Alex Baranowski <aleksander.baranowski@yahoo.pl> 7-3.1
- EuroLinux rebranding 
* Mon Feb 23 2015 Pat Riehecky <riehecky@fnal.gov> 7-3
- Fix minor branding issue in xulrunner default prefs

* Wed Oct 1 2014 Pat Riehecky <riehecky@fnal.gov> 7-2
- UpDated for new website paths

* Tue May 13 2014 Pat Riehecky <riehecky@fnal.gov> 7-1
- Updated with artwork from Fixation

* Tue May 6 2014 Pat Riehecky <riehecky@fnal.gov> 7-0
- initial build from SL6 package
