from shutil import copy

copy('zestpkg/site.db','zestpkg/static/backup')
print("Backup done!")
