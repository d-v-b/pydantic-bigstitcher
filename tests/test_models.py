from xml.etree import ElementTree as etree

from pydantic_xml import BaseXmlModel, element
import pytest
from xmldiff import main
import xmltodict
from xmldiff.actions import DeleteNode
from pydantic_bigstitcher import BasePath, BoundingBoxes, PatternTimePoints, SequenceDescription, SpimData2, ViewInterestPoints, ViewRegistrations, ViewSetup, ViewSetups, ZarrImageLoader, ZGroup
from pydantic_bigstitcher.transforms import AffineViewTransform, HoAffine, flatten_hoaffine, stringify_tuple

def test_simple_model():
  data = """
   <A>
    <B>
      <prop_b>1</prop_b>
    </B>
    <B>
      <prop_b>1</prop_b>
    </B>
    <C>
      <prop_c>1</prop_c>
    </C>
    </A>
   """
  class B(BaseXmlModel):
    prop_b: int = element(tag='prop_b')
    
  class C(BaseXmlModel):
    prop_c: int = element(tag='prop_c')
  class A(BaseXmlModel):
    b: list[B] = element(tag='B') 
    c: list[C] = element(tag='C')

  A.from_xml(data)

def test_decode_zarr_image_loader():
    data = """
    <ImageLoader format="bdv.multimg.zarr" version="1.0">
      <zarr type="absolute">/data/foo_dataset/SPIM.ome.zarr</zarr>
      <zgroups>
        <zgroup setup="0" timepoint="0">
          <path>tile_x_0000_y_0000_z_0000_ch_488.zarr</path>
        </zgroup>
      </zgroups>
    </ImageLoader>
    """
    observed = ZarrImageLoader.from_xml(data)
    observed_xml_str = etree.tostring(etree.fromstring(observed.to_xml()))
    data_xml_str = etree.tostring(etree.fromstring(data))
    diff_result = main.diff_texts(data_xml_str, observed_xml_str)
    assert diff_result == []

def test_decode_zarr_image_loader_2():
    data = """<ImageLoader format="bdv.multimg.zarr" version="1.0">
    <s3bucket>aind-open-data</s3bucket>
    <zarr type="absolute">
    foo_708373_2024-04-02_19-49-38_flatfield-correction_2024-04-15_18-15-40/SPIM.ome.zarr
    </zarr>
    <zgroups>
    <zgroup setup="0" timepoint="0">
    <path>tile_x_0000_y_0000_z_0000_ch_488.zarr</path>
    </zgroup>
    </zgroups>
    </ImageLoader>"""
    observed = ZarrImageLoader.from_xml(data)
    observed_xml_str = etree.tostring(etree.fromstring(observed.to_xml()))
    data_xml_str = etree.tostring(etree.fromstring(data))

    diff_result = main.diff_texts(data_xml_str, observed_xml_str)
    assert diff_result == []


def test_decode_zgroup():
    data = """
        <zgroup setup="0" timepoint="0">
          <path>tile_x_0000_y_0000_z_0000_ch_488.zarr</path>
        </zgroup>"""
    observed = ZGroup.from_xml(data)
    observed_xml_str = etree.tostring(etree.fromstring(observed.to_xml()))
    data_xml_str = etree.tostring(etree.fromstring(data))

    diff_result = main.diff_texts(data_xml_str, observed_xml_str)
    assert diff_result == []


def test_decode_timepoints():
    data = """
    <Timepoints type="pattern">
      <integerpattern>0</integerpattern>
    </Timepoints>
        """
    observed = PatternTimePoints.from_xml(data)
    observed_xml_str = etree.tostring(etree.fromstring(observed.to_xml()))
    data_xml_str = etree.tostring(etree.fromstring(data))

    diff_result = main.diff_texts(data_xml_str, observed_xml_str)
    assert diff_result == []

