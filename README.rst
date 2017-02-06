py-mailqueued
=============

py-mailqueued is an ansynchronous daemon for sending or queueing mail,
depending on the state of the network. It's primary advantage is that it always
sends mail immediately if the network is up, and queues only if the network is
down.

It currently only supports using NetworkManager over dbus to query the network
status. This has the advantage that most Linux desktop/laptop setups use
NetworkManager and dbus, and isn't bound to silly tricks like pinging (which
make be blocked by a proxy or firewall) or resolving a hostname (which is
not guaranteed to work). It also means that the daemon switches modes as soon
as NetworkManager switches to or from full network access. The downide is of
course that NetworkManager must be managing all of your network interfaces.

Usage
=====

This package requires systemd to run. You're welcome to use it without systemd,
but I'm not intrested in supporting any other init system. Sorry.

This package also requires that you use NetworkManager. This should cover most
systems that realistically need a mail-queueing daemon. I might take patches to
support other clients if they have dbus interfaces.

This first thing you'll need to do is enable the daemon:

.. code-block:: sh

    systemctl --user daemon-reload
    systemctl --user start mailqueued
    systemctl --user enable mailqueued

Once that's done add 'mail-queue' to the front of your normal mailer command
(tested with msmtp):

.. code-block:: sh

    /bin/mail-queue /bin/msmtp --account=myaccount -t

And that's it. Mail will be sent when generated if the network is up, and
queued when it is not
