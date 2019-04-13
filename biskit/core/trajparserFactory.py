##
## Biskit, a toolkit for the manipulation of macromolecular structures
## Copyright (C) 2004-2018 Raik Gruenberg & Johan Leckner
##
## This program is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 3 of the
## License, or any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
## General Public License for more details.
##
## You find a copy of the GNU General Public License in the file
## license.txt along with this program; if not, write to the Free
## Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
##
##
"""
.. seealso:: `biskit.core.TrajParser`,`biskit.core.TrajParserNetCDF`,
"""

from biskit.core.trajparser import TrajParserError, TrajParser
from biskit.core.trajparseNetCDF import TrajParseNetCDF

class TrajParserFactory:
    """
    Provide the right PDBParser for different structure sources.
    """

    @staticmethod
    def getParser( source ):
        """
        getParser( source ) -> TrajParser; Fetch a Parser for the source.

        The method is static and should be called directly with the class::

           p = TrajParserFactory.getParser( 'myfile.crd' )

        Args:
            source (str or LocalPath): trajectory source (file)

        Returns:
            TrajParser: a parser that should be able to handle the given source

        Raises:
            TrajParserError: if no compatible parser is found
        """

        if TrajParseNetCDF.supports( source ):
            return TrajParseNetCDF()
            
        raise TrajParserError('Format of %r is not recognized.' % source)

#############
##  TESTING        
#############
import biskit.test as BT
        
class Test(BT.BiskitTest):
    """nothing to test"""
    pass
