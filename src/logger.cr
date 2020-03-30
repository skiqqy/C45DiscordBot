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
end

startServer("listen.sock")