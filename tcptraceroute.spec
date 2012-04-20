%define		subver	beta4
%define		rel		4
Summary:	A traceroute implementation using TCP packets
Summary(pl.UTF-8):	Implementacja traceroute używająca pakietów TCP
Summary(ru.UTF-8):	tcptraceroute - это реализация traceroute при помощи TCP пакетов
Summary(uk.UTF-8):	tcptraceroute - це реалізація traceroute за допомогою TCP пакетів
Name:		tcptraceroute
Version:	1.5
Release:	0.%{subver}.%{rel}
License:	GPL v2
Group:		Applications/Networking
Source0:	http://michael.toren.net/code/tcptraceroute/%{name}-%{version}%{subver}.tar.gz
# Source0-md5:	d9068b69154515aced634d7000fe9675
URL:		http://michael.toren.net/code/tcptraceroute/
BuildRequires:	automake
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

%description -l pl.UTF-8
Bardziej tradycyjne traceroute(8) wysyłają pakiety UDP lub ICMP ECHO z
TTL równym jeden, i zwiększają TTL do osiągnięcia celu. Wypisując
bramki po drodze generujące komunikaty ICMP time exceeded, umożliwiają
określenie drogi pakietów. Są to bardzo przydatne narzędzia do
diagnostyki sieci.

Problemem jest rozpowszechnienie firewalli we współczesnym Internecie,
wiele pakietów wysyłanych przez traceroute(8) jest filtrowana,
uniemożliwiając całkowite prześledzenie drogi do celu. Jednak w wielu
przypadkach, te firewalle przepuszczają przychodzące pakiety TCP na
określone porty, na których słuchają maszyny za firewallem. Poprzez
wysyłnie pakietów TCP SYN zamiast UDP czy ICMP ECHO, tcptraceroute
może ominąć większość firewalli filtrujących.

%description -l uk.UTF-8
Завдяки тому, що tcptraceroute надсилає TCP SYN пакети замість UDP чи
ICMP ECHO пакетів, він може проходити через найбільш часто
встановлювані фільтри міжмережевих екранів (firewalls).

%description -l ru.UTF-8
Благодаря тому, что tcptraceroute посылает TCP SYN пакеты вместо UDP
или ICMP ECHO пакетов, он может проходить через наиболее часто
используемые фильтры межсетевых экранов (firewalls).

%prep
%setup -q -n %{name}-%{version}%{subver}

%build
cp -f /usr/share/automake/config.sub .
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
