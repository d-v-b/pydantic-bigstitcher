from __future__ import annotations

from pydantic_xml import BaseXmlModel, attr, element
import numpy as np

from typing import Iterable, Mapping, TypeVar, TypeAlias, Literal, Generic
from pydantic import BaseModel

T = TypeVar('T', bound=str)

# bigstitcher only represents the 3 classic spatial axes
Axes: TypeAlias = Literal["z", "y", "x"]
axes: tuple[Axes, ...] = ("z", "y", "x")

VectorMap: TypeAlias = Mapping[T, float]
MatrixMap: TypeAlias = Mapping[T, VectorMap[T]]

class HoAffine(BaseModel, Generic[T]):
    """
    Model a homogeneous affine transformation with named axes. The transform is decomposed into
    a translation transform and an affine transform.
    """
    translation: VectorMap[T]
    affine: MatrixMap[T]

class Transform(BaseModel, Generic[T]):
    name: str
    type: str
    transform: HoAffine[T]

def destringify_tuple(data: str) -> tuple[str, ...]:
    return tuple(data.split(' '))

def stringify_tuple(data: Iterable[str]) -> str:
    return ' '.join(data)


class AffineViewTransform(BaseXmlModel, tag='ViewTransform'):
    typ: Literal["affine"] = attr(name="type")
    name: str = element(tag="Name")
    affine: str = element(tag="affine")

    def to_transform(self) -> Transform[Axes]:
        return parse_transform_xyz(self)

def parse_transform_xyz(tx: AffineViewTransform) -> Transform:
    homo_affine_arrayed = np.array(tuple(float(x) for x in destringify_tuple(tx.affine))).reshape(len(axes),len(axes) + 1)
    trans_array = homo_affine_arrayed[:,-1]
    aff_array = homo_affine_arrayed[:, :-1]
    aff_dict = {}
    
    trans_dict: VectorMap[Axes] = {ax: trans_array[idx] for idx, ax in enumerate(reversed(axes))}
    for oidx, oax in enumerate(reversed(axes)):
        aff_dict[oax] = {iax: aff_array[oidx][iidx] for iidx, iax in enumerate(reversed(axes))}
    
    return Transform(
        name=tx.name,
        type=tx.typ,
        transform=
        HoAffine[Axes](
            translation=trans_dict,
            affine=aff_dict
        )
        )

def flatten_hoaffine(tx: HoAffine, axes_out: tuple[str, ...]) -> tuple[float, ...]:
    out: tuple[float, ...] = ()
    for ax_o in axes_out:
        for ax_i in axes_out:
            out += (tx.affine[ax_o][ax_i],)
        out += (tx.translation[ax_o], )
    return out

