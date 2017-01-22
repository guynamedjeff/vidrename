import glob, os, re

directory = r'D:\Downloads\test'
extensions = [r'*.mp4', r'*.mkv', r'*.avi']

# Renames media files into a unified format.
def rename(dir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        title = remove_spaces(title)
        resolution = find_resolution(title).lower()
        if re.search(r'e[0-9]+', title, re.I):
            title = rename_tv_shows(title)
        else:
            title = rename_movies(title)
        os.rename(pathAndFilename,
            os.path.join(dir,titlePattern % title + resolution + ext))

# Seperates titles with periods, reformats text, and removes added text references on tv files.
def rename_tv_shows(title):
    titleSegments = title.split('.')
    n = 0
    # 're.I' flag performs case-insensitive matching.
    while re.search(r'e[0-9]+', titleSegments[n], re.I) == None:
      titleSegments[n] = titleSegments[n].title()
      n += 1
    titleSegments[n] = titleSegments[n].upper()
    title = '.'.join(titleSegments[:n+1])
    return title

# Removes parenthesis, seperates titles with periods, and reformats text on movie files.
def rename_movies(title):
    title = title.replace("(","").replace(")","")
    titleSegments = title.split('.')
    # 're.I' flag performs case-insensitive matching.
    year = r'\d\d\d\d'
    if re.search(year, title, re.I):
      n = 0
      while re.search(year, titleSegments[n], re.I) == None:
        titleSegments[n] = titleSegments[n].title()
        n += 1
      titleSegments[n] = titleSegments[n].upper()
      title = '.'.join(titleSegments[:n+1])
      return title

    match = re.search(r'\.[0-9]+p', title, re.I)
    if match:
        return '.'.join(titleSegments).replace(match.group(), '').title()

    return title.title()

# Removes spaces and hyphens from title.
def remove_spaces(title):
    titleSegments = title.split()
    return '.'.join(titleSegments).replace('.-','').replace('-','')

# Preserves resolution.
def find_resolution(title):
    match = re.search(r'[0-9]+p', title, re.I)
    if match:
        return '.' + match.group()
    return ''

for extension in extensions:
    rename(directory, extension, r'%s')

###############################Instructions###################################

#Original python function from stackoverflow
# (http://stackoverflow.com/questions/225735/batch-renaming-of-files-in-a-directory):

# import glob, os
#
# def rename(dir, pattern, titlePattern):
#     for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
#         title, ext = os.path.splitext(os.path.basename(pathAndFilename))
#         os.rename(pathAndFilename,
#             os.path.join(dir,titlePattern % title + ext))

#Example:

#rename(r'D:\Downloads\test', r'*.mp4', r'new(%s)')
#changes 'Video.mp4' to 'new(Video).mp4' based on original

#How to split in python from stackoverflow
# http://stackoverflow.com/questions/17060039/split-string-at-nth-occurrence-of-a-given-character

# text = '20_231_myString_234'
# n = 2
# groups = text.split('_')
# '_'.join(groups[:n]), '_'.join(groups[n:])
# ('20_231','myString_234')