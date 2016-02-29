#!/usr/bin/python

#----------------------------------------------------------#
# Developer : Jose Mari Caballa Rey                        #
# Project Name: lampin.py                                  #
# Description: to develop a python based script install    #
#              for lamp server installer for Ubuntu 14.00. #
# Version: 1.0                                             #
# Date Started: 27 February 2016                           #
# Date Updated: 28 February 2016                           #
#               29 February 2016                           #
#----------------------------------------------------------#

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
                def apache_function():
                        print '''
|------------------------------------------------------------|
| Select the following (press 'ctrl + c' exit the program ): |
| 1 - install apache 2                                       |
| 2 - update  apache 2                                       |
| 3 - remove  apache 2                                       |
| back - go to main menu                                     |
|------------------------------------------------------------|
                        '''
                        switch_apache = raw_input("\033[1;36mapache: select > \033[1;m")
                        if switch_apache == "1":
                                cmd = os.system("apt-get install apache2")
                        elif switch_apache == "2":
                                cmd = os.system("apt-get update apache2")
                        elif switch_apache == "3":
                                cmd = os.system("apt-get remove apache2")
                        elif switch_apache == "back" or switch_apache == "BACK":
                                mainmenu_function()
                        else:
                                print "\033[1;31m 0000 Invalid Command! 0000 \033[1;m"
                        apache_function()
                        
                def mysql_function():
                        print '''
|------------------------------------------------------------|
| Select the following (press 'ctrl + c' exit the program ): |
| 1 - install mysql                                          |
| 2 - update  mysql                                          |
| 3 - remove  mysql                                          |
| back - go to main menu                                     |
|------------------------------------------------------------|
                        '''
                        switch_mysql = raw_input("\033[1;36mmysql: select > \033[1;m")
                        if switch_mysql == "1":
                                cmd = os.system("apt-get install mysql-server php5-mysql")
                        elif switch_mysql == "2":
                                cmd = os.system("apt-get update mysql-server php5-mysql")
                        elif switch_mysql == "3":
                                cmd = os.system("apt-get remove mysql-server php5-mysql")
                        elif switch_mysql == "back" or switch_mysql == "BACK":
                                mainmenu_function()
                        else:
                                print "\033[1;31m 0000 Invalid Command! 0000 \033[1;m"
                        mysql_function()
                        
                def php_function():
                        print '''
|------------------------------------------------------------|
| Select the following (press 'ctrl + c' exit the program ): |
| 1 - install php5                                           |
| 2 - install php7                                           |
| back - go to main menu                                     |
|------------------------------------------------------------|
                        '''
                        switch_php = raw_input("\033[1;36mphp: select > \033[1;m")
                        if switch_php == "1":
                                cmd = os.system("apt-get install php5 libapache2-mod-php5 php5-mcrypt")
                        elif switch_php == "2":
                                print "\033[1;31m 0000 To be updated soon! 0000 \033[1;m"
                        elif switch_php == "back" or switch_php == "BACK":
                                mainmenu_function()
                        else:
                                print "\033[1;31m 0000 Invalid Command! 0000 \033[1;m"
                        php_function()

                def help_function():
                        print '''
|---------------------------------------------------------------------------------------------|
| How to used LAMPIN (Linux, Apache, MySQL and PHP Installer Kit)                             |
|                                                                                             |
| SCRIPT INSTALLATION                                                                         |
|   - sudo su                                                                                 |
|   - git clone https://github.com/reyjmc03/lampin.git && cp lampin/lampin.py /usr/bin/lampin |
|   - chmod +x /usr/bin/lampin                                                                |
|   - sudo lampin                                                                             |
|                                                                                             |
| LAMP Installation                                                                           |
|`  - just select the number of a tool to install it                                          |
|    - back: go to main menu                                                                  |
|---------------------------------------------------------------------------------------------|
                        '''
                        switch_help = raw_input("\033[1;36mhelp: select > \033[1;m")
                        if switch_help == "back" or switch_help == "BACK":
                                mainmenu_function()
                        else:
                                print "\033[1;31m 0000 Invalid Command! 0000 \033[1;m"
                        help_function()
                        
                def about_function():
                        print '''
|-------------------------------------------------------------|
| About LAMPPIN (Linux, Apache, MySQL, and PHP Installer Kit) |
| Created by Jose Mari Rey                                    |
| Contact Me @                                                |
|        - Website : http://www.jomarrey.com                  |
|        - Facebook : https://facebook.com/jomarrey03         |
|        - Email : reyjmc03@gmail.com                         |
|                                                             |
| press 'ctrl + c' exit the program                           |
| back - go to main menu                                      |
|-------------------------------------------------------------|
                        '''
                        switch_about = raw_input("\033[1;36mabout: select > \033[1;m")
                        if switch_about == "back":
                                mainmenu_function()
                        else:
                                print "\033[1;31m 0000 Invalid Command! 0000 \033[1;m"
                        about_function()
                        
		def mainmenu_function():
			while True:
				print '''
|------------------------------------------------------------|
| Select the following (press 'ctrl + c' exit the program ): |
| 1 - apt-get Update repositories                            |
| 2 - Install or Remove Apache2                              |
| 3 - Install or Remove MySql                                |
| 4 - Install PHP                                            |
| 5 - Help                                                   |
| 6 - About                                                  |
|------------------------------------------------------------|
			'''
				switch_main = raw_input("\033[1;36mmain: select > \033[1;m")
			
				if switch_main == "1":
                                        command = os.system("apt-get update")
                                elif switch_main == "2":
                                        apache_function()
                                elif switch_main == "3":
                                        mysql_function()
                                elif switch_main == "4":
                                        php_function()
                                elif switch_main == "5":
                                        help_function()
                                elif switch_main == "6":
                                        about_function()      
                                else:
                                        print "\033[1;31m 0000 Invalid Command! 0000 \033[1;m"
					
		mainmenu_function()
	except KeyboardInterrupt:
		print '''
\033[1;31mGoodbye .. Thank you!!! :) \033[1;m
'''
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)


if __name__ == "__main__":
    main()
