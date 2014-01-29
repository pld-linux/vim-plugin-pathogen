%define		plugin	pathogen
Summary:	Vim plugin: Easy manipulation of 'runtimepath', 'path', 'tags', etc
Name:		vim-plugin-%{plugin}
Version:	2.2
Release:	1
License:	Vim
Group:		Applications/Editors/Vim
Source0:	https://github.com/tpope/vim-pathogen/tarball/v%{version}/%{plugin}-%{version}.tgz
# Source0-md5:	5d5b7692a0aaac21d26a866a7ea7ad61
URL:		http://www.vim.org/scripts/script.php?script_id=2332
# for _vimdatadir
Requires:	vim-rt >= 4:7.2.170
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
Manage your 'runtimepath' with ease. In practical terms, pathogen.vim
makes it super easy to install plugins and runtime files in their own
private directories.

%prep
%setup -qc
mv *-%{plugin}-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/autoload
cp -p autoload/*.vim $RPM_BUILD_ROOT%{_vimdatadir}/autoload

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.markdown
%{_vimdatadir}/autoload/*.vim
