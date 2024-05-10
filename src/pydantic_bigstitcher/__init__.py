from __future__ import annotations
from typing import Literal, Optional
from pydantic_xml import BaseXmlModel, attr, element

class BasePath(BaseXmlModel):
    type: Literal["relative", "absolute"] = attr()

class ZGroup(BaseXmlModel, tag='zgroup'):
    setup: str = attr()
    timepoint: str = attr()
    path: str = element()

class ZGroups(BaseXmlModel, tag='zgroups'):
    zgroups: list[ZGroup] = element(tag='zgroup')

class Zarr(BaseXmlModel, tag='zarr'):
    type: str = attr()

class ZarrImageLoader(BaseXmlModel, tag='ImageLoader'):
    format: str = attr()
    version: str = attr()
    zarr: Zarr = element(tag='zarr')
    zgroups: ZGroups
    
class VoxelSize(BaseXmlModel):
    unit: str = element()
    size: str = element()

class Attributes(BaseXmlModel):
    illumination: str = element()
    channel: str = element()
    tile: str = element()
    angle: str = element()

class ViewSetup(BaseXmlModel):
    id: str = element()
    name: str = element()
    size: str = element()
    voxelSize: VoxelSize
    attributes: Attributes

class PatternTimePoints(BaseXmlModel, tag='Timepoints'):
    type: Literal["pattern"] = attr()
    timepoints: list[str] = element(tag='integerpattern')

class MissingView(BaseXmlModel):
    setup: str = attr()
    timepoint: str = attr()

class MissingViews(BaseXmlModel):
    views: list[MissingView] = element('MissingView', default=None)

class ViewSetups(BaseXmlModel):
    viewSetup: list[ViewSetup] = element(tag='ViewSetup')

class SequenceDescription(BaseXmlModel):
    """
    https://github.com/bigdataviewer/spimdata/blob/46c3878baef80cc4170a33012c8281481dbbfcb2/src/main/java/mpicbg/spim/data/generic/sequence/AbstractSequenceDescription.java#L52
    """
    ImageLoader: ZarrImageLoader
    ViewSetups: ViewSetups
    Timepoints: PatternTimePoints = element(tag='Timepoints')
    MissingViews: MissingViews

class AffineViewTransform(BaseXmlModel):
    type: Literal['affine'] = attr('affine')
    name: str = element(tag='Name')
    affine: str = element(tag='affine')

class ViewRegistration(BaseXmlModel):
    """
    https://github.com/bigdataviewer/spimdata/blob/master/src/main/java/mpicbg/spim/data/registration/ViewRegistrations.java#L47
    """
    timepoint: str = attr()
    setup: str = attr()
    viewTransforms: list[AffineViewTransform] = element(tag='ViewTransform')

class SpimData(BaseXmlModel):
    """
    https://github.com/bigdataviewer/spimdata/blob/46c3878baef80cc4170a33012c8281481dbbfcb2/src/main/java/mpicbg/spim/data/generic/AbstractSpimData.java#L36
    """
    version: Literal['0.2'] = attr(version="0.2")
    BasePath: BasePath
    SequenceDescription: SequenceDescription
    ViewRegistrations: list[ViewRegistration] = element(tag='ViewRegistration')

class ViewInterestPoints(BaseXmlModel):
    pass


class SpimData2(SpimData, tag='SpimData'):
    """
    https://github.com/PreibischLab/multiview-reconstruction/blob/master/src/main/java/net/preibisch/mvrecon/fiji/spimdata/SpimData2.java#L64
    """
    ViewInterestPoints: ViewInterestPoints

