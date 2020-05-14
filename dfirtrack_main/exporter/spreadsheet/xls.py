from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
import dfirtrack.config as dfirtrack_config
from dfirtrack_main.logger.default_logger import info_logger, warning_logger
from dfirtrack_main.models import Analysisstatus, Reason, Recommendation, System, Systemstatus, Tag
from time import strftime
import xlwt

def write_row(worksheet, content, row_num, style):
    """ write single row to worksheet """

    # write row depending on column number
    for col_num in range(len(content)):
        worksheet.write(row_num, col_num, content[col_num], style)

    # return worksheet object
    return worksheet


def style_headline():
    """ change style to headline """

    # define styling for headline
    style = xlwt.XFStyle()
    style = xlwt.easyxf(
        'font: bold on; alignment: horizontal center'
    )

    # return style object
    return style


def style_default():
    """ change style to default """

    # clear styling to default
    style = xlwt.XFStyle()
    style = xlwt.easyxf(
        'alignment: vertical top, horizontal left'
    )

    # return style object
    return style


@login_required(login_url="/login")
def system(request):


    """ check variables of dfirtrack.config """

    # reset stop condition
    stop_system_exporter_spreadsheet_xls = False

    # check SPREAD_SYSTEM_ID for bool
    if not isinstance(dfirtrack_config.SPREAD_SYSTEM_ID, bool):
        messages.error(request, "Deformed `SPREAD_SYSTEM_ID` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_SYSTEM_ID deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_DNSNAME for bool
    if not isinstance(dfirtrack_config.SPREAD_DNSNAME, bool):
        messages.error(request, "Deformed `SPREAD_DNSNAME` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_DNSNAME deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_DOMAIN for bool
    if not isinstance(dfirtrack_config.SPREAD_DOMAIN, bool):
        messages.error(request, "Deformed `SPREAD_DOMAIN` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_DOMAIN deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_SYSTEMSTATUS for bool
    if not isinstance(dfirtrack_config.SPREAD_SYSTEMSTATUS, bool):
        messages.error(request, "Deformed `SPREAD_SYSTEMSTATUS` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_SYSTEMSTATUS deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_ANALYSISSTATUS for bool
    if not isinstance(dfirtrack_config.SPREAD_ANALYSISSTATUS, bool):
        messages.error(request, "Deformed `SPREAD_ANALYSISSTATUS` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_ANALYSISSTATUS deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_REASON for bool
    if not isinstance(dfirtrack_config.SPREAD_REASON, bool):
        messages.error(request, "Deformed `SPREAD_REASON` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_REASON deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_RECOMMENDATION for bool
    if not isinstance(dfirtrack_config.SPREAD_RECOMMENDATION, bool):
        messages.error(request, "Deformed `SPREAD_RECOMMENDATION` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_RECOMMENDATION deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_SYSTEMTYPE for bool
    if not isinstance(dfirtrack_config.SPREAD_SYSTEMTYPE, bool):
        messages.error(request, "Deformed `SPREAD_SYSTEMTYPE` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_SYSTEMTYPE deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_IP for bool
    if not isinstance(dfirtrack_config.SPREAD_IP, bool):
        messages.error(request, "Deformed `SPREAD_IP` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_IP deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_OS for bool
    if not isinstance(dfirtrack_config.SPREAD_OS, bool):
        messages.error(request, "Deformed `SPREAD_OS` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_OS deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_COMPANY for bool
    if not isinstance(dfirtrack_config.SPREAD_COMPANY, bool):
        messages.error(request, "Deformed `SPREAD_COMPANY` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_COMPANY deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_LOCATION for bool
    if not isinstance(dfirtrack_config.SPREAD_LOCATION, bool):
        messages.error(request, "Deformed `SPREAD_LOCATION` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_LOCATION deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_SERVICEPROVIDER for bool
    if not isinstance(dfirtrack_config.SPREAD_SERVICEPROVIDER, bool):
        messages.error(request, "Deformed `SPREAD_SERVICEPROVIDER` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_SERVICEPROVIDER deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_TAG for bool
    if not isinstance(dfirtrack_config.SPREAD_TAG, bool):
        messages.error(request, "Deformed `SPREAD_TAG` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_TAG deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_CASE for bool
    if not isinstance(dfirtrack_config.SPREAD_CASE, bool):
        messages.error(request, "Deformed `SPREAD_CASE` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_CASE deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_SYSTEM_CREATE_TIME for bool
    if not isinstance(dfirtrack_config.SPREAD_SYSTEM_CREATE_TIME, bool):
        messages.error(request, "Deformed `SPREAD_SYSTEM_CREATE_TIME` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_SYSTEM_CREATE_TIME deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_SYSTEM_MODIFY_TIME for bool
    if not isinstance(dfirtrack_config.SPREAD_SYSTEM_MODIFY_TIME, bool):
        messages.error(request, "Deformed `SPREAD_SYSTEM_MODIFY_TIME` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_SYSTEM_MODIFY_TIME deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_WORKSHEET_SYSTEMSTATUS for bool
    if not isinstance(dfirtrack_config.SPREAD_WORKSHEET_SYSTEMSTATUS, bool):
        messages.error(request, "Deformed `SPREAD_WORKSHEET_SYSTEMSTATUS` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_WORKSHEET_SYSTEMSTATUS deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_WORKSHEET_ANALYSISSTATUS for bool
    if not isinstance(dfirtrack_config.SPREAD_WORKSHEET_ANALYSISSTATUS, bool):
        messages.error(request, "Deformed `SPREAD_WORKSHEET_ANALYSISSTATUS` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_WORKSHEET_ANALYSISSTATUS deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_WORKSHEET_REASON for bool
    if not isinstance(dfirtrack_config.SPREAD_WORKSHEET_REASON, bool):
        messages.error(request, "Deformed `SPREAD_WORKSHEET_REASON` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_WORKSHEET_REASON deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_WORKSHEET_RECOMMENDATION for bool
    if not isinstance(dfirtrack_config.SPREAD_WORKSHEET_RECOMMENDATION, bool):
        messages.error(request, "Deformed `SPREAD_WORKSHEET_RECOMMENDATION` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_WORKSHEET_RECOMMENDATION deformed")
        stop_system_exporter_spreadsheet_xls = True

    # check SPREAD_WORKSHEET_TAG for bool
    if not isinstance(dfirtrack_config.SPREAD_WORKSHEET_TAG, bool):
        messages.error(request, "Deformed `SPREAD_WORKSHEET_TAG` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS variable SPREAD_WORKSHEET_TAG deformed")
        stop_system_exporter_spreadsheet_xls = True

    # leave system_exporter_spreadsheet_xls if variables caused errors
    if stop_system_exporter_spreadsheet_xls:

        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_XLS_END_WITH_ERRORS")
        return redirect(reverse('system_list'))


    """ prepare file including formatting """

    # create xls MIME type object
    sod = HttpResponse(content_type='application/ms-excel')

    # define filename
    sod['Content-Disposition'] = 'attachment; filename="systems.xls"'

    # create workbook object with UTF-8 encoding
    workbook = xlwt.Workbook(encoding='utf-8')
    # define name of worksheet within file
    worksheet_system = workbook.add_sheet('systems')

    # define styling for headline
    style = style_headline()

    """ start with headline """

    # set counter
    row_num = 0

    # create empty list
    headline = []

    # check for attribute id
    if dfirtrack_config.SPREAD_SYSTEM_ID:
        headline.append('ID')

    # append mandatory attribute
    headline.append('System')

    # check for remaining attributes
    if dfirtrack_config.SPREAD_DNSNAME:
        headline.append('DNS name')
    if dfirtrack_config.SPREAD_DOMAIN:
        headline.append('Domain')
    if dfirtrack_config.SPREAD_SYSTEMSTATUS:
        headline.append('Systemstatus')
    if dfirtrack_config.SPREAD_ANALYSISSTATUS:
        headline.append('Analysisstatus')
    if dfirtrack_config.SPREAD_REASON:
        headline.append('Reason')
    if dfirtrack_config.SPREAD_RECOMMENDATION:
        headline.append('Recommendation')
    if dfirtrack_config.SPREAD_SYSTEMTYPE:
        headline.append('Systemtype')
    if dfirtrack_config.SPREAD_IP:
        headline.append('IP')
    if dfirtrack_config.SPREAD_OS:
        headline.append('OS')
    if dfirtrack_config.SPREAD_COMPANY:
        headline.append('Company')
    if dfirtrack_config.SPREAD_LOCATION:
        headline.append('Location')
    if dfirtrack_config.SPREAD_SERVICEPROVIDER:
        headline.append('Serviceprovider')
    if dfirtrack_config.SPREAD_TAG:
        headline.append('Tag')
    if dfirtrack_config.SPREAD_CASE:
        headline.append('Case')
    if dfirtrack_config.SPREAD_SYSTEM_CREATE_TIME:
        headline.append('Created')
    if dfirtrack_config.SPREAD_SYSTEM_MODIFY_TIME:
        headline.append('Modified')

    # write headline
    worksheet_system = write_row(worksheet_system, headline, row_num, style)

    # clear styling to default
    style = style_default()

    """ append systems """

    # get all System objects ordered by system_name
    systems = System.objects.all().order_by("system_name")

    # iterate over systems
    for system in systems:

        # skip system depending on export variable
        if system.system_export_spreadsheet == False:
            continue

        # autoincrement row counter
        row_num += 1

        # set column counter
        col_num = 1

        # create empty list for line
        entryline = []

        """ check for attribute """

        # system id
        if dfirtrack_config.SPREAD_SYSTEM_ID:
            entryline.append(system.system_id)

        """ append mandatory attribute """

        # system name
        entryline.append(system.system_name)

        """ check for remaining attributes """

        # dnsname
        if dfirtrack_config.SPREAD_DNSNAME:
            if system.dnsname == None:
                dnsname = ''
            else:
                dnsname = system.dnsname.dnsname_name
            entryline.append(dnsname)
        # domain
        if dfirtrack_config.SPREAD_DOMAIN:
            if system.domain == None:
                domain = ''
            else:
                domain = system.domain.domain_name
            entryline.append(domain)
        # systemstatus
        if dfirtrack_config.SPREAD_SYSTEMSTATUS:
            entryline.append(system.systemstatus.systemstatus_name)
        # analysisstatus
        if dfirtrack_config.SPREAD_ANALYSISSTATUS:
            entryline.append(system.analysisstatus.analysisstatus_name)
        # reason
        if dfirtrack_config.SPREAD_REASON:
            if system.reason == None:
                reason = ''
            else:
                reason = system.reason.reason_name
            entryline.append(reason)
        # recommendation
        if dfirtrack_config.SPREAD_RECOMMENDATION:
            if system.recommendation== None:
                recommendation = ''
            else:
                recommendation = system.recommendation.recommendation_name
            entryline.append(recommendation)
        # systemtype
        if dfirtrack_config.SPREAD_SYSTEMTYPE:
            if system.systemtype == None:
                systemtype = ''
            else:
                systemtype = system.systemtype.systemtype_name
            entryline.append(systemtype)
        # ip
        if dfirtrack_config.SPREAD_IP:
            # get all ips of system
            ips_all = system.ip.all()
            # count ips
            n = system.ip.count()
            # create empty ip string
            ip = ''
            # set counter
            i = 1
            # iterate over ip objects in ip list
            for ip_obj in ips_all:
                # add actual ip to ip string
                ip = ip + ip_obj.ip_ip
                # add newline except for last ip
                if i < n:
                    ip = ip + '\n'
                    i = i + 1
            entryline.append(ip)
        # os
        if dfirtrack_config.SPREAD_OS:
            if system.os == None:
                os = ''
            else:
                os = system.os.os_name
            entryline.append(os)
        # company
        if dfirtrack_config.SPREAD_COMPANY:
            companys_all = system.company.all()
            # count companies
            n = system.company.count()
            # create empty company string
            company = ''
            # set counter
            i = 1
            # iterate over company objects in company list
            for company_obj in companys_all:
                # add actual company to company string
                company = company + company_obj.company_name
                # add newline except for last company
                if i < n:
                    company = company + '\n'
                    i = i + 1
            entryline.append(company)
        # location
        if dfirtrack_config.SPREAD_LOCATION:
            if system.location == None:
                location = ''
            else:
                location = system.location.location_name
            entryline.append(location)
        # serviceprovider
        if dfirtrack_config.SPREAD_SERVICEPROVIDER:
            if system.serviceprovider == None:
                serviceprovider = ''
            else:
                serviceprovider = system.serviceprovider.serviceprovider_name
            entryline.append(serviceprovider)
        # tag
        if dfirtrack_config.SPREAD_TAG:
            tags_all = system.tag.all()
            # count tags
            n = system.tag.count()
            # create empty tag string
            tag = ''
            # set counter
            i = 1
            # iterate over tag objects in tag list
            for tag_obj in tags_all:
                # add actual tag to tag string
                tag = tag + tag_obj.tag_name
                # add newline except for last tag
                if i < n:
                    tag = tag + '\n'
                    i = i + 1
            entryline.append(tag)
        # case
        if dfirtrack_config.SPREAD_CASE:
            cases_all = system.case.all()
            # count cases
            n = system.case.count()
            # create empty case string
            case = ''
            # set counter
            i = 1
            # iterate over case objects in case list
            for case_obj in cases_all:
                # add actual case to case string
                case = case + case_obj.case_name
                # add newline except for last case
                if i < n:
                    case = case + '\n'
                    i = i + 1
            entryline.append(case)
        # system create time
        if dfirtrack_config.SPREAD_SYSTEM_CREATE_TIME:
            systeme_create_time = system.system_create_time.strftime('%Y-%m-%d %H:%M')
            entryline.append(systeme_create_time)
        # system modify time
        if dfirtrack_config.SPREAD_SYSTEM_MODIFY_TIME:
            system_modify_time = system.system_modify_time.strftime('%Y-%m-%d %H:%M')
            entryline.append(system_modify_time)

        # write line for system
        worksheet_system = write_row(worksheet_system, entryline, row_num, style)

    # write an empty row
    row_num += 2

    # write meta information for file creation
    actualtime = strftime('%Y-%m-%d %H:%M')
    worksheet_system.write(row_num, 0, 'SOD created:', style)
    worksheet_system.write(row_num, 1, actualtime, style)
    row_num += 1
    creator = str(request.user)
    worksheet_system.write(row_num, 0, 'Created by:', style)
    worksheet_system.write(row_num, 1, creator, style)

    #print("rows: " + str(len(worksheet_system._Worksheet__rows)))
    #print("cols: " + str(len(worksheet_system._Worksheet__cols))) # --> does not work

    """ add worksheet for systemstatus """

    # check all conditions
    if dfirtrack_config.SPREAD_WORKSHEET_SYSTEMSTATUS and dfirtrack_config.SPREAD_SYSTEMSTATUS and Systemstatus.objects.count() != 0:

        # define name of worksheet within file
        worksheet_systemstatus = workbook.add_sheet('systemstatus')

        # create empty list
        headline_systemstatus = []

        # append attributes
        headline_systemstatus.append('ID')
        headline_systemstatus.append('Systemstatus')
        headline_systemstatus.append('Note')

        # define styling for headline
        style = style_headline()

        # set counter
        row_num = 0

        # write headline
        worksheet_systemstatus = write_row(worksheet_systemstatus, headline_systemstatus, row_num, style)

        # clear styling to default
        style = style_default()

        """ append systemstatus """

        # get all Systemstatus objects ordered by systemstatus_name
        systemstatuss = Systemstatus.objects.all().order_by("systemstatus_id")

        # iterate over systemstatus
        for systemstatus in systemstatuss:

            # autoincrement row counter
            row_num += 1

            # set column counter
            col_num = 1

            # create empty list for line
            entryline_systemstatus = []

            entryline_systemstatus.append(systemstatus.systemstatus_id)
            entryline_systemstatus.append(systemstatus.systemstatus_name)
            entryline_systemstatus.append(systemstatus.systemstatus_note)

            # write line for systemstatus
            worksheet_systemstatus = write_row(worksheet_systemstatus, entryline_systemstatus, row_num, style)

    """ add worksheet for analysisstatus """

    # check all conditions
    if dfirtrack_config.SPREAD_WORKSHEET_ANALYSISSTATUS and dfirtrack_config.SPREAD_ANALYSISSTATUS and Analysisstatus.objects.count() != 0:

        # define name of worksheet within file
        worksheet_analysisstatus = workbook.add_sheet('analysisstatus')

        # create empty list
        headline_analysisstatus = []

        # append attributes
        headline_analysisstatus.append('ID')
        headline_analysisstatus.append('Analysisstatus')
        headline_analysisstatus.append('Note')

        # define styling for headline
        style = style_headline()

        # set counter
        row_num = 0

        # write headline
        worksheet_analysisstatus = write_row(worksheet_analysisstatus, headline_analysisstatus, row_num, style)

        # clear styling to default
        style = style_default()

        """ append analysisstatus """

        # get all Analysisstatus objects ordered by analysisstatus_name
        analysisstatuss = Analysisstatus.objects.all().order_by("analysisstatus_id")

        # iterate over analysisstatus
        for analysisstatus in analysisstatuss:

            # autoincrement row counter
            row_num += 1

            # set column counter
            col_num = 1

            # create empty list for line
            entryline_analysisstatus = []

            entryline_analysisstatus.append(analysisstatus.analysisstatus_id)
            entryline_analysisstatus.append(analysisstatus.analysisstatus_name)
            entryline_analysisstatus.append(analysisstatus.analysisstatus_note)

            # write line for analysisstatus
            worksheet_analysisstatus = write_row(worksheet_analysisstatus, entryline_analysisstatus, row_num, style)

    """ add worksheet for reason """

    # check all conditions
    if dfirtrack_config.SPREAD_WORKSHEET_REASON and dfirtrack_config.SPREAD_REASON and Reason.objects.count() != 0:

        # define name of worksheet within file
        worksheet_reason = workbook.add_sheet('reasons')

        # create empty list
        headline_reason = []

        # append attributes
        headline_reason.append('ID')
        headline_reason.append('Reason')
        headline_reason.append('Note')

        # define styling for headline
        style = style_headline()

        # set counter
        row_num = 0

        # write headline
        worksheet_reason = write_row(worksheet_reason, headline_reason, row_num, style)

        # clear styling to default
        style = style_default()

        """ append reasons """

        # get all Reason objects ordered by reason_name
        reasons = Reason.objects.all().order_by("reason_name")

        # iterate over reasons
        for reason in reasons:

            # autoincrement row counter
            row_num += 1

            # set column counter
            col_num = 1

            # create empty list for line
            entryline_reason = []

            entryline_reason.append(reason.reason_id)
            entryline_reason.append(reason.reason_name)
            entryline_reason.append(reason.reason_note)

            # write line for reason
            worksheet_reason = write_row(worksheet_reason, entryline_reason, row_num, style)

    """ add worksheet for recommendation """

    # check all conditions
    if dfirtrack_config.SPREAD_WORKSHEET_RECOMMENDATION and dfirtrack_config.SPREAD_RECOMMENDATION and Recommendation.objects.count() != 0:

        # define name of worksheet within file
        worksheet_recommendation = workbook.add_sheet('recommendations')

        # create empty list
        headline_recommendation = []

        # append attributes
        headline_recommendation.append('ID')
        headline_recommendation.append('Recommendation')
        headline_recommendation.append('Note')

        # define styling for headline
        style = style_headline()

        # set counter
        row_num = 0

        # write headline
        worksheet_recommendation = write_row(worksheet_recommendation, headline_recommendation, row_num, style)

        # clear styling to default
        style = style_default()

        """ append recommendations """

        # get all Recommendation objects ordered by recommendation_name
        recommendations = Recommendation.objects.all().order_by("recommendation_name")

        # iterate over recommendations
        for recommendation in recommendations:

            # autoincrement row counter
            row_num += 1

            # set column counter
            col_num = 1

            # create empty list for line
            entryline_recommendation = []

            entryline_recommendation.append(recommendation.recommendation_id)
            entryline_recommendation.append(recommendation.recommendation_name)
            entryline_recommendation.append(recommendation.recommendation_note)

            # write line for recommendation
            worksheet_recommendation = write_row(worksheet_recommendation, entryline_recommendation, row_num, style)

    """ add worksheet for tag """

    # check all conditions
    if dfirtrack_config.SPREAD_WORKSHEET_TAG and dfirtrack_config.SPREAD_TAG and Tag.objects.count() != 0:

        # define name of worksheet within file
        worksheet_tag = workbook.add_sheet('tags')

        # create empty list
        headline_tag = []

        # append attributes
        headline_tag.append('ID')
        headline_tag.append('Tag')
        headline_tag.append('Note')

        # define styling for headline
        style = style_headline()

        # set counter
        row_num = 0

        # write headline
        worksheet_tag = write_row(worksheet_tag, headline_tag, row_num, style)

        # clear styling to default
        style = style_default()

        """ append tags """

        # get all Tag objects ordered by tag_name
        tags = Tag.objects.all().order_by("tag_name")

        # iterate over tags
        for tag in tags:

            # autoincrement row counter
            row_num += 1

            # set column counter
            col_num = 1

            # create empty list for line
            entryline_tag = []

            entryline_tag.append(tag.tag_id)
            entryline_tag.append(tag.tag_name)
            entryline_tag.append(tag.tag_note)

            # write line for tag
            worksheet_tag = write_row(worksheet_tag, entryline_tag, row_num, style)

    # close file
    workbook.save(sod)

    # call logger
    info_logger(str(request.user), " SYSTEM_XLS_CREATED")

    # return xls object
    return sod
