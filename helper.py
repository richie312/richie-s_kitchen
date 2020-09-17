# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 16:26:13 2020

@author: aritra_chatterjee
"""

# show images
# =============================================================================
# for img in images_labels:
#     image = cv2.imread(os.path.join(images_folder,img))
#     half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1) 
#     cv2.imshow('{}'.format(img),half)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# 
# =============================================================================


# =============================================================================
# # create files in text folder for corresponding recipe
# text_folder = os.path.join(main_dir,'recipe_text')
# text_files = [images_labels[i].split('.')[0]+str('.txt')
#               for i in range(len(images_labels))]
# 
# for file in text_files:
#     with open(os.path.join(text_folder,file),'w') as outfile:
#         outfile.write('')
# 
# =============================================================================
