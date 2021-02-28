from torch import nn

from SSD.ssd.modeling.backbone import build_backbone
from SSD.ssd.modeling.box_head import build_box_head


class SSDDetector(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        self.backbone = build_backbone(cfg)
        self.box_head = build_box_head(cfg)

    def forward(self, images, targets=None):
        features = self.backbone(images)
        detections_raw, detections, detector_losses = self.box_head(features, targets)
        if self.training:
            return detector_losses
        return detections_raw, detections
