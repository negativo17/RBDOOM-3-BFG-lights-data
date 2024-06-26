Name:           RBDOOM-3-BFG-lights-data
Version:        1.3.0
Release:        1
Summary:        Doom 3 BFG Edition baked environment probes and lightgrid data
License:        GPL
URL:            https://github.com/RobertBeckebans/%{name}
BuildArch:      noarch

Source0:        %{name}-%{version}.tar.xz

Requires:       doom3bfg
Requires:       RBDOOM-3-BFG >= 1.3.0

Provides:       doom3bfg-lights-data = %{version}-%{release}

%description
Baked environment probes and lightgrid data for all Doom 3 BFG Edition single
player maps when using the RBDOOM-3-BFG engine.

The data is generated by loading each level and executing the following
commands in the game console:
- bakeLightGrids
- bakeEnvironmentProbes

%prep
%setup -q -c -n doom3bfg

%install
mkdir -p %{buildroot}%{_datadir}/doom3bfg/
cp -fr base %{buildroot}%{_datadir}/doom3bfg/

%files
%{_datadir}/doom3bfg/base/*

%changelog
* Wed Jun 28 2023 Simone Caronni <negativo17@gmail.com> - 1.3.0-1
- First build.
