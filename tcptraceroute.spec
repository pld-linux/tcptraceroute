Summary:	A traceroute implementation using TCP packets
Summary(pl):	Implementacja traceroute u©ywaj╠ca pakietСw TCP
Summary(uk):	tcptraceroute - це реал╕зац╕я traceroute за допомогою TCP пакет╕в
Summary(ru):	tcptraceroute - это реализация traceroute при помощи TCP пакетов
Name:		tcptraceroute
Version:	1.5
%define	_pre	beta3
Release:	0.%{_pre}.2
License:	GPL
Group:		Applications/Networking
# Source0-md5:	f04c12e24e1755dbddd5df4f061b9a10
Source0:	http://michael.toren.net/code/tcptraceroute/%{name}-%{version}%{_pre}.tar.gz
Patch0:		%{name}-setuid.patch
URL:		http://michael.toren.net/code/tcptraceroute/
BuildRequires:	libnet-devel
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The more traditional traceroute(8) sends out either UDP or ICMP ECHO
packets with a TTL of one, and increments the TTL until the
destination has been reached. By printing the gateways that generate
ICMP time exceeded messages along the way, it is able to determine the
path packets are taking to reach the destination. It is a very useful
network diagnostic tool.

The problem is that with the widespread use of firewalls on the modern
Internet, many of the packets that traceroute(8) sends out end up
being filtered, making it impossible to completely trace the path to
the destination. However, in many cases, these firewalls will permit
inbound TCP packets to specific ports that hosts sitting behind the
firewall are listening for connections on. By sending out TCP SYN
packets instead of UDP or ICMP ECHO packets, tcptraceroute is able to
bypass the most common firewall filters.

%description -l pl
Bardziej tradycyjne traceroute(8) wysyЁaj╠ pakiety UDP lub ICMP ECHO z
TTL rСwnym jeden, i zwiЙkszaj╠ TTL do osi╠gniЙcia celu. Wypisuj╠c
bramki po drodze generuj╠ce komunikaty ICMP time exceeded, umo©liwiaj╠
okre╤lenie drogi pakietСw. S╠ to bardzo przydatne narzЙdzia do
diagnostyki sieci.

Problemem jest rozpowszechnienie firewalli we wspСЁczesnym Internecie,
wiele pakietСw wysyЁanych przez traceroute(8) jest filtrowana,
uniemo©liwiaj╠c caЁkowite prze╤ledzenie drogi do celu. Jednak w wielu
przypadkach, te firewalle przepuszczaj╠ przychodz╠ce pakiety TCP na
okre╤lone porty, na ktСrych sЁuchaj╠ maszyny za firewallem. Poprzez
wysyЁnie pakietСw TCP SYN zamiast UDP czy ICMP ECHO, tcptraceroute
mo©e omin╠Ф wiЙkszo╤Ф firewalli filtruj╠cych.

%description -l uk
Завдяки тому, що tcptraceroute надсила╓ TCP SYN пакети зам╕сть UDP
чи ICMP ECHO пакет╕в, в╕н може проходити через найб╕льш часто
встановлюван╕ ф╕льтри м╕жмережевих екран╕в (firewalls).

%description -l ru
Благодаря тому, что tcptraceroute посылает TCP SYN пакеты вместо UDP
или ICMP ECHO пакетов, он может проходить через наиболее часто
используемые фильтры межсетевых экранов (firewalls).

%prep
%setup -q -n %{name}-%{version}%{_pre}

%patch -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install %{name} $RPM_BUILD_ROOT%{_sbindir}
install %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS examples.txt README
%attr(4754,root,adm) %{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*
