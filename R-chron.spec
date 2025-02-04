%global packname  chron
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.3.44
Release:          2
Summary:          Chronological objects which can handle dates and times
Group:            Sciences/Mathematics
License:          GPL-2
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/chron_2.3-44.tar.gz
Requires:         R-graphics R-stats 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires: R-scales
Requires: R-scales
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

# %check
# %{_bindir}/R CMD check %{packname}

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

