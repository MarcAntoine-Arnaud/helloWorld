EnsureSConsVersion(2, 3, 0)

import os
import sys
import ConfigParser

buildMode = ARGUMENTS.get('mode', 'release')
#lib_python = ARGUMENTS.get('lib_python', 'python2.7')
incdir_python = ARGUMENTS.get('incdir_python', '')
installPrefix = ARGUMENTS.get('prefix', '/usr/local')

if not (buildMode in ['debug', 'release']):
    print "Error: expected 'debug' or 'release', found: " + buildMode
    Exit(1)

env     = Environment().Clone()
envPy   = Environment().Clone()

# C++ environment
env.Append(
    CPPPATH = [
        "#src",
    ],
    CXXFLAGS = [
        '-Wall',
        '-fPIC',
    ],
    LIBPATH = [
        "#src",
        "#build/src"
    ],
)

# Python environment
envPy.Replace(
    CPPPATH = [
        incdir_python,
        ".",
    ],
    SWIGCXXFILESUFFIX= '_wrapPython$CXXFILESUFFIX',
    SHLIBPREFIX= '_',
    CXXFLAGS = [
        '-Wall',
    ],
    SWIGFLAGS = [
        '-python',
        '-c++',
        '-fcompact',
    ],
    LIBPATH = [
        "#src",
    ],
)

envPy.Append( SWIGPATH = envPy['CPPPATH'] )

Export( "env" )
Export( "envPy" )
Export( "installPrefix" )

VariantDir( 'build/'+buildMode+'/src', 'src', duplicate = 0 )
VariantDir( 'build/'+buildMode+'/app', 'app', duplicate = 0 )

sconscripts = [
    'build/src/SConscript',
    'build/app/SConscript',
]
 
SConscript('src/SConscript', variant_dir='build/'+buildMode+'/src')
SConscript('app/SConscript', variant_dir='build/'+buildMode+'/app')

