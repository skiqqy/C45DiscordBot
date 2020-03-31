# This is a logging server written in crystal
#
# Only accepts one connection, why? Cause I'm not going
# to write concurrent code in Crystal and spend my time
# shoving scheduler yields between every 10 lines, nah
# fam, I'm about that lean life.

require "socket"

def startServer(path : String)
	print("Starting UNIX domain socket server on \"" + path + "\"...\n");

	socket = Socket.new(Socket::Family::UNIX, Socket::Type::RAW);
	socket.bind(Socket::UNIXAddress.new(path))

	while true
		print("Waiting for a datagram to arrive...\n");

		# No peak mode so we have a size datagram, we read 4 bytes
		# Size will be interpreted as Int via little-endian decoding
		# (and therefore encoding on the client side (Python))
		datagramMessageSizeBytes = Slice(UInt8).new(4);
		print(UInt8.to_s()+"\n");
		print(UInt8.class.to_s()+"\n");
		size = IO::ByteFormat::LittleEndian.decode(UInt32, datagramMessageSizeBytes)
		print("Next datagram size to be: " + size.to_s() + "\n");
		
		
		
		print("Datagram arrived and cycle finished.\n");
	end
end

startServer("./listen.sock")