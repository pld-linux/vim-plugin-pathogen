%define		plugin	pathogen
Summary:	Vim plugin: Easy manipulation of 'runtimepath', 'path', 'tags', etc
Name:		vim-plugin-%{plugin}
Version:	2.3
Release:	1
License:	Vim
Group:		Applications/Editors/Vim
Source0:	https://github.com/tpope/vim-pathogen/archive/v%{version}/%{plugin}-%{version}.tar.gz
# Source0-md5:	8cf56e1d8f5c993bee44d89a003aa943
URL:		http://www.vim.org/scripts/script.php?script_id=2332
Requires:	vim-rt >= 4:7.2.170
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
Manage your 'runtimepath' with ease. In practical terms, pathogen.vim
makes it super easy to install plugins and runtime files in their own
private directories.

For management of individually installed plugins in `~/.vim/bundle`
adding `execute pathogen#infect()` to the top of your .vimrc is the
only other setup necessary.

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
%doc README.markdown CONTRIBUTING.markdown
%{_vimdatadir}/autoload/*.vim
