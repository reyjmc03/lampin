#!/usr/bin/python

# --------------------------------------------------------------------------------------------------
# Developer : Jose Mari Caballa Rey
# Project Name: lampin.py
# Description: to develop a python based script install for lamp server installer for Ubuntu 14.00.
# Version: 1.0
# Date Started: 27 February 2016 
# Date Updated: 28 February 2016
# ---------------------------------------------------------------------------------------------------

import os
import sys, traceback

def main():
	try:
                print '''
##################################################################
------------------------------------------------------------------                      
  @@         @@@      @@@@      @@@@   @@@@@@,   @@.  @@@'    @@
  @@        '@@@+     @@@@     ,@@@@   @@@@@@@,` @@.  @@@@    @@ 
  @@        @@.@@     @@#@'    @@`@@   @@   @@@  @@.  @@@@@   @@ 
  @@        @@ @@`    @@ @@    @@`@@   @@   ;@@  @@.  @@`#@`  @@ 
  @@       +@; @@@    @@ @@   #@,`@@   @@   @@@  @@.  @@ @@@  @@ 
  @@       @@  .@@    @@ '@#  #@ `@@   @@  .@@'  @@.  @@ `@@  @@ 
  @@      `@@   @@    @@  @@ `@@ `@@   @@@@@@@   @@.  @@  @@@ @@ 
  @@      @@@@@@@@@   @@  @@`@@. `@@   @@@@@`    @@.  @@  `@@`@@ 
  @@      @@@@@@@@@   @@  '@@@@  `@@   @@        @@.  @@   @@@@@ 
  @@     `@@     @@`  @@   @@@#  `@@   @@        @@.  @@    @@@@ 
  @@@@@@ @@@     @@@  @@   @@@`  `@@   @@        @@.  @@   `@@@@ 
  @@@@@@ @@`     ,@@  @@   ;@@ ` `@@   @@        @@.  @@     @@@ 
------------------------------------------------------------------
##################################################################
------------------ LAMP Installer Command Script -----------------
##################################################################

		'''
                def apache():
                        print "apache ok!"
                        switch_about = raw_input("\033[1;36mapache: select > \033[1;m")
                        apache()
                        
                def mysql():
                        print "mysql ok!"
                        switch_about = raw_input("\033[1;36mmysql: select > \033[1;m")
                        mysql()
                        
                def php():
                        print "php ok!"
                        switch_about = raw_input("\033[1;36mphpt: select > \033[1;m")
                        php()
                        
                def about():
                        print "about ok!"
                        switch_about = raw_input("\033[1;36mabout: select > \033[1;m")
                        about()
                        
		def mainmenu():
			while True:
				print '''
|-----------------------------------|
| Select the following:             |
| 1) apt-get Update repositories    |
| 2) Install or Remove Apache2      |
| 3) Install or Remove MySql        |
| 4) Install PHP                    |
| 5) Help                           |
| 6) About                          |
|-----------------------------------|
			'''
				switch_main = raw_input("\033[1;36mmain: select > \033[1;m")
			
				if switch_main == "1":
                                        command = os.system("apt-get update")
                                elif switch_main == "2":
                                        apache()
                                elif switch_main == "3":
                                        print "ok"
                                elif switch_main == "4":
                                        print "ok"
                                elif switch_main == "5":
                                        print " 5ok"
                                elif switch_main == "6":
                                        about()      
                                else:
                                        print "---- Invalid Command! ----"
					
		mainmenu()
	except KeyboardInterrupt:
		print "Shutdown requested...Goodbye..."
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)


if __name__ == "__main__":
    main()
