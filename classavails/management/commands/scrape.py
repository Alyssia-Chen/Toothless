from classavails.models import ClassAvails
from django.core.management.base import BaseCommand
# To grab urls
from urllib.request import urlopen as uReq
# To parse html
from bs4 import BeautifulSoup as soup

class Command(BaseCommand):

    def handle(self, *args, **options):
        my_url = 'https://www.sis.hawaii.edu/uhdad/avail.classes?i=MAN&t=202210&s=ACC'
        
        # Opening connection and grabbing the page
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()

        # Parses html
        page_soup = soup(page_html, "html.parser")

        # Grab each row which either contains a class (has CRN) or some other notes 
        containers = page_soup.select("tr")

        # Loop to get important info:
        for container in containers:
            if (len(container.findAll("td", {"colspan":"11"})) < 1):
                try:
                    CRN = container.a.text
                    course = container.findAll("td", {"nowrap":"nowrap"})[0].text
                    section = container.findAll("td", {"class":"default"})[3].text
                    title = container.findAll("td", {"class":"default"})[4].text
                    creditNum = container.findAll("td", {"class":"default"})[5].text
                    instructor = container.findAll("abbr")[0].span["title"]
                    curEnrolled = container.findAll("td", {"align": "center"})[0].text
                    seatsAvail = container.findAll("td", {"align": "center"})[1].text
                    curWaitlisted = container.findAll("td", {"align": "center"})[2].text
                    waitlistAvailable = container.findAll("td", {"align": "center"})[3].text
                    classShorthand = container.findAll("td", {"class" : "default"})[11].text #This needs to be broken down into actual days
                    time = container.findAll("td", {"class" : "default"})[12].text # need parsing?

                    roomShorthand = container.findAll("abbr")[1].text
                    roomLong = container.findAll("abbr")[1].span["title"]

                    dates = container.findAll("td", {"class": "default"})[14].text

                    ClassAvails.objects.create(
                        CRN = CRN,
                        course = course,
                        section = section,
                        title = title,
                        credits = creditNum,
                        instructor = instructor,
                        curEnrolled = curEnrolled,
                        seatsAvail = seatsAvail,
                        curWaitlisted = curWaitlisted,
                        waitlistAvailable = waitlistAvailable,
                        days = classShorthand,
                        time = time,
                        location = roomShorthand,
                        dates = dates,
                    )
                except:
                    print("An exception occurred")
            else:
                print("Comment found")

        


# self.stdout.write()
# python manage.py scrape <argument>