Summary:	A traceroute implementation using TCP packets
Summary(pl):	Implementacja traceroute u�ywaj�ca pakiet�w TCP
Summary(uk):	tcptraceroute - �� ���̦��æ� traceroute �� ��������� TCP ����Ԧ�
Summary(ru):	tcptraceroute - ��� ���������� traceroute ��� ������ TCP �������
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
Bardziej tradycyjne traceroute(8) wysy�aj� pakiety UDP lub ICMP ECHO z
TTL r�wnym jeden, i zwi�kszaj� TTL do osi�gni�cia celu. Wypisuj�c
bramki po drodze generuj�ce komunikaty ICMP time exceeded, umo�liwiaj�
okre�lenie drogi pakiet�w. S� to bardzo przydatne narz�dzia do
diagnostyki sieci.

Problemem jest rozpowszechnienie firewalli we wsp�czesnym Internecie,
wiele pakiet�w wysy�anych przez traceroute(8) jest filtrowana,
uniemo�liwiaj�c ca�kowite prze�ledzenie drogi do celu. Jednak w wielu
przypadkach, te firewalle przepuszczaj� przychodz�ce pakiety TCP na
okre�lone porty, na kt�rych s�uchaj� maszyny za firewallem. Poprzez
wysy�nie pakiet�w TCP SYN zamiast UDP czy ICMP ECHO, tcptraceroute
mo�e omin�� wi�kszo�� firewalli filtruj�cych.

%description -l uk
������� ����, �� tcptraceroute �������� TCP SYN ������ ��ͦ��� UDP
�� ICMP ECHO ����Ԧ�, צ� ���� ��������� ����� ���¦��� �����
�����������Φ Ʀ����� ͦ���������� ����Φ� (firewalls).

%description -l ru
��������� ����, ��� tcptraceroute �������� TCP SYN ������ ������ UDP
��� ICMP ECHO �������, �� ����� ��������� ����� �������� �����
������������ ������� ���������� ������� (firewalls).

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
