from __future__ import annotations

from typing import Literal

from pydantic_xml import BaseXmlModel, attr, element


class BasePath(BaseXmlModel):
    typ: Literal["relative", "absolute"] = attr(name="type")


class ZGroup(BaseXmlModel, tag="zgroup"):
    setup: str = attr()
    timepoint: str = attr()
    path: str = element()


class ZGroups(BaseXmlModel, tag="zgroups"):
    zgroups: list[ZGroup] = element(tag="zgroup")


class Zarr(BaseXmlModel, tag="zarr"):
    typ: str = attr(name="type")


class ZarrImageLoader(BaseXmlModel, tag="ImageLoader"):
    fmt: str = attr(name="format")
    version: str = attr()
    zarr: Zarr = element(tag="zarr")
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
    ident: str = element(tag="id")
    name: str = element()
    size: str = element()
    voxel_size: VoxelSize = element(tag="voxelSize")
    attributes: Attributes


class ViewSetups(BaseXmlModel):
    view_setup: list[ViewSetup] = element(tag="ViewSetup")


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

    image_loader: ZarrImageLoader
    view_setups: ViewSetups = element(tag="ViewSetups")
    time_points: PatternTimePoints = element(tag="Timepoints")
    missing_views: MissingViews = element(tag="MissingViews")


class AffineViewTransform(BaseXmlModel):
    typ: Literal["affine"] = attr(name="type")
    name: str = element(tag="Name")
    affine: str = element(tag="affine")


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

class SpimData2(SpimData, tag="SpimData"):
    """
    https://github.com/PreibischLab/multiview-reconstruction/blob/master/src/main/java/net/preibisch/mvrecon/fiji/spimdata/SpimData2.java#L64
    """

    view_interest_points: ViewInterestPoints = element(tag='ViewInterestPoints')
    bounding_boxes: BoundingBoxes = element(tag='BoundingBoxes')
#    point_spread_functions: PointSpreadFunctions
#    stitching_results: StitchingResults
#    intensity_adjustments: IntensityAdjustments 

