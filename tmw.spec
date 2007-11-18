%bcond_without	opengl	#disable OpenGL support
Summary:	A free Open Source 2D MMORPG
Summary(pl.UTF-8):	Darmowa gra typu MMORPG 2D
Name:		tmw
Version:	0.0.23
Release:	2
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/themanaworld/%{name}-%{version}.tar.gz
# Source0-md5:	4c4233a3b904dcf2935685e5ec1e6e5a
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-OpenGL.patch
Patch2:		%{name}-guichan.patch
URL:		http://themanaworld.org/
%{?with_opengl:BuildRequires:	OpenGL-devel}
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	curl-devel
BuildRequires:	guichan-devel >= 0.7.0
BuildRequires:	libxml2-devel
BuildRequires:	physfs-devel
BuildRequires:	pkgconfig
# should be autodetected
Requires:	curl
Requires:	SDL_image
Requires:	SDL_mixer
Requires:	SDL_net
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
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_opengl:--with-opengl}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/tmw
%{_desktopdir}/tmw.desktop
%{_mandir}/man6/%{name}.6*
%{_pixmapsdir}/*
