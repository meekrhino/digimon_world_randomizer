# Author: Tristan Challener <challenert@gmail.com>
# Copyright: please don't steal this that is all

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
                file.write( 'Logging mode is set to \'' + verbose + '\'\n\n' )

        self.verbose = verbose


    def log( self, str ):
        """
        Write string to log file (or console) only if verbose
        mode is set to full.

        Keyword arguments:
        str -- String to write
        """

        if( self.verbose == 'full' ):
            self.logAlways( str )


    def logChange( self, str ):
        """
        Write string to log file (or console) if verbose
        mode is set to casual or full.

        Keyword arguments:
        str -- String to write
        """

        if( self.verbose == 'full' or self.verbose == 'casual' ):
            self.logAlways( str )


    def logError( self, str ):
        """
        Write string to log file (or console) regardless
        of verbosity settings and mark error.

        Keyword arguments:
        str -- Error string to write
        """

        error = True
        self.logAlways( str )


    def fatalError( self, str ):
        """
        Write string to log file (or console) regardless
        of verbosity settings and mark error.

        Keyword arguments:
        str -- Error string to write
        """

        self.logError( str )
        print( 'Program ended with errors.  See log file for errors.' )
        exit()


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
