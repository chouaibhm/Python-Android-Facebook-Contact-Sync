#!/usr/bin/env python2

import vobject, sys, os, subprocess

versionNumber = 1.1

def usage():
    print >> sys.stderr, "Usage:  %s [OPTIONS]" % (sys.argv[0])
    print >> sys.stderr, """
OPTIONS may be some of:
    -a    --add-contacts       When adding birthdays, add new contacts for people you are friends on facebook with but don't have in your vcard file.

    -v    --version            Output version of the password generator program

    -h    --help               Output this message

The defaut option is only to add to contacts that overlap between facebook and your vcard file.
""" % {'command': sys.argv[0]}

def version():
    print "Python Password Generator Version: " + str(versionNumber)


def main(argv):
    doAdd = False
    if len(argv) > 1:   
        if argv[1] == "-a" or argv[1] == "--add-contacts":
            doAdd = True
        elif argv[1] == "-v" or argv[1] == "--version":
            version()
            sys.exit()
        else:
            usage()
            sys.exit()
            
    f = open("facebook_birthdays.ics","r")
    contents = f.read()
    contents = contents.decode('utf-8')
    f.close()
    
    bDayDict = {}
    components = vobject.readComponents(contents, validate=True)
    for component in components:
        for vevents in component.getChildren():
            if type(vevents) is vobject.icalendar.RecurringComponent:
                dt = ""
                n = ""
                for child in vevents.getChildren():
                    if child.name == "DTSTART":
                        m = str(child.value.month) 
                        if len(m) == 1:
                            m = "0"+m
                        d = str(child.value.day)
                        if len(d) == 1:
                            d = "0"+d
                        dt = "2015" + m + d
                    if child.name == "SUMMARY":
                        n = unicode(child.value)
                        ind = n.find('\'')
                        n = n[:ind]
                bDayDict[n]=dt
    
    
    f = open("contacts.vcf","rb")
    contents = f.read()
    contents = contents.decode('utf-8')
    f.close()
    
    newvcf = []
    
    components = vobject.readComponents(contents, validate=True)
    for component in components:
        for child in component.getChildren():
            if child.name == "FN":
                if child.value in bDayDict:
                    component.add('bday')
                    component.bday.value = bDayDict.pop(child.value)
        newvcf.append(component)

    if doAdd:
        nonexistantContacts = bDayDict.items()
        for contact in nonexistantContacts:
            v = vobject.vCard()
            v.add('n')
            fullname = contact[0].split(" ")
            last = fullname[len(fullname) - 1]
            first = fullname[0]
            v.n.value = vobject.vcard.Name( family=last, given=first )
            v.add('fn')
            v.fn.value = contact[0]
            v.add('bday')
            v.bday.value = contact[1]
            v.add('version')
            v.version.value = "2.1"
            newvcf.add(v)

    f = open("out1.vcf", 'wb')
    print newvcf
    for vcard in newvcf:
        f.write(vcard.serialize())
    f.close()
    
if __name__ == "__main__":
       sys.exit(main(sys.argv)) 
