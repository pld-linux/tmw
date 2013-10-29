%bcond_without	opengl	#disable OpenGL support
Summary:	A free Open Source 2D MMORPG
Summary(pl.UTF-8):	Gra typu MMORPG 2D o otwartych źródłach
Name:		tmw
Version:	0.5.2
Release:	4
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/themanaworld/%{name}-%{version}.tar.bz2
# Source0-md5:	c843ef420aced82db1e51fa14e80174a
Patch0:		%{name}-desktop.patch
URL:		http://themanaworld.org/
%{?with_opengl:BuildRequires:	OpenGL-GLU-devel}
%{?with_opengl:BuildRequires:	OpenGL-devel}
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	guichan-devel >= 0.8.0
BuildRequires:	libpng-devel
BuildRequires:	libxml2-devel
BuildRequires:	physfs-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	SDL_image
Requires:	SDL_mixer
Requires:	SDL_net
# should be autodetected
Requires:	curl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Mana World (TMW) is a serious effort to create an innovative free
and open source MMORPG. TMW uses 2D graphics and aims to create a
large and diverse interactive world. It is licensed under the GPL,
making sure this game can't ever run away from you.

The project includes the development of both a client and a server, as
well as the development of an online world. At the moment we're making
alpha releases of the client, while our server is in early
development. The eAthena free software Ragnarok Online server is used
until our own server has matured enough to replace it. Once ready,
we'll be making releases of our server too so anybody will be free to
set up their own server and start building their own online world.

%description -l pl.UTF-8
The Mana World (TMW) to poważna próba stworzenia innowacyjnej darmowej
gry MMORPG z otwartymi źródłami. TMW używa grafiki 2D i ma stworzyć
duży i różnorodny interaktywny świat. Jest licencjonowana na warunkach
GPL, dzięki czemu nigdy nie zostanie zabrana.

Projekt obejmuje rozwój zarówno klienta jak i serwera, a także
tworzenie świata online. Aktualnie są tworzone wydania alpha klienta,
natomiast serwer jest we wczesnym etapie rozwoju. Do czasu osiągnięcia
dojrzałości serwera TMW używany jest darmowy serwer eAthena Ragnarok
Online.

%prep
%setup -q -c
%patch0 -p1

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/mana
%{_datadir}/mana
%{_desktopdir}/mana.desktop
%{_pixmapsdir}/mana.png
