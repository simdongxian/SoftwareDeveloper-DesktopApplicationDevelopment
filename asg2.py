# Refactor code
# -------------
# Not timed (good to get it back within 24 hours)
#
# An intern has provided the code below to update the version number
# within two different files.
# The intern has left and you need to review and improve the code before
# submitting to source control.
#
# Please do not be constrained by the existing code (i.e. you don't have
# to keep the same function names, structure)
# Aim for production quality 'best-practice/clean' code
#
# Original Requirements
# ---------------------
# A script in a build process needs to update the build version number in 2
# locations.
# - The version number will be in an environment variable "BuildNum"
# - The files to be modified will be under "$SourcePath/develop/global/src"
# directory
# - The "SConstruct" file has a line "point=123," (where 123
# (just an example) should be updated with the value of "BuildNum"
# Environment variable)
# - The "VERSION"file has a line "ADLMSDK_VERSION_POINT= 123" (where 123
# (just an example) should be updated with the value of "BuildNum"
# Environment variable)


# SCONSTRUCT file interesting lines
# config.version = Version(
# major=15,
# minor=0,
# point=6,
# patch=0
#)

# VERSION file interesting line
# ADLMSDK_VERSION_POINT=6

import os
import re

def updateFileVersion(source_path, build_num, fileName, search_title):
    base_path = os.path.join(source_path, "develop", "global", "src", fileName)
    temp_path = os.path.join(source_path, "develop", "global", "src", fileName + "1" )

    os.chmod(base_path, 0o755)
    fin = open(base_path, 'r')
    fout = open(temp_path, 'w')

    for line in fin:
        line=re.sub(search_title + "=[\d]+", search_title + "=" + build_num, line)
        fout.write(line)
    fin.close()
    fout.close()

    os.remove(base_path)
    os.rename(temp_path, base_path)

def updateBuildVersion(source_path, build_num):
    config_title = {
        "SConstruct": "point",
        "VERSION": "ADLMSDK_VERSION_POINT"
    }

    updateFileVersion(source_path, build_num, "SConstruct", config_title["SConstruct"])
    updateFileVersion(source_path, build_num, "VERSION", config_title["VERSION"])

def main():
    build_num = os.environ.get("BuildNum")
    source_path = os.environ.get("SourcePath")
  
    if not build_num or not source_path:
        raise EnvironmentError("Missing 'BuildNum' or 'SourcePath' environment variables.")

    updateBuildVersion(source_path, build_num)


main()