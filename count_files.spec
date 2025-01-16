Name: count_files
Version: 1.0
Release: 1%{?dist}
Summary: Script to count files in the /etc directory

License: GPL
Source0: count_files.sh

%description
Script to count files in the /etc directory, excluding directories and links.

%prep

%build

%install
mkdir -p %{buildroot}/usr/local/bin
cp %{SOURCE0} %{buildroot}/usr/local/bin/count_files.sh

%files
/usr/local/bin/count_files.sh

%changelog

