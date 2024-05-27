from pydantic_bigstitcher import PatternTimePoints, SequenceDescription, SpimData2, ZarrImageLoader, ZGroup
import pytest
from xml.etree import ElementTree as etree
from xmldiff import main

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
    ZarrImageLoader.from_xml(data)

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
    <zgroup setup="1" timepoint="0">
    <path>tile_x_0000_y_0001_z_0000_ch_488.zarr</path>
    </zgroup>
    <zgroup setup="2" timepoint="0">
    <path>tile_x_0000_y_0002_z_0000_ch_488.zarr</path>
    </zgroup>
    <zgroup setup="3" timepoint="0">
    <path>tile_x_0001_y_0000_z_0000_ch_488.zarr</path>
    </zgroup>
    <zgroup setup="4" timepoint="0">
    <path>tile_x_0001_y_0001_z_0000_ch_488.zarr</path>
    </zgroup>
    <zgroup setup="5" timepoint="0">
    <path>tile_x_0001_y_0002_z_0000_ch_488.zarr</path>
    </zgroup>
    <zgroup setup="6" timepoint="0">
    <path>tile_x_0002_y_0000_z_0000_ch_488.zarr</path>
    </zgroup>
    <zgroup setup="7" timepoint="0">
    <path>tile_x_0002_y_0001_z_0000_ch_488.zarr</path>
    </zgroup>
    <zgroup setup="8" timepoint="0">
    <path>tile_x_0002_y_0002_z_0000_ch_488.zarr</path>
    </zgroup>
    <zgroup setup="9" timepoint="0">
    <path>tile_x_0003_y_0000_z_0000_ch_488.zarr</path>
    </zgroup>
    <zgroup setup="10" timepoint="0">
    <path>tile_x_0003_y_0001_z_0000_ch_488.zarr</path>
    </zgroup>
    <zgroup setup="11" timepoint="0">
    <path>tile_x_0003_y_0002_z_0000_ch_488.zarr</path>
    </zgroup>
    <zgroup setup="12" timepoint="0">
    <path>tile_x_0004_y_0000_z_0000_ch_488.zarr</path>
    </zgroup>
    <zgroup setup="13" timepoint="0">
    <path>tile_x_0004_y_0001_z_0000_ch_488.zarr</path>
    </zgroup>
    <zgroup setup="14" timepoint="0">
    </zgroup>
    </zgroups>
    </ImageLoader>"""
    ZarrImageLoader.from_xml(data)


def test_decode_zgroup():
    data = """
        <zgroup setup="0" timepoint="0">
          <path>tile_x_0000_y_0000_z_0000_ch_488.zarr</path>
        </zgroup>"""
    ZGroup.from_xml(data)


def test_decode_timepoints():
    data = """
    <Timepoints type="pattern">
      <integerpattern>0</integerpattern>
    </Timepoints>
        """
    PatternTimePoints.from_xml(data)


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

@pytest.mark.xfail
def test_encode_decode(demo_xml_0: str) -> None:
    model = SpimData2.from_xml(demo_xml_0)
    assert model.to_xml() == demo_xml_0

def test_decode_2(demo_xml_0) -> None:
    model = SpimData2.from_xml(demo_xml_0)
    model_xml = model.to_xml()

    assert model_xml == demo_xml_0