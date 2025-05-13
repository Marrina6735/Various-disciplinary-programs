# Bayram Tagiev
#
# Starting simulation

for {set r 0} {$r < $n} {incr r} {
	$ns at 0.0 "$ftp($r) start"
	$ns at 1.0 "plotwindow $tcp(0) $windowvstime"
	$ns at 20.0 "$ftp($r) stop"
}

$ns at 21.0 "finish"
