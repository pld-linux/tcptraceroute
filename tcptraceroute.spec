Summary:	A traceroute implementation using TCP packets
Summary(pl):	Implementacja traceroute u¿ywaj±ca pakietów TCP
Name:		tcptraceroute
Version:	1.2
Release:	2
License:	GPL
Group:		Applications/Networking
Source0:	http://michael.toren.net/code/tcptraceroute/%{name}-%{version}.tar.gz
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
Bardziej tradycyjne traceroute(8) wysy³aj± pakiety UDP lub ICMP ECHO z
TTL równym jeden, i zwiêkszaj± TTL do osi±gniêcia celu. Wypisuj±c
bramki po drodze generuj±ce komunikaty ICMP time exceeded, umo¿liwiaj±
okre¶lenie drogi pakietów. S± to bardzo przydatne narzêdzia do
diagnostyki sieci.

Problemem jest rozpowszechnienie firewalli we wspó³czesnym Internecie,
wiele pakietów wysy³anych przez traceroute(8) jest filtrowana,
uniemo¿liwiaj±c ca³kowite prze¶ledzenie drogi do celu. Jednak w wielu
przypadkach, te firewalle przepuszczaj± przychodz±ce pakiety TCP na
okre¶lone porty, na których s³uchaj± maszyny za firewallem. Poprzez
wysy³nie pakietów TCP SYN zamiast UDP czy ICMP ECHO, tcptraceroute
mo¿e omin±æ wiêkszo¶æ firewalli filtruj±cych.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install %{name} $RPM_BUILD_ROOT%{_sbindir}
install %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf changelog examples.txt README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(4754,root,adm) %{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*
