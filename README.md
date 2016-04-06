# wordlist-rss-generator

I have been trying to improve my German vocabulary for a while. I thought some passive learning could help and have been enjoying the 'Word of the day' dictionary screensaver on my Mac.

This is an attempt to coopt the now defunct RSS visualiser screensaver and use for the same purpose.

You need to set up the cron job to make it work. Obviously, you can change the language file to fit your needs.

This is the cron job you will need to set if you want it to refresh the feed every 10 minutes: 

*/10 * * * * /path/to/project/directory/setenv.sh

You also need to set the environment variable: TRANSLATOR_PROJECT_ROOT_DIR to /path/to/project/directory/


Enjoy. It's pretty easy to use!
