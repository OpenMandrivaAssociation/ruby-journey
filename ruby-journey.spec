%define rname	journey

Name:		ruby-journey
Summary:	Ruby router
Version:	1.0.3
Release:	1
License:	MIT
Group:		Development/Ruby
URL:		http://rubygems.org/gems/journey
Source0:	http://rubygems.org/downloads/journey-1.0.3.gem
BuildArch:	noarch
BuildRequires:	ruby-RubyGems

%description
Journey is a router. It routes requests.

%prep

%build

%install
gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache

%files
%{ruby_gemdir}/gems/%{rname}-%{version}
%{ruby_gemdir}/specifications/%{rname}-%{version}.gemspec
%doc %{ruby_gemdir}/doc/%{rname}-%{version}
