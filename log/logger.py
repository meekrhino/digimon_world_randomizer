# Author: Tristan Challener <challenert@gmail.com>
# Copyright: TODO

"""
Utilities for manipulating digimon data.
"""


class Logger:
    """
    Randomization and ROM handler logging interface.
    """

    def __init__( self, verbose, filename=None ):
        """
        Intialize verbosity.

        Keyword arguments:
        verbose -- Print all information?
        """

        self.error = False

        self.filename = filename
        if( self.filename is not None ):
            with open( self.filename, 'w' ) as file:
                file.write( 'Digimon World Randomization Log\n\n' )

        self.verbose = verbose


    def log( self, str ):
        """
        Write string to log file (or console) if in verbose
        mode.

        Keyword arguments:
        str -- String to write
        """

        if( self.verbose ):
            self.logAlways( str )


    def logAlways( self, str ):
        """
        Write string to log file (or console) regardless
        of verbosity settings.

        Keyword arguments:
        str -- String to write
        """

        if( self.filename is not None ):
            with open( self.filename, 'a' ) as file:
                file.write( str + '\n' )
        else:
            print( str )


    def logError( self, str ):
        """
        Write string to log file (or console) regardless
        of verbosity settings and mark error.

        Keyword arguments:
        str -- Error string to write
        """

        error = True
        self.logAlways( str )
