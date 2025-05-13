# finish procedure
#
# Generates necesery files
# Loads xgraph to render graphs


proc finish {} {
   global ns nf
   $ns flush-trace
   close $nf
   global tchan_
   set awkCode {
      {
	 if ($1 == "Q" && NF>2) {
	    print $2, $3 >> "temp.q";
	    set end $2
	 }
	 else if ($1 == "a" && NF>2)
	 print $2, $3 >> "temp.a";
      }
   }

   set f [open temp.queue w]
   puts $f "TitleText: RED"
   puts $f "Device: Postscript"

   if { [info exists tchan_] } {
      close $tchan_
   }

   exec rm -f temp.q temp.a
   exec touch temp.a temp.q

   exec awk $awkCode all.q

   puts $f \"queue
   exec cat temp.q >@ $f
   puts $f \n\"ave_queue
   exec cat temp.a >@ $f
   close $f

   exec xgraph -bb -tk -x time -t "TCPRenoCWND" wvst &
   exec xgraph -bb -tk -x time -y queue temp.queue &
   exec nam out.nam &
   exit 0
}
