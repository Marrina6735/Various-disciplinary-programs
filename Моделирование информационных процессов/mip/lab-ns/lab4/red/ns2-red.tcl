# Bayram Tagiev
#
# main file

set ns [new Simulator]

set nf [open out.nam w]
$ns namtrace-all $nf



source "nodes.tcl"
source "queue.tcl"
source "plotWindow.tcl"
source "modeling.tcl"
source "finish.tcl"



$ns run

