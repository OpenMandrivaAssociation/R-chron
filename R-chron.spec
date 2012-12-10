%global packname  chron
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.3_42
Release:          1
Summary:          Chronological objects which can handle dates and times
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.3-42.tar.gz
Requires:         R-graphics R-stats 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-graphics R-stats 

%description
Chronological objects which can handle dates and times

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.3_42-1
+ Revision: 775046
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.3_41-1
+ Revision: 774846
- Update and rebuild with R2spec
- Update and rebuild with R2spec

* Tue Dec 29 2009 Jérôme Brenier <incubusss@mandriva.org> 2.3.33-1mdv2010.1
+ Revision: 483317
- import R-cran-chron

