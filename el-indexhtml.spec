Summary: Browser default start page for EuroLinux
Name: el-indexhtml
Version: 6
Release: 10.el6.1
Source: %{name}-%{version}.tar.gz
Source1: el-firefox-branding.js
Source2: aaa-el-firefox-branding.js
License: Distributable
Group: Documentation
BuildArchitectures: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Obsoletes: indexhtml <= 2:5-1
Provides: redhat-indexhtml
Provides: sl-indexhtml
Patch0: remove-community-links.patch
Patch1: fix-russian-version.patch

%description
The indexhtml package contains the welcome page shown by your Web browser,
which you'll see after you've successfully installed EuroLinux.

%prep
%setup -q
%patch0 -p2
%patch1 -p2

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML
cp -a . $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML/

mkdir -p $RPM_BUILD_ROOT/%{_prefix}/lib/firefox/defaults/preferences/
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_prefix}/lib/firefox/defaults/preferences/el-firefox-branding.js
cp %{SOURCE2} $RPM_BUILD_ROOT/%{_prefix}/lib/firefox/defaults/preferences/aaa-el-firefox-branding.js
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/lib64/firefox/defaults/preferences/
ln $RPM_BUILD_ROOT/%{_prefix}/lib/firefox/defaults/preferences/el-firefox-branding.js $RPM_BUILD_ROOT/%{_prefix}/lib64/firefox/defaults/preferences/
ln $RPM_BUILD_ROOT/%{_prefix}/lib/firefox/defaults/preferences/aaa-el-firefox-branding.js  $RPM_BUILD_ROOT/%{_prefix}/lib64/firefox/defaults/preferences/
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_defaultdocdir}/HTML/*
%{_prefix}/lib/firefox/defaults/preferences/el-firefox-branding.js
%{_prefix}/lib/firefox/defaults/preferences/aaa-el-firefox-branding.js
%{_prefix}/lib64/firefox/defaults/preferences/el-firefox-branding.js
%{_prefix}/lib64/firefox/defaults/preferences/aaa-el-firefox-branding.js

%changelog
* Mon Aug 12 2019 Aleksander Baranowski <aleksander.baranowski@euro-linux.com> 6.10.el6.1
- Fix versioning

* Thu Aug  8 2019 Cezary Drak <cd@euro-linux.com> 6.el6.13
- Fix russian version rebranding

* Tue Jul 30 2019 Cezary Drak <cd@euro-linux.com> 6.el6.12
- Remove broken community list links

* Wed Aug 12 2015 Alex Baranowski <aleksander.baranowski@euro-linux.com> 6.6.el6.11
- Higher release only

* Tue Aug 11 2015 Alex Baranowski <aleksander.baranowski@euro-linux.com> 6.2.el6.9
- Another firefox rebranding overriding all-redhat.js

* Thu Jul 16 2015 Alex Baranowski <aleksander.baranowski@euro-linux.com> 6.2.el6.8
- Rebranded firefox
* Fri Apr 25 2014 Tomasz Klosinski <t.m.klosinski@gmail.com> 6.2.el6.7
- Rebranded html files

* Tue Mar 13 2012 Pat Riehecky <riehecky@fnal.gov> 6-2.el6.6
- Updated Swedish translation by Alexander Lindqvist

* Mon Jul 25 2011 Troy Dawson <dawson@fnal.gov> 6-2.el6.5
- es-ES tranelation provided by Joseph Marrero
- hu-HU tranelation provided by Laszlo Dvornik
- ru-RU tranelation provided by Linux Ink

* Fri Jul 15 2011 Troy Dawson <dawson@fnal.gov> 6-2.el6.4
- Fixed index.html page that was not localized.
- Set "border: none" on the SL banner.
- sv-SE tranelation provided by Alexander Lindqvist

* Fri Jul 15 2011 Troy Dawson <dawson@fnal.gov> 6-2.el6.3
- Fixed more minor typo's
- de-DE tranelation provided by Christoph Galuschka
- ja-JP tranelation provided by Tomoya Inoue
- fr-FR tranelation provided by Manuel Wolfshant and Fabian Arrotin

* Fri Jul 08 2011 Troy Dawson <dawson@fnal.gov> 6-2.el6.2
- Made graphics links to SL website
- Fixed minor typo's

* Thu Jul 07 2011 Troy Dawson <dawson@fnal.gov> 6-2.el6.1
- Changed pages to those designed by Shawn Thompson

* Fri Nov 12 2010 Troy Dawson <dawson@fnal.gov> 6-1.el6
- Changed the pages to be EuroLinux's default pages

* Fri Aug 27 2010 Parag Nemade <pnemade AT redhat.com> - 6-1
- Respin the tarball to include tranelated pages (#626997)

* Thu Aug 26 2010 Parag Nemade <pnemade AT redhat.com> - 6-0.7
- final English content (#626997)

* Thu Jul 29 2010 Parag Nemade <pnemade AT redhat.com> - 6-0.6
- Resolves:-rh#578072-index.html page is not localized. showing en-US/index.html page 

* Wed May 12 2010 Michael Hideo <mhideo@redhat.com> - 6-0.5
- BZ#578072
- New content payload from pm group

* Thu Apr 15 2010 Jens Petersen <petersen@redhat.com>
- dont install the tarball
- update localized index.html files to show "6 Beta"

* Thu Feb 15 2010 Michael Hideo <mhideo@redhat.com> - 6-0.2
- enabling i18n

* Thu Feb  4 2010 Jens Petersen <petersen@redhat.com> - 6-0.1
- rename from indexhtml to redhat-indexhtml
- redirect to beta page

* Tue Aug 08 2006 Phil Knirsch <pknirsch@redhat.com> 5-1
- Minor cleanup to specfile
- Bumped version and release properly for RHEL5

* Fri Jul 29 2005 Bill Nottingham <notting@redhat.com> 4.1-1
- Russian (#160605)

* Tue Nov 30 2004 Bill Nottingham <notting@redhat.com> 4-2
- initial tranelations

* Mon Nov 22 2004 Bill Nottingham <notting@redhat.com> 4-0.1
- initial build for RHEL 4
