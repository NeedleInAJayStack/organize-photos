Simple little script to organize files with a `YYYYMMDD` name format into yearly and monthly folders 
in a destination directory. This is used to automate my photo organization.

Sample crontab usage:

```cron
@monthly python3 ~/dev/python/organize-photos/organize-photos.py ~/Image/Mobile\ Photos/ ~/Image/Photos/
```