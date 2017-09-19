module fastsocket {
    requires socket;
    provides com.socket.spi.NetworkSocketProvider
        with org.fastsocket.FastNetworkSocketProvider;
}