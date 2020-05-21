#############################
#                           #
#   DFIRTrack config file   #
#                           #
#############################

from os.path import expanduser

# SETTINGS

# MAIN APP SETTINGS (dfirtrack.settings)
## change path for the log file (default: `$HOME`)
LOGGING_PATH = expanduser('~')
## change path for the markdown documentation
MARKDOWN_PATH = ''

# decide whether the system name should be editable or not in system form to avoid accidentally corruption (admin can edit it either way)
SYSTEM_NAME_EDITABLE = False

# ARTIFACTS
EVIDENCE_PATH = expanduser('~') + '/dfirtrack_artifact_storage'

# EXPORTER

# SPREADSHEET (CSV and XLS)

# choose optional system attributes to export to spreadsheet
SPREAD_SYSTEM_ID = True
SPREAD_DNSNAME = True
SPREAD_DOMAIN = True
SPREAD_SYSTEMSTATUS = True
SPREAD_ANALYSISSTATUS = False
SPREAD_REASON = False
SPREAD_RECOMMENDATION = False
SPREAD_SYSTEMTYPE = True
SPREAD_IP = True
SPREAD_OS = False
SPREAD_COMPANY = False
SPREAD_LOCATION = False
SPREAD_SERVICEPROVIDER = False
SPREAD_TAG = True
SPREAD_CASE = False
SPREAD_SYSTEM_CREATE_TIME = True
SPREAD_SYSTEM_MODIFY_TIME = True

# IMPORTER

# IMPORT SYSTEMS AND ENTRIES VIA GIRAF API (dfirtrack_main.importer.api.giraf)
## add an url for giraf (e. g. 'https://giraf.testing.vm')
GIRAF_URL = ''
## add an user for giraf api
GIRAF_USER = ''
## add a password for giraf api user
GIRAF_PASS = ''

# IMPORT SYSTEMS FROM CLIENT CSV FILE (dfirtrack_main.importer.file.csv.system)

# CSV contains a headline (True) or not (False)
CSV_HEADLINE = True
# skip (True) or not (False) systems, that already exist
CSV_SKIP_EXISTING_SYSTEM = True

# ip should be set via CSV column (True) or not at all (False) (import via web form not possible for multiple systems)
CSV_CHOICE_IP = True

# column of system rather system_name (numerical value starting with 0 [zero] for first column)
CSV_COLUMN_SYSTEM = 0
# column of ip address (numerical value starting with 0 [zero] for first column) (only used if CSV_CHOICE_IP is set to True)
CSV_COLUMN_IP = 1

# attribute should be set via this config (True) or via web form (False) during import
CSV_CHOICE_SYSTEMSTATUS = True
CSV_CHOICE_ANALYSISSTATUS = True
CSV_CHOICE_REASON = False
CSV_CHOICE_DOMAIN = False
CSV_CHOICE_DNSNAME = False
CSV_CHOICE_SYSTEMTYPE = False
CSV_CHOICE_OS = False
CSV_CHOICE_LOCATION = False
CSV_CHOICE_SERVICEPROVIDER = False

# attributes with fixed values (used if CSV_CHOICE_... is set to True)

# 'Systemstatus' for imported systems (choose from 'Clean', 'Unknown', 'Analysis ongoing', 'Compromised', 'Remediation done', 'Reinstalled', 'Removed', 'Not analyzed' or your custom values)
CSV_DEFAULT_SYSTEMSTATUS = 'Unknown'
# 'Analysisstatus' for imported systems (choose from 'Needs analysis', 'Ready for analysis', 'Ongoing analysis', 'Nothing to do', 'Main analysis finished' or your custom values)
CSV_DEFAULT_ANALYSISSTATUS = 'Needs analysis'

# attributes with chooseable values (choose string for attribute name, non-existing attributes will be created)
CSV_DEFAULT_REASON = 1
CSV_DEFAULT_DOMAIN = 1
CSV_DEFAULT_DNSNAME = 1
CSV_DEFAULT_SYSTEMTYPE = 1
CSV_DEFAULT_OS = 1
CSV_DEFAULT_LOCATION = 1
CSV_DEFAULT_SERVICEPROVIDER = 1

# IMPORT SYSTEMS WITH TAGS FROM CLIENT CSV FILE (dfirtrack_main.importer.file.csv.systems_tags)
## add a list of strings representing the relevant tags you want to automatically import
TAGLIST = []
## add a string used as prefix for clearly identifying previously automatically imported tags (e. g. "AUTO" leads to "AUTO_TAG")
TAGPREFIX = ''
## add a headline for the systems to import by tags
SYSTEMTAG_HEADLINE = ''
## add a subheadline for the systems to import by tags
SYSTEMTAG_SUBHEADLINE = ''


# IMPORT REPORTITEMS FROM SERVER FILESYSTEM (dfirtrack_main.importer.file.filesystem.reportitems)
## add a server path (without trailing slash!) where reportitems (preferably in markdown syntax) are stored as <system_name>.md (lowercase!)
REPORTITEMS_FILESYSTEMPATH = ''
## add a headline for the reportitems to import
REPORTITEMS_HEADLINE = ''
## add a subheadline for the reportitems to import
REPORTITEMS_SUBHEADLINE = ''
## if 'True' the reportitem will be deleted from DFIRTrack if it disappears from the filesystem, change to 'False' to change this behaviour
REPORTITEMS_DELETE = True
