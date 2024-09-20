from __future__ import annotations

from typing import Any, Literal, Optional

from pydantic_xml import BaseXmlModel, attr, element

from pydantic_bigstitcher.transforms import Axes, HoAffine
from pydantic_bigstitcher.transforms import AffineViewTransform


class BasePath(BaseXmlModel):
    typ: Literal["relative", "absolute"] = attr(name="type")
    path: str

class ZGroup(BaseXmlModel, tag="zgroup"):
    setup: str = attr()
    timepoint: str = attr()
    path: str | None = element(default=None)


class ZGroups(BaseXmlModel):
    zgroups: list[ZGroup] = element(tag="zgroup")


class Zarr(BaseXmlModel):
    typ: str = attr(name="type")
    path: str

class N5(BaseXmlModel):
    typ: str = attr(name='type')
    path: str


class ZarrImageLoader(BaseXmlModel, tag='ImageLoader', skip_empty=True):
    fmt: str = attr(name="format")
    version: str = attr()
    s3bucket: Optional[str] = element(default=None)
    zarr: Zarr = element(tag="zarr")
    zgroups: ZGroups = element(tag="zgroups")

class BDVN5ImageLoader(BaseXmlModel, tag='ImageLoader', skip_empty=True):
    fmt: str = attr(name="format")
    version: str = attr()
    n5: N5 = element(tag='n5')

class VoxelSize(BaseXmlModel):
    unit: str = element()
    size: str = element()


class ViewSetupAttributes(BaseXmlModel):
    illumination: str = element()
    channel: str = element()
    tile: str = element()
    angle: str = element()

class ViewSetup(BaseXmlModel):
    ident: str = element(tag="id")
    name: str = element()
    size: str = element()
    voxel_size: VoxelSize = element(tag="voxelSize")
    attributes: ViewSetupAttributes = element(tag='attributes')

class Attribute(BaseXmlModel):
    id: int = element(tag='id')
    name: str = element(tag='name')

class IlluminationAttribute(BaseXmlModel, tag='Attributes'):
    name: Literal["illumination"] = attr(tag='name')
    illumination: list[Attribute] = element(tag='Illumination')

class TileAttribute(BaseXmlModel, tag='Attributes'):
    name: Literal["tile"] = attr(tag='name')
    tile: list[Attribute] = element(tag='Tile')

class AngleAttribute(BaseXmlModel, tag='Attributes'):
    name: Literal["angle"] = attr(tag='name')
    angle: list[Attribute] = element(tag='Angle')

class ChannelAttribute(BaseXmlModel, tag='Attributes'):
    name: Literal["channel"] = attr(tag='name')
    angle: list[Attribute] = element(tag='Channel')

class ViewSetups(BaseXmlModel):
    # the order of the definition of these attributes should match the order of the data in xml
    view_setups: list[ViewSetup] = element(tag="ViewSetup")
    attributes: list[IlluminationAttribute | TileAttribute | AngleAttribute | ChannelAttribute] = element(tag='Attributes')


class PatternTimePoints(BaseXmlModel, tag="Timepoints"):
    typ: Literal["pattern"] = attr(name="type")
    timepoints: list[str] = element(tag="integerpattern")


class MissingView(BaseXmlModel):
    setup: str = attr()
    timepoint: str = attr()


class MissingViews(BaseXmlModel):
    views: list[MissingView] = element("MissingView", default=None)


class SequenceDescription(BaseXmlModel):
    """
    https://github.com/bigdataviewer/spimdata/blob/46c3878baef80cc4170a33012c8281481dbbfcb2/src/main/java/mpicbg/spim/data/generic/sequence/AbstractSequenceDescription.java#L52
    """

    image_loader: ZarrImageLoader |  BDVN5ImageLoader | None = element(tag="ImageLoader", default=None)
    view_setups: ViewSetups | None = element(tag="ViewSetups", default=None)
    time_points: PatternTimePoints | None = element(tag="Timepoints",  default=None)
    missing_views: MissingViews | None = element(tag="MissingViews",  default=None)


class ViewRegistration(BaseXmlModel):
    """
    https://github.com/bigdataviewer/spimdata/blob/master/src/main/java/mpicbg/spim/data/registration/ViewRegistrations.java#L47
    """

    timepoint: str = attr()
    setup: str = attr()
    view_transforms: list[AffineViewTransform] = element(tag="ViewTransform")

class ViewRegistrations(BaseXmlModel):
    elements: list[ViewRegistration] = element(tag='ViewRegistration')

class SpimData(BaseXmlModel):
    """
    https://github.com/bigdataviewer/spimdata/blob/46c3878baef80cc4170a33012c8281481dbbfcb2/src/main/java/mpicbg/spim/data/generic/AbstractSpimData.java#L36
    """

    version: Literal["0.2"] = attr(version="0.2")
    base_path: BasePath = element(tag='BasePath')
    sequence_description: SequenceDescription = element(tag='SequenceDescription')
    view_registrations: ViewRegistrations = element(tag="ViewRegistrations")


class ViewInterestPointsFile(BaseXmlModel):
    timepoint: str = attr()
    setup: str = attr()
    label: str = attr()
    params: str = attr()
    path: str 

class ViewInterestPoints(BaseXmlModel):
    data: list[ViewInterestPointsFile] = element(tag='ViewInterestPointsFile')

class BoundingBox(BaseXmlModel):
    """
    https://github.com/PreibischLab/multiview-reconstruction/blob/master/src/main/java/net/preibisch/mvrecon/fiji/spimdata/boundingbox/BoundingBox.java#L30
    """
    title: str = attr()
    mininum: str = attr(name='min')
    maximum: str = attr(name='max')

class BoundingBoxes(BaseXmlModel):
    """
    https://github.com/PreibischLab/multiview-reconstruction/blob/master/src/main/java/net/preibisch/mvrecon/fiji/spimdata/boundingbox/BoundingBoxes.java#L29
    """
    data: list[BoundingBox] | None = element(tag='BoundingBox', default=None)

class PointSpreadFunctions(BaseXmlModel):
    ...

class StitchingResults(BaseXmlModel):
    ...

class IntensityAdjustments(BaseXmlModel):
    ...


class SpimData2(SpimData, tag="SpimData"):
    """
    https://github.com/PreibischLab/multiview-reconstruction/blob/master/src/main/java/net/preibisch/mvrecon/fiji/spimdata/SpimData2.java#L64
    """

    view_interest_points: ViewInterestPoints | None = element(tag='ViewInterestPoints', default=None)
    bounding_boxes: BoundingBoxes | None = element(tag='BoundingBoxes', default=None)
    point_spread_functions: PointSpreadFunctions | None = element(tag='PointSpreadFunctions', default=None)
    stitching_results: StitchingResults | None = element(tag='StitchingResults', default=None)
    intensity_adjustments: IntensityAdjustments | None = element(tag='IntensityAdjustments',  default=None)

