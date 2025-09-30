from __future__ import annotations

from typing import Literal

from xml.etree.ElementTree import Element, fromstring, tostring
from pydantic import model_validator, PrivateAttr
from pydantic_xml import BaseXmlModel, attr, element

from pydantic_bigstitcher.transform import AffineViewTransform


class BasePath(BaseXmlModel):
    type: Literal["relative", "absolute"] = attr(name="type")
    path: str


class ZGroupA(BaseXmlModel, tag="zgroup"):
    setup: str = attr()
    path: str = element()
    timepoint: str = attr()


class ZGroupB(BaseXmlModel, tag="zgroup"):
    setup: str = attr()
    path: str = element()
    tp: str = attr()
    

class ZGroupC(BaseXmlModel, tag="zgroup"):
    setup: str = attr()
    path: str = attr()
    timepoint: str = attr()
    

class ZGroupD(BaseXmlModel, tag="zgroup"):
    setup: str = attr()
    path: str = attr()
    tp: str = attr()
    indicies: str | None = attr(default=None)

ZGroup = ZGroupA | ZGroupB | ZGroupC | ZGroupD


class ZGroups(BaseXmlModel, tag="zgroups"):
    elements: list[ZGroup] = element(tag="zgroup")


class Zarr(BaseXmlModel):
    type: str = attr(name="type")
    path: str


class N5(BaseXmlModel):
    type: str = attr(name="type")
    path: str


class ZarrImageLoader(BaseXmlModel, tag="ImageLoader", skip_empty=True):
    fmt: str = attr(name="format")
    version: str = attr()
    s3bucket: str | None = element(default=None)
    zarr: Zarr = element(tag="zarr")
    zgroups: ZGroups = element(tag="zgroups")


class BDVN5ImageLoader(BaseXmlModel, tag="ImageLoader", skip_empty=True):
    fmt: str = attr(name="format")
    version: str = attr()
    n5: N5 = element(tag="n5")


class VoxelSize(BaseXmlModel):
    unit: str = element()
    size: str = element()


class ViewSetupAttributes(BaseXmlModel):
    illumination: str = element()
    channel: str = element()
    tile: str = element()
    angle: str = element()


class Camera(BaseXmlModel):
    name: str = element()
    exposure_time: str = element(tag="exposureTime")
    exposure_units: str = element(tag="exposureUnits")


class ViewSetup(BaseXmlModel, search_mode="unordered"):
# class ViewSetup(BaseXmlModel):
    ident: str = element(tag="id")
    name: str = element()
    size: str = element()
    voxel_size: VoxelSize = element(tag="voxelSize")
    camera: Camera | None = element(tag="camera", default=None)
    attributes: ViewSetupAttributes = element(tag="attributes")


class Attribute(BaseXmlModel):
    id: int = element(tag="id")
    name: str = element(tag="name")


class IlluminationAttribute(BaseXmlModel, tag="Attributes"):
    name: Literal["illumination"] = attr(tag="name")
    illumination: list[Attribute] = element(tag="Illumination")


class TileAttribute(BaseXmlModel, tag="Attributes"):
    name: Literal["tile"] = attr(tag="name")
    tile: list[Attribute] = element(tag="Tile")


class AngleAttribute(BaseXmlModel, tag="Attributes"):
    name: Literal["angle"] = attr(tag="name")
    angle: list[Attribute] = element(tag="Angle")


class ChannelAttribute(BaseXmlModel, tag="Attributes"):
    name: Literal["channel"] = attr(tag="name")
    angle: list[Attribute] = element(tag="Channel")


class ViewSetups(BaseXmlModel):
    # the order of the definition of these attributes should match the order of the data in xml
    elements: list[ViewSetup] = element(tag="ViewSetup")
    attributes: list[IlluminationAttribute | TileAttribute | AngleAttribute | ChannelAttribute] = (
        element(tag="Attributes")
    )


class PatternTimePoints(BaseXmlModel, tag="Timepoints"):
    type: Literal["pattern"] = attr(name="type")
    elements: list[str] = element(tag="integerpattern")


class MissingView(BaseXmlModel):
    setup: str = attr()
    timepoint: str = attr()


class MissingViews(BaseXmlModel):
    elements: list[MissingView] = element("MissingView", default=None)


class SequenceDescription(BaseXmlModel, search_mode="unordered"):
    """
    https://github.com/bigdataviewer/spimdata/blob/46c3878baef80cc4170a33012c8281481dbbfcb2/src/main/java/mpicbg/spim/data/generic/sequence/AbstractSequenceDescription.java#L52
    """

    image_loader: ZarrImageLoader | BDVN5ImageLoader | None = element(
        tag="ImageLoader", default=None
    )
    view_setups: ViewSetups | None = element(tag="ViewSetups", default=None)
    time_points: PatternTimePoints | None = element(tag="Timepoints", default=None)
    missing_views: MissingViews | None = element(tag="MissingViews", default=None)


