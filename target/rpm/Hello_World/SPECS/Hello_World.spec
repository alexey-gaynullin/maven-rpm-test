%define _unpackaged_files_terminate_build 0
%define __jar_repack 0
Name: Hello_World
Version: 1.0
Release: 1
Summary: Hello_World
License: (c) null
Group: Application/System
autoprov: yes
autoreq: yes
Prefix: /usr/local
BuildArch: noarch
BuildRoot: /home/shaggy/maven-rpm-test/target/rpm/Hello_World/buildroot

%description

%install

if [ -d $RPM_BUILD_ROOT ];
then
  mv /home/shaggy/maven-rpm-test/target/rpm/Hello_World/tmp-buildroot/* $RPM_BUILD_ROOT
else
  mv /home/shaggy/maven-rpm-test/target/rpm/Hello_World/tmp-buildroot $RPM_BUILD_ROOT
fi

%files

%attr(550,root,root) "/usr/local/hello_world"
%attr(440,root,root)  "/etc/systemd/system/hello.service"
