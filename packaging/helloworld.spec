Name: helloworld		
Version: 0.1
Release: 0
Summary: Test of packaging.

Group:	Development/Languages/C and C++	
License: GPL-3.0+

BuildRequires: scons
BuildRequires: gcc
BuildRequires: g++
BuildRequires: swig
BuildRequires: swig2.0
BuildRequires: python-devel
#Requires:	

%description
Testing packages using python binding and binaries.

%prep
%setup -q


%build
%configure
scons incdir_python=/usr/include/python2.7/ %{?_smp_mflags}


%install
scons incdir_python=/usr/include/python2.7/ --install-sandbox=%{buildroot}

%files
%defattr(-,root,root)
/%{_bindir}/*
/%{_libdir}/lib*.so.*
#/%{_mandir}/man1/*.1.gz

%files devel
%defattr(-,root,root)
/%{_libdir}/*.a
/%{_includedir}/*.hpp

%files python
%defattr(-,root,root)
/%{py_sitedir}

%changelog
* Sat Jul 5 2014 - arnaud.marcantoine@gmail.com
- first release of packaging