class ViewRegistration(BaseXmlModel):
    """
    https://github.com/bigdataviewer/spimdata/blob/master/src/main/java/mpicbg/spim/data/registration/ViewRegistrations.java#L47
    """

    timepoint: str = attr()
    setup: str = attr()
    view_transforms: list[AffineViewTransform] = element(tag="ViewTransform")


class ViewRegistrations(BaseXmlModel):
    elements: list[ViewRegistration] = element(tag="ViewRegistration")


class SpimData(BaseXmlModel, search_mode="unordered"):
    """
    https://github.com/bigdataviewer/spimdata/blob/46c3878baef80cc4170a33012c8281481dbbfcb2/src/main/java/mpicbg/spim/data/generic/AbstractSpimData.java#L36
    """

    version: Literal["0.2"] = attr(version="0.2")
    base_path: BasePath = element(tag="BasePath")
    sequence_description: SequenceDescription = element(tag="SequenceDescription")
    view_registrations: ViewRegistrations = element(tag="ViewRegistrations")


class ViewInterestPointsFile(BaseXmlModel):
    timepoint: str = attr()
    setup: str = attr()
    label: str = attr()
    params: str = attr()
    path: str


class ViewInterestPoints(BaseXmlModel):
    elements: list[ViewInterestPointsFile] | None = element(
        tag="ViewInterestPointsFile", default=None
    )


class BoundingBox(BaseXmlModel):
    """
    https://github.com/PreibischLab/multiview-reconstruction/blob/master/src/main/java/net/preibisch/mvrecon/fiji/spimdata/boundingbox/BoundingBox.java#L30
    """

    title: str = attr()
    minimum: str = attr(name="min")
    maximum: str = attr(name="max")


class BoundingBoxes(BaseXmlModel):
    """
    https://github.com/PreibischLab/multiview-reconstruction/blob/master/src/main/java/net/preibisch/mvrecon/fiji/spimdata/boundingbox/BoundingBoxes.java#L29
    """

    elements: list[BoundingBox] | None = element(tag="BoundingBox", default=None)


class PointSpreadFunctions(BaseXmlModel): ...


class StitchingResults(BaseXmlModel): ...


class IntensityAdjustments(BaseXmlModel): ...


# Reusable decorator to preserve unknown direct child XML elements
def with_extra_children(known_tags: set[str]):
    """
    Decorator to add automatic preservation of unknown direct child XML elements.
    known_tags: set of tag names that the model explicitly handles.
    """
    def decorator(cls):
        cls._KNOWN_TAGS = set(known_tags)

        original_from_xml = getattr(cls, "from_xml", None)
        original_to_xml = getattr(cls, "to_xml", None)

        @classmethod
        def from_xml(decorated_cls, data: str | bytes, **kwargs):
            root = fromstring(data)
            extras: list[Element] = []
            for child in list(root):
                if child.tag not in decorated_cls._KNOWN_TAGS:
                    extras.append(child)
                    root.remove(child)
            # parse only known subtree
            parsed = original_from_xml(tostring(root), **kwargs)
            setattr(parsed, "_extra", extras)
            return parsed

        def to_xml(self, *args, **kwargs):
            base_xml = original_to_xml(self, *args, **kwargs)
            root = fromstring(base_xml)
            extras = getattr(self, "_extra", [])
            if isinstance(extras, list):
                for child in extras:
                    root.append(child)
            return tostring(root, encoding="unicode")

        cls.from_xml = from_xml
        cls.to_xml = to_xml

        cls._extra = PrivateAttr(default_factory=list)

        return cls
    return decorator


@with_extra_children(known_tags={
    "BasePath",
    "SequenceDescription",
    "ViewRegistrations",
    "ViewInterestPoints",
    "BoundingBoxes",
    "PointSpreadFunctions",
    "StitchingResults",
    "IntensityAdjustments",
})
class SpimData2(SpimData, tag="SpimData"):
    """
    https://github.com/PreibischLab/multiview-reconstruction/blob/master/src/main/java/net/preibisch/mvrecon/fiji/spimdata/SpimData2.java#L64

    Unknown direct child XML elements are preserved via the with_extra_children decorator.
    """
    model_config = {"arbitrary_types_allowed": True}

    view_interest_points: ViewInterestPoints | None = element(
        tag="ViewInterestPoints", default=None
    )
    bounding_boxes: BoundingBoxes | None = element(tag="BoundingBoxes", default=None)
    point_spread_functions: PointSpreadFunctions | None = element(
        tag="PointSpreadFunctions", default=None
    )
    stitching_results: StitchingResults | None = element(tag="StitchingResults", default=None)
    intensity_adjustments: IntensityAdjustments | None = element(
        tag="IntensityAdjustments", default=None
    )
