Summary:	A free Open Source 2D MMORPG
Summary(pl):	Darmowa gra typu MMORPG 2D
Name:		tmw
Version:	0.0.19
Release:	2
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/themanaworld/%{name}-%{version}.tar.gz
# Source0-md5:	b142f603c75819a04ac50d876776e92b
URL:		http://themanaworld.org/
BuildRequires:	curl-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	guichan-devel
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

%description -l pl
The Mana World (TMW) to powa¿na próba stworzenia innowacyjnej darmowej
gry MMORPG z otwartymi ¼ród³ami. TMW u¿ywa grafiki 2D i ma stworzyæ
du¿y i ró¿norodny interaktywny ¶wiat. Jest licencjonowana na warunkach
GPL, dziêki czemu nigdy nie zostanie zabrana.

Projekt obejmuje rozwój zarówno klienta jak i serwera, a tak¿e
tworzenie ¶wiata online. Aktualnie s± tworzone wydania alpha klienta,
natomiast serwer jest we wczesnym etapie rozwoju. Do czasu osi±gniêcia
dojrza³o¶ci serwera TMW u¿ywany jest darmowy serwer eAthena Ragnarok
Online.

%prep
%setup -q

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/tmw
%{_desktopdir}/tmw.desktop
%{_pixmapsdir}/*
