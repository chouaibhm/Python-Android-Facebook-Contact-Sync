#Facebook Contact Sync in Two Easy(ish) Python Scripts! 

##How to add contact photos to your addressbook from Facebook
In order to use this python script to download your contact photos, you will need to get a copy of the list of all your facebook friends. In order to do this, go to your friends page on your timeline. This page loads the list of your friends as you scroll further down the page, using javascript. In order to get your full list of friends, you will need a way to download the generated page's html source **after** you've already scrolled down and gotten all of your friends on the page. If you have firefox, you can achieve this by using [the web developer add-on](http://chrispederick.com/work/web-developer/). Select "View Source" -\> "View Generated Source." Probably it will take a minute and your computer's CPU and fan will spin up. Wait a while and a new window will pop-up with the source html for the page. Click "File" -\> "Save As" and save it as index.html. We'll need this file for the script.
![Facebook screenshot of the friends page showing how to download source](http://i.imgur.com/xFilq60.png)

1. Clone this repo. `git clone https://github.com/f41c0r/Python-Android-Facebook-Contact-Sync.git`
2. Move the file into the repo. Make sure it's named `index.html`.
3. Export your existing contacts from android into a vcf file using the android contacts file. Place it in the same directory, and name it `in.vcf`.
4. Execute the `fb_picture_scrape_add_to_vcard.py` python script. It may take a minute or two.
5. Copy the .vcf file back to your sdcard on your phone, delete all your phone contacts. (in android, Settings -\> Apps -\> All Applications -> Contacts Storage -\> Clear Data)
6. Import the new out.vcf file in the address book.

##How to take your facebook contacts and put them in your addressbook

Go to Facebook, and go to the events page. At the bottom, right click the link to the webcal of people's birthdays, and select "Copy Link Location"
![Facebook screenshot of events page showing where to find the webcal link](http://i.imgur.com/hdg6peZ.png)

Paste the url into your browser, replacing `webcal://` with `https://` - this will prompt download of the ics file from Facebook.

1. Clone this repo. `git clone https://github.com/f41c0r/Python-Android-Facebook-Contact-Sync.git`
2. Rename and move the file to `facebook_birthdays.ics`.
3. Export your adressbook to a .vcf file and place it in the same directory, name it `contacts.vcf`
4. Run the `fb_birthday_vcard_merger.py` python script. The -a argument may also be of interest as well.
5. Copy the .vcf file back to your sdcard on your phone, delete all your phone contacts. (in android, Settings -\> Apps -\> All Applications -> Contacts Storage -\> Clear Data)
6. Import the new out.vcf file in the address book.

On some versions of android the birthdays don't show up in the addressbook because google can't be bothered to even write a competent version of a vcard reader. (Note that the bday field has been included in every version of the vcard specification since the start.) In such a case, you can use something [birthday adapter](http://sufficientlysecure.org/birthday-adapter) which will put the birthdays into your android calendar. 

If all you wanted was to add the birthdays in your calendar and you don't care about mantaining the vCard file, you could just attempt to import the .ics file to your calendar, and skip all this mess in the first place.


## License
GPL v3.0 
