from torch.utils.data import Dataset
#import torchvision.transforms.functional as TF
import torch
from skimage import io 

class WildfireDataset(Dataset):
    def __init__(self, image_paths, labels, transform=False):
        self.image_paths = image_paths
        self.labels = labels
        self.transform = transform
        
    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        image_filepath = self.image_paths[idx]

        image = io.imread(image_filepath)
        label = torch.tensor(self.labels[idx])
       
        if self.transform: #if is indicated, the image will be transformed
        #into whatever the user indicates, in this case, into a tensor
            image = self.transform(image)
        
        return image, label