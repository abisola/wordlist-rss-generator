# wordlist-rss-generator

I have been trying to improve my German vocabulary for a while. I thought some passive learning could help and have been enjoying the 'Word of the day' dictionary screensaver on my Mac.

This is an attempt to coopt the now defunct RSS visualiser screensaver and use for the same purpose.

You need to set up the cron job to make it work. Obviously, you can change the language file to fit your needs.

This is the cron job you will need to set if you want it to refresh the feed every 10 minutes:

  */10 * * * * /path/to/project/directory/setenv.sh

You also need to set the environment variable: TRANSLATOR_PROJECT_ROOT_DIR to /path/to/project/directory/


Enjoy. It's pretty easy to use!

I got hold of [the list](https://germangrinds.files.wordpress.com/2013/02/die-500-hc3a4ufigsten-wc3b6rter-der-deutschen-sprache-translated.pdf) I'm using from [Holger Haase's wonderful blog](http://germangrinds.com/about/)

To use this, you will also need to download the RSS Visualiser Screensaver app which is no longer provided with OS X by default. I was able to do this by following the instructions from [Neil Gonzalez on the WonderHowTo site](http://mac-how-to.wonderhowto.com/how-to/get-apples-rss-visualizer-back-as-screensaver-mac-os-x-10-8-higher-0156457/).
