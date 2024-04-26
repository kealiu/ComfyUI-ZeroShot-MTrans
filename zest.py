import torch
import numpy as np
from PIL import Image, ImageChops, ImageEnhance

class ZeSTGrayoutSubject:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": { 
                    "target_image": ("IMAGE",), 
                    "subject_mask": ("MASK",), 
                    "brighter": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01})
                }
        }
    
    RETURN_TYPES = ("IMAGE",)
    OUTPUT_IS_LIST = (False, )
    FUNCTION = "grayoutSubject"
    CATEGORY = "image"

    def grayoutSubject(self, target_image, subject_mask, brighter):
        print("target_image ", target_image.size(), target_image)
        print("subject_mask ", subject_mask.size(), subject_mask)
        print("brighter ", brighter)
        # from pure mask to image
        subject_mask = subject_mask.reshape((-1, 1, subject_mask.shape[-2], subject_mask.shape[-1])).movedim(1, -1).expand(-1, -1, -1, 3)

        target = Image.fromarray((255. * target_image[0]).numpy().astype(np.uint8))
        subjectmask = Image.fromarray((255. * subject_mask[0]).numpy().astype(np.uint8))

        grayall_target = target.convert('L').convert('RGB')
        grayall_target = ImageEnhance.Brightness(grayall_target)
        grayall_target = grayall_target.enhance(brighter)

        graysubject = ImageChops.darker(grayall_target, subjectmask)
        colorbackground = ImageChops.darker(target, ImageChops.invert(subjectmask))

        grayoutsubject = ImageChops.lighter(colorbackground, graysubject)

        output_images = []
        image = np.array(grayoutsubject).astype(np.float32) / 255.0
        image = torch.from_numpy(image)[None,]
        output_images.append(image)
        return output_images

