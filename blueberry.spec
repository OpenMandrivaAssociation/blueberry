Name:           blueberry
Version:        1.3.4
Release:        1
Summary:        A configuration tool for Bluetooth
License:        GPLv3+
Group:          Communications/Bluetooth
Url:            https://github.com/linuxmint/blueberry
Source:         https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  hicolor-icon-theme
BuildRequires:  python
BuildRequires:  desktop-file-utils
Requires:       python-dbus
Requires:       python3dist(pygobject)
Requires:       python3dist(setproctitle)
Requires:       bluez-tools
Requires:       gnome-bluetooth >= 3.14
Requires:       rfkill
Recommends:       wmctrl

%description
Utility for Bluetooth devices graphical configuration.

%package -n cinnamon-applet-%{name}
Summary:        Cinnamon applet for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       cinnamon
Conflicts:      %{name} < 1.2.5-2

%description -n cinnamon-applet-%{name}
Cinnamon applet for %{name}.

%prep
%setup -q
%autopatch -p1

# Add execution bit to files in /usr/bin/ directory.
chmod a+x .%{_bindir}/* .%{_prefix}/lib/%{name}/*.py

# Replace the icon with an existing one.
sed -i 's/^\(Icon=\).*$/\1%{name}/' .%{_datadir}/applications/%{name}.desktop

%build
%make_build

%install
cp -a .%{_prefix} %{buildroot}%{_prefix}
cp -a .%{_sysconfdir} %{buildroot}%{_sysconfdir}

%find_lang %{name}

%files -f %{name}.lang
%doc debian/changelog debian/copyright README.md
%{_bindir}/%{name}*
%{_prefix}/lib/%{name}/
%{_sysconfdir}/xdg/autostart/*.desktop
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}*
%{_datadir}/glib-2.0/schemas/org.%{name}.gschema.xml

%files -n cinnamon-applet-%{name}
%{_datadir}/cinnamon/applets/blueberry@cinnamon.org/
