from chunkify import chunkify

# put ur input file path here
chunkify('submission\\Navigam1108\\Feature_Addition_Chunkify\\test.txt', 10)

# test on a large file  (29 mb)
#chunkify('submission\\Navigam1108\\Feature_Addition_Chunkify\\Computer Organizatiion and Design.pdf', 1000)
# successful

# invalid inputs
# chunkify('submission\\Navigam1108\\Feature_Addition_Chunkify\\test.txt', -1)
# chunkify('submission\\Navigam1108\\Feature_Addition_Chunkify\\non_existing_file', 10)