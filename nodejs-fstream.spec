%{?scl:%scl_package nodejs-fstream}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-fstream
Version:    1.0.3
Release:    3%{?dist}
Summary:    Advanced file system stream objects for Node.js
License:    BSD
Group:      System Environment/Libraries
URL:        https://github.com/isaacs/fstream
Source0:    http://registry.npmjs.org/fstream/-/fstream-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Provides advanced file system stream objects for Node.js.  These objects are
like FS streams, but with stat on them, and support directories and
symbolic links, as well as normal files.  Also, you can use them to set
the stats on a file, even if you don't change its contents, or to create
a symlink, etc.

%prep
%setup -q -n package
%nodejs_fixdep graceful-fs '>= 4.1.2'

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/fstream
cp -pr lib fstream.js package.json %{buildroot}%{nodejs_sitelib}/fstream

%nodejs_symlink_deps

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/fstream
%doc LICENSE README.md examples

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.3-3
- rebuilt

* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.3-2
- Use fixdep to fix dependency on graceful-fs

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.3-1
- New upstream release
- Fix bogus date in first changelog entry

* Thu Jan 16 2014 Tomas Hrcka <thrcka@redhat.com> - 0.1.25-1
- New upstream release 0.1.25

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.1.24-2
- replace provides and requires with macro

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.24-1
- new upstream release 0.1.24

* Fri Jul 12 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.23-1
- new upstream release 0.1.23

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.22-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.22-2
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.1.22-2
- Add support for software collections

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.22-1
- new upstream release 0.1.22

* Sun Jan 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.21-3
- fix License tag

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.21-2
- add missing build section
- fix summary/description

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.21-1
- new upstream release 0.1.21
- clean up for submission

* Thu Mar 29 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.18-1
- New upstream release 0.1.18

* Wed Mar 28 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.17-1
- new upstream release 0.1.17

* Thu Mar 22 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.14-1
- new upstream release 0.1.14

* Sun Mar 04 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.13-1
- new upstream release 0.1.13

* Thu Feb 09 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.12-1
- new upstream release 0.1.12

* Fri Jan 21 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.11-1
- initial package
