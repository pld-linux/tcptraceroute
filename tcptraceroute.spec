Summary:	A traceroute implementation using TCP packets
Name:		tcptraceroute
Version:	1.2
Release:	1
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
URL:		http://michael.toren.net/code/tcptraceroute/
Source0:	http://michael.toren.net/code/tcptraceroute/%{name}-%{version}.tar.gz
BuildRequires:	libnet-devel
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
The more traditional traceroute(8) sends out either UDP or ICMP ECHO
packets with a TTL of one, and increments the TTL until the
destination has been reached. By printing the gateways that generate
ICMP time exceeded messages along the way, it is able to deter­ mine
the path packets are taking to reach the destination. It is a very
useful network diagnostic tool.

The problem is that with the widespread use of firewalls on the modern
Internet, many of the packets that traceroute(8) sends out end up
being filtered, making it impossible to completely trace the path to
the destination. However, in many cases, these fire­ walls will permit
inbound TCP packets to specific ports that hosts sitting behind the
firewall are listening for connections on. By sending out TCP SYN
packets instead of UDP or ICMP ECHO packets, tcptraceroute is able to
bypass the most common firewall fil­ ters.

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
