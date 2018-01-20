import spinner
import outcome
import bin_stuff
banana = spinner.Spinner()
ba = bin_stuff.BinBuilder()
ba.corner(banana)
bin_stuff.print_bin(banana._bins)
#print banana._bins