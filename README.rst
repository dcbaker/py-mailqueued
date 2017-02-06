py-mailqueued
=============

py-mailqueued is an ansynchronous daemon for sending or queueing mail, depending on the state of the network. It's primary advantage is that it always send mail immediately if the network is up, and queues only if the network is down.

It currently only supports using NetworkManager over dbus to query the network status. This has the advantage that most Linux desktop/laptop setups use NetworkManager and dbus, and isn't bound to silly tricks like pinging (which make be blocked by a proxy or firewall) or resolving a hostname (which is expensive). It also means that the daemon switches modes as soon as NetworkManager switches to or from full network access. The downide is of course that NetworkManager must be managing all of your network interfaces.
