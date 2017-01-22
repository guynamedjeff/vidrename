import glob, os, re

directory = r'D:\Downloads\test'
extensions = [r'*.mp4', r'*.mkv', r'*.avi']

# Renames media files into a unified format.
def rename(dir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        title = remove_spaces(title)
        resolution = find_resolution(title).lower()
        if re.search(r'e[0-9]+', title, re.I) or re.search(r'\.\d\d\d\.', title, re.I):
            title = rename_tv_shows(title)
        else:
            title = rename_movies(title)
        os.rename(pathAndFilename,
            os.path.join(dir,titlePattern % title + resolution + ext))

# Seperates titles with periods, reformats text, and removes added text references on tv files.
def rename_tv_shows(title):
    titleSegments = title.split('.')
    match = r'^\d\d\d$'
    # 're.I' flag performs case-insensitive matching.
    if re.search(r'e[0-9]+', title, re.I):
        match = r'e[0-9]+'
    titleSegments, n = segment_by_type(titleSegments, match)
    titleSegments[n] = titleSegments[n].upper()
    title = '.'.join(titleSegments[:n+1])
    return title

# Removes parenthesis, seperates titles with periods, and reformats text on movie files.
def rename_movies(title):
    titleSegments = title.split('.')
    match = r'\d\d\d\d'
    # 're.I' flag performs case-insensitive matching.
    if re.search(match, title, re.I):
      titleSegments, n = segment_by_type(titleSegments, match)
      titleSegments[n] = titleSegments[n].upper()
      title = '.'.join(titleSegments[:n+1])
      return title

    # If no year exists, but a resolution does.
    match = re.search(r'\.[0-9]+p', title, re.I)
    if match:
        return '.'.join(titleSegments).replace(match.group(), '').title()

    return title.title()

# Removes spaces, parenthesis, and hyphens from title.
def remove_spaces(title):
    title = re.sub('[()]', '', title)
    titleSegments = title.split()
    return '.'.join(titleSegments).replace('.-','').replace('-','')

# Returns resolution if there is a title match for a resolution.
def find_resolution(title):
    match = re.search(r'[0-9]+p', title, re.I)
    if match:
        return '.' + match.group()
    return ''

# Reformats a title's segments based on type.
# Returns a tuple of titleSegments and 'n' to denote a finishing point.
def segment_by_type(titleSegments, match):
    n = 0
    while re.search(match, titleSegments[n], re.I) == None:
      titleSegments[n] = titleSegments[n].capitalize()
      n += 1
    return titleSegments, n

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