<div align="center">

# quicksearch-module
#### 🔍 Python 模块/全局变量的方法模糊搜索
#### 🔍 Python fuzzy search for module/global variables

</div>

### 特性 | Features
- ✔ Python 3.1+ (兼容性好)
- ✔ 无第三方库依赖 (适合无网环境)
- ✔ 模糊搜索 是
  (编不下去了)

### 用法 | Usage
```commandline
Search> Exception.__
__cause__           
__class__           	__context__         	__delattr__         	__dict__            
__dir__             	__doc__             	__eq__              	__format__          
__ge__              	__getattribute__    	__gt__              	__hash__            
__init__            	__init_subclass__   	__le__              	__lt__              
__ne__              	__new__             	__reduce__          	__reduce_ex__       
__repr__            	__setattr__         	__setstate__        	__sizeof__          
__str__             	__subclasshook__    	__suppress_context__	__traceback__       

29 in set (0.0 sec)
Search> socket
AF_APPLETALK           
AF_BLUETOOTH           	AF_DECnet              	AF_INET                	AF_INET6               
AF_IPX                 	AF_IRDA                	AF_LINK                	AF_SNA                 
AF_UNSPEC              	AI_ADDRCONFIG          	AI_ALL                 	AI_CANONNAME           
AI_NUMERICHOST         	AI_NUMERICSERV         	AI_PASSIVE             	AI_V4MAPPED            
AddressFamily          	AddressInfo            	BDADDR_ANY             	BDADDR_LOCAL           
BTPROTO_RFCOMM         	CAPI                   	EAGAIN                 	EAI_AGAIN              
EAI_BADFLAGS           	EAI_FAIL               	EAI_FAMILY             	EAI_MEMORY             
EAI_NODATA             	EAI_NONAME             	EAI_SERVICE            	EAI_SOCKTYPE           
EBADF                  	EWOULDBLOCK            	INADDR_ALLHOSTS_GROUP  	INADDR_ANY             
INADDR_BROADCAST       	INADDR_LOOPBACK        	INADDR_MAX_LOCAL_GROUP 	INADDR_NONE            
INADDR_UNSPEC_GROUP    	IPPORT_RESERVED        	IPPORT_USERRESERVED    	IPPROTO_AH             
IPPROTO_CBT            	IPPROTO_DSTOPTS        	IPPROTO_EGP            	IPPROTO_ESP            
IPPROTO_FRAGMENT       	IPPROTO_GGP            	IPPROTO_HOPOPTS        	IPPROTO_ICLFXBM        
IPPROTO_ICMP           	IPPROTO_ICMPV6         	IPPROTO_IDP            	IPPROTO_IGMP           
IPPROTO_IGP            	IPPROTO_IP             	IPPROTO_IPV4           	IPPROTO_IPV6           
IPPROTO_L2TP           	IPPROTO_MAX            	IPPROTO_ND             	IPPROTO_NONE           
IPPROTO_PGM            	IPPROTO_PIM            	IPPROTO_PUP            	IPPROTO_RAW            
IPPROTO_RDP            	IPPROTO_ROUTING        	IPPROTO_SCTP           	IPPROTO_ST             
IPPROTO_TCP            	IPPROTO_UDP            	IPV6_CHECKSUM          	IPV6_DONTFRAG          
IPV6_HOPLIMIT          	IPV6_HOPOPTS           	IPV6_JOIN_GROUP        	IPV6_LEAVE_GROUP       
IPV6_MULTICAST_HOPS    	IPV6_MULTICAST_IF      	IPV6_MULTICAST_LOOP    	IPV6_PKTINFO           
IPV6_RECVRTHDR         	IPV6_RECVTCLASS        	IPV6_RTHDR             	IPV6_TCLASS            
IPV6_UNICAST_HOPS      	IPV6_V6ONLY            	IP_ADD_MEMBERSHIP      	IP_DROP_MEMBERSHIP     
IP_HDRINCL             	IP_MULTICAST_IF        	IP_MULTICAST_LOOP      	IP_MULTICAST_TTL       
IP_OPTIONS             	IP_RECVDSTADDR         	IP_TOS                 	IP_TTL                 
IntEnum                	IntFlag                	MSG_BCAST              	MSG_CTRUNC             
MSG_DONTROUTE          	MSG_ERRQUEUE           	MSG_MCAST              	MSG_OOB                
MSG_PEEK               	MSG_TRUNC              	MSG_WAITALL            	MsgFlag                
NI_DGRAM               	NI_MAXHOST             	NI_MAXSERV             	NI_NAMEREQD            
NI_NOFQDN              	NI_NUMERICHOST         	NI_NUMERICSERV         	RCVALL_MAX             
RCVALL_OFF             	RCVALL_ON              	RCVALL_SOCKETLEVELONLY 	SHUT_RD                
SHUT_RDWR              	SHUT_WR                	SIO_KEEPALIVE_VALS     	SIO_LOOPBACK_FAST_PATH 
SIO_RCVALL             	SOCK_DGRAM             	SOCK_RAW               	SOCK_RDM               
SOCK_SEQPACKET         	SOCK_STREAM            	SOL_IP                 	SOL_SOCKET             
SOL_TCP                	SOL_UDP                	SOMAXCONN              	SO_ACCEPTCONN          
SO_BROADCAST           	SO_DEBUG               	SO_DONTROUTE           	SO_ERROR               
SO_EXCLUSIVEADDRUSE    	SO_KEEPALIVE           	SO_LINGER              	SO_OOBINLINE           
SO_RCVBUF              	SO_RCVLOWAT            	SO_RCVTIMEO            	SO_REUSEADDR           
SO_SNDBUF              	SO_SNDLOWAT            	SO_SNDTIMEO            	SO_TYPE                
SO_USELOOPBACK         	SocketIO               	SocketKind             	SocketType             
TCP_FASTOPEN           	TCP_KEEPCNT            	TCP_KEEPIDLE           	TCP_KEEPINTVL          
TCP_MAXSEG             	TCP_NODELAY            	_GLOBAL_DEFAULT_TIMEOUT	_GiveupOnSendfile      
_LOCALHOST             	_LOCALHOST_V6          	__all__                	__builtins__           
__cached__             	__doc__                	__file__               	__loader__             
__name__               	__package__            	__spec__               	_blocking_errnos       
_intenum_converter     	_socket                	close                  	create_connection      
create_server          	dup                    	errno                  	error                  
errorTab               	fromfd                 	fromshare              	gaierror               
getaddrinfo            	getdefaulttimeout      	getfqdn                	gethostbyaddr          
gethostbyname          	gethostbyname_ex       	gethostname            	getnameinfo            
getprotobyname         	getservbyname          	getservbyport          	has_dualstack_ipv6     
has_ipv6               	herror                 	htonl                  	htons                  
if_indextoname         	if_nameindex           	if_nametoindex         	inet_aton              
inet_ntoa              	inet_ntop              	inet_pton              	io                     
ntohl                  	ntohs                  	os                     	selectors              
setdefaulttimeout      	socket                 	socketpair             	sys                    
timeout           
     	
226 in set (0.0 sec)
Search> socket.a
AF_APPLETALK  
AF_BLUETOOTH  	AF_DECnet     	AF_INET       	AF_INET6      
AF_IPX        	AF_IRDA       	AF_LINK       	AF_SNA        
AF_UNSPEC     	AI_ADDRCONFIG 	AI_ALL        	AI_CANONNAME  
AI_NUMERICHOST	AI_NUMERICSERV	AI_PASSIVE    	AI_V4MAPPED   
AddressFamily 	AddressInfo   	

19 in set (0.0 sec)
Search> q
Quit.
```
### 开源协议 | License
MIT

### 关于
在微机课没事干做的小东西, 方便轻量、快速搜索记不清的API