def test_decode_sequence_description():
    data = """
  <SequenceDescription>
    <ImageLoader format="bdv.multimg.zarr" version="1.0">
      <zarr type="absolute">/data/foo/bar.ome.zarr</zarr>
      <zgroups>
        <zgroup setup="0" timepoint="0">
          <path>tile_x_0000_y_0000_z_0000_ch_488.zarr</path>
        </zgroup>
      </zgroups>
    </ImageLoader>
    <ViewSetups>
      <ViewSetup>
        <id>0</id>
        <name>tile_x_0000_y_0000_z_0000_ch_488</name>
        <size>14192 10640 28672</size>
        <voxelSize>
          <unit>µm</unit>
          <size>0.7480000148631624 0.7479999743009398 1.0</size>
        </voxelSize>
        <attributes>
          <illumination>0</illumination>
          <channel>0</channel>
          <tile>0</tile>
          <angle>0</angle>
        </attributes>
      </ViewSetup>
      <Attributes name="illumination">
        <Illumination>
          <id>0</id>
          <name>0</name>
        </Illumination>
      </Attributes>
      <Attributes name="channel">
        <Channel>
          <id>0</id>
          <name>0</name>
        </Channel>
      </Attributes>
      <Attributes name="tile">
        <Tile>
          <id>0</id>
          <name>tile_x_0000_y_0000_z_0000_ch_488</name>
        </Tile>
      </Attributes>
      <Attributes name="angle">
        <Angle>
          <id>0</id>
          <name>0</name>
        </Angle>
      </Attributes>
    </ViewSetups>
    <Timepoints type="pattern">
      <integerpattern>0</integerpattern>
    </Timepoints>
    <MissingViews />
  </SequenceDescription>
    """
    observed = SequenceDescription.from_xml(data)
    observed_xml_str = etree.tostring(etree.fromstring(observed.to_xml()))
    data_xml_str = etree.tostring(etree.fromstring(data))

    diff_result = main.diff_texts(data_xml_str, observed_xml_str)
    assert diff_result == []

def test_decode_view_interest_points():
    data = """
      <ViewInterestPoints>
        <ViewInterestPointsFile timepoint="0" setup="0" label="beads"
            params="DOG (Spark) s=1.8 t=0.003 overlappingOnly=true min=false max=true downsampleXY=8 downsampleZ=8 minIntensity=0.0 maxIntensity=20000.0">
            tpId_0_viewSetupId_0/beads</ViewInterestPointsFile>
    </ViewInterestPoints>
    """

    observed = ViewInterestPoints.from_xml(data)
    observed_xml_str = etree.tostring(etree.fromstring(observed.to_xml()))
    data_xml_str = etree.tostring(etree.fromstring(data))
    diff_result = main.diff_texts(data_xml_str, observed_xml_str)
    assert diff_result == []


@pytest.mark.parametrize('attribute_path, model_class', [
   ('SequenceDescription', SequenceDescription),
   ('BasePath', BasePath),
   ('ViewRegistrations', ViewRegistrations),
   ])
@pytest.mark.parametrize('bigstitcher_xml', (0,1,2,3), indirect=True)
def test_view_setups(bigstitcher_xml: str, attribute_path: str, model_class: BaseXmlModel):
  from xml.etree import ElementTree
  tree = ElementTree.fromstring(bigstitcher_xml)
  for part in attribute_path.split('/'):
     tree = tree.find(part)
     if tree is None:
        raise ValueError(f'Could not find a node at {attribute_path}')

  subnode_str = etree.tostring(tree)
  model = model_class.from_xml(subnode_str)
  observed = xmltodict.parse(model.to_xml())
  expected = xmltodict.parse(subnode_str)
  assert observed == expected


@pytest.mark.parametrize('bigstitcher_xml', (0,1,2), indirect=True)
def test_encode_decode(bigstitcher_xml: str) -> None:
    model = SpimData2.from_xml(bigstitcher_xml.encode())
    model_xml = model.to_xml()
    data_xml_encoded = bigstitcher_xml.encode()
    diff = main.diff_texts(model_xml, data_xml_encoded)
    # ensure that the diff only contains deletions, i.e. the modeled xml is larger than the real xml
    assert all(isinstance(x, DeleteNode) for x in diff)

def test_transform():
  trs = {'x': -7096.0, 'y': -5320.0, 'z': -28672.0}
  aff = {
      'x': {'x': 1.2, 'y': 0.2, 'z': 0.0},
      'y': {'x': 0.0, 'y': 1.5, 'z': 0.0},
      'z': {'x': 3.0, 'y': 0.0, 'z': 1.0},
      }
  affine_str = f"{aff['x']['x']} {aff['x']['y']} {aff['x']['z']} {trs['x']} {aff['y']['x']} {aff['y']['y']} {aff['y']['z']} {trs['y']} {aff['z']['x']} {aff['z']['y']} {aff['z']['z']} {trs['z']}"
  name = "Translation to Nominal Grid"
  transform_xml = (
      '<ViewTransform type="affine">'
      f'<Name>{name}</Name>'
      f'<affine>{affine_str}</affine>'
      '</ViewTransform>'
    )

  tx_model = AffineViewTransform.from_xml(transform_xml)
  assert tx_model.name== name
  assert tx_model.typ == 'affine'
  tx = tx_model.to_transform()
  assert tx.transform == HoAffine(affine=aff, translation=trs)
  assert stringify_tuple(map(str, flatten_hoaffine(tx.transform, axes_out=('x','y','z')))) == affine_str