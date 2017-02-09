#By: Jeff Roszkowski
#https://github.com/guynamedjeff/vidrename

import glob, os, re

# Runs core application.
def run_it(path):
    extensions = [r'*.mp4', r'*.mkv', r'*.avi']
    directory = r'%s' % path
    for extension in extensions:
        rename(directory, extension, r'%s')

# Renames media files into a unified format.
def rename(dir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        title = remove_spaces(title)
        resolution, title = extract_resolution(title)
        title = segment_and_repair(title)
        while title.endswith('.'):
            title = title[:-1]
        os.rename(pathAndFilename,
              os.path.join(dir,titlePattern % title + resolution + ext))

# Removes the junk attached to the end of each file name.
# Adds a trailing period to the title to help distinguish digit length
# Also, provides a fix for capitalization and returns the finished title.
def segment_and_repair(title):
    title = title + '.'
    titleSegments = title.split('.')
    match = None
    types = [r'\.s*\d*e\d+', r'\.\d\d\d\.', r'\.\d+x\d+\.', r'\.[1-2]\d\d\d\.']
    for t in types:
      if re.search(t, title, re.I):
        match = re.search(t, title, re.I)
        titleSegments, n = segment_by_type(titleSegments, match.group())
        titleSegments[n] = titleSegments[n].upper()
        title = '.'.join(titleSegments[:n+1])
        return title
    return title.title()

# Removes spaces, parenthesis, and hyphens from title.
def remove_spaces(title):
    title = re.sub('[()]', '', title)
    titleSegments = title.split()
    return '.'.join(titleSegments).replace('.-','').replace('-','')

# Returns resolution if there is a title match for a resolution.
# Also, removes any mentions of a resolution from the title string.
def extract_resolution(title):
    match = re.search(r'[0-9]+p', title, re.I)
    if match:
        return ('.' + match.group()).lower(), title.replace('.' + match.group(), '')
    return '', title

# Reformats a title's segments based on type.
# Returns a tuple of titleSegments and 'n' to denote a finishing point.
def segment_by_type(titleSegments, match):
    n = 0
    match = match.replace(".","")
    while re.search(match, titleSegments[n], re.I) == None:
      titleSegments[n] = titleSegments[n].capitalize()
      n += 1
    return titleSegments, n

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