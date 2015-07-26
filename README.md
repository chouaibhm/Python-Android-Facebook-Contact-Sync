# How to take your facebook contacts and put them in your addressbook

Go to Facebook, and go to the events page. At the bottom, right click the link to the webcal of people's birthdays, and select "Copy Link Location"
![Facebook Screenshot](http://i.imgur.com/hdg6peZ.png)

Paste the url into your browser, replacing `webcal://` with `https://` - this will prompt download of the ics file from Facebook.

1. Clone this repo. `git clone https://github.com/f41c0r/fb_birthday_vcard_merger.git`
2. Rename and move the file to `facebook_birthdays.ics`.
3. Export your adressbook to a .vcf file and place it in the same directory.
4. Run the python script. The -a argument may also be of interest as well.
5. Copy the .vcf file back to your sdcard on your phone, delete all your phone contacts. (in android, Settings -\> Apps -\> All Applications -> Contacts Storage -\> Clear Data)
6. Import the new out.vcf file in the address book.

On some versions of android the birthdays don't show up in the addressbook because google can't be bothered to even write a competent version of a vcard reader. (Note that the bday field has been included in every version of the vcard specification since the start.) In such a case, you can use something [birthday adapter](http://sufficientlysecure.org/birthday-adapter) which will put the birthdays into your android calendar. Or you could just attempt to import the .ics file to your calendar, and skip all this mess in the first place.


## License
GPL v3.0 
