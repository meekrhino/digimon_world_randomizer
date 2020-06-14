# Author: Tristan Challener <challenert@gmail.com>
# Copyright: please don't steal this that is all

import os

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
        self.file = None

        if( self.filename is not None ):
            with open( self.filename, 'w' ):
                self.logAlways( self.getHeader( 'Digimon World Randomization Log' ) )
                self.logAlways( 'Logging mode is set to \'' + verbose + '\'' )

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

        self.error = True
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
        self.close()
        exit()


    def close( self ):
        """
        Close the logging file.
        """

        self.logAlways( self.getHeader( 'End of Log' ) )
        if( self.file is not None ):
            self.file.close()


    def rename( self, newName ):
        """
        Close the logging file.

        Keyword arguments:
        newName -- New name of file
        """

        os.rename( self.filename, newName )


    def logAlways( self, str ):
        """
        Write string to log file (or console) regardless
        of verbosity settings.

        Keyword arguments:
        str -- String to write
        """

        if( self.filename is not None ):
            if( self.file is None ):
                self.file = open( self.filename, 'a' )
            self.file.write( str + '\n' )
        else:
            print( str )


    def getHeader( self, str ):
        """
        Return a log header for the specified section name.

        Keyword arguments:
        str -- Section name
        """

        out = '\n============================================================\n'
        out += '   ' + str + '\n'
        out += '============================================================\n'

        return out