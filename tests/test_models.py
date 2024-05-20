from pydantic_bigstitcher import PatternTimePoints, SequenceDescription, SpimData2, ZarrImageLoader, ZGroup
import pytest

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
    _ = SequenceDescription.from_xml(data)

@pytest.mark.xfail
def test_encode_decode(demo_xml: str) -> None:
    model = SpimData2.from_xml(demo_xml)
    assert model.to_xml() == demo_xml

def test_decode_2() -> None:
    data = """<SpimData version="0.2">
    <BasePath type="relative">.</BasePath>
    <SequenceDescription>
    <ImageLoader format="bdv.multimg.zarr" version="1.0">
    <s3bucket>aind-open-data</s3bucket>
    <zarr type="absolute">
    foo_708373_2024-04-02_19-49-38_flatfield-correction_2024-04-15_18-15-40/SPIM.ome.zarr
    </zarr>
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
    <ViewSetup>
    <id>1</id>
    <name>tile_x_0000_y_0001_z_0000_ch_488</name>
    <size>14192 10640 28672</size>
    <voxelSize>
    <unit>µm</unit>
    <size>0.7480000148631624 0.7479999743009398 1.0</size>
    </voxelSize>
    <attributes>
    <illumination>0</illumination>
    <channel>0</channel>
    <tile>1</tile>
    <angle>0</angle>
    </attributes>
    </ViewSetup>
    <ViewSetup>
    <id>2</id>
    <name>tile_x_0000_y_0002_z_0000_ch_488</name>
    <size>14192 10640 28672</size>
    <voxelSize>
    <unit>µm</unit>
    <size>0.7480000148631624 0.7479999743009398 1.0</size>
    </voxelSize>
    <attributes>
    <illumination>0</illumination>
    <channel>0</channel>
    <tile>2</tile>
    <angle>0</angle>
    </attributes>
    </ViewSetup>
    <ViewSetup>
    <id>3</id>
    <name>tile_x_0001_y_0000_z_0000_ch_488</name>
    <size>14192 10640 28672</size>
    <voxelSize>
    <unit>µm</unit>
    <size>0.7480000148631624 0.7479999743009398 1.0</size>
    </voxelSize>
    <attributes>
    <illumination>0</illumination>
    <channel>0</channel>
    <tile>3</tile>
    <angle>0</angle>
    </attributes>
    </ViewSetup>
    <ViewSetup>
    <id>4</id>
    <name>tile_x_0001_y_0001_z_0000_ch_488</name>
    <size>14192 10640 28672</size>
    <voxelSize>
    <unit>µm</unit>
    <size>0.7480000148631624 0.7479999743009398 1.0</size>
    </voxelSize>
    <attributes>
    <illumination>0</illumination>
    <channel>0</channel>
    <tile>4</tile>
    <angle>0</angle>
    </attributes>
    </ViewSetup>
    <ViewSetup>
    <id>5</id>
    <name>tile_x_0001_y_0002_z_0000_ch_488</name>
    <size>14192 10640 28672</size>
    <voxelSize>
    <unit>µm</unit>
    <size>0.7480000148631624 0.7479999743009398 1.0</size>
    </voxelSize>
    <attributes>
    <illumination>0</illumination>
    <channel>0</channel>
    <tile>5</tile>
    <angle>0</angle>
    </attributes>
    </ViewSetup>
    <ViewSetup>
    <id>6</id>
    <name>tile_x_0002_y_0000_z_0000_ch_488</name>
    <size>14192 10640 28672</size>
    <voxelSize>
    <unit>µm</unit>
    <size>0.7480000148631624 0.7479999743009398 1.0</size>
    </voxelSize>
    <attributes>
    <illumination>0</illumination>
    <channel>0</channel>
    <tile>6</tile>
    <angle>0</angle>
    </attributes>
    </ViewSetup>
    <ViewSetup>
    <id>7</id>
    <name>tile_x_0002_y_0001_z_0000_ch_488</name>
    <size>14192 10640 28672</size>
    <voxelSize>
    <unit>µm</unit>
    <size>0.7480000148631624 0.7479999743009398 1.0</size>
    </voxelSize>
    <attributes>
    <illumination>0</illumination>
    <channel>0</channel>
    <tile>7</tile>
    <angle>0</angle>
    </attributes>
    </ViewSetup>
    <ViewSetup>
    <id>8</id>
    <name>tile_x_0002_y_0002_z_0000_ch_488</name>
    <size>14192 10640 28672</size>
    <voxelSize>
    <unit>µm</unit>
    <size>0.7480000148631624 0.7479999743009398 1.0</size>
    </voxelSize>
    <attributes>
    <illumination>0</illumination>
    <channel>0</channel>
    <tile>8</tile>
    <angle>0</angle>
    </attributes>
    </ViewSetup>
    <ViewSetup>
    <id>9</id>
    <name>tile_x_0003_y_0000_z_0000_ch_488</name>
    <size>14192 10640 28672</size>
    <voxelSize>
    <unit>µm</unit>
    <size>0.7480000148631624 0.7479999743009398 1.0</size>
    </voxelSize>
    <attributes>
    <illumination>0</illumination>
    <channel>0</channel>
    <tile>9</tile>
    <angle>0</angle>
    </attributes>
    </ViewSetup>
    <ViewSetup>
    <id>10</id>
    <name>tile_x_0003_y_0001_z_0000_ch_488</name>
    <size>14192 10640 28672</size>
    <voxelSize>
    <unit>µm</unit>
    <size>0.7480000148631624 0.7479999743009398 1.0</size>
    </voxelSize>
    <attributes>
    <illumination>0</illumination>
    <channel>0</channel>
    <tile>10</tile>
    <angle>0</angle>
    </attributes>
    </ViewSetup>
    <ViewSetup>
    <id>11</id>
    <name>tile_x_0003_y_0002_z_0000_ch_488</name>
    <size>14192 10640 28672</size>
    <voxelSize>
    <unit>µm</unit>
    <size>0.7480000148631624 0.7479999743009398 1.0</size>
    </voxelSize>
    <attributes>
    <illumination>0</illumination>
    <channel>0</channel>
    <tile>11</tile>
    <angle>0</angle>
    </attributes>
    </ViewSetup>
    <ViewSetup>
    <id>12</id>
    <name>tile_x_0004_y_0000_z_0000_ch_488</name>
    <size>14192 10640 28672</size>
    <voxelSize>
    <unit>µm</unit>
    <size>0.7480000148631624 0.7479999743009398 1.0</size>
    </voxelSize>
    <attributes>
    <illumination>0</illumination>
    <channel>0</channel>
    <tile>12</tile>
    <angle>0</angle>
    </attributes>
    </ViewSetup>
    <ViewSetup>
    <id>13</id>
    <name>tile_x_0004_y_0001_z_0000_ch_488</name>
    <size>14192 10640 28672</size>
    <voxelSize>
    <unit>µm</unit>
    <size>0.7480000148631624 0.7479999743009398 1.0</size>
    </voxelSize>
    <attributes>
    <illumination>0</illumination>
    <channel>0</channel>
    <tile>13</tile>
    <angle>0</angle>
    </attributes>
    </ViewSetup>
    <ViewSetup>
    <id>14</id>
    <name>tile_x_0004_y_0002_z_0000_ch_488</name>
    <size>14192 10640 28672</size>
    <voxelSize>
    <unit>µm</unit>
    <size>0.7480000148631624 0.7479999743009398 1.0</size>
    </voxelSize>
    <attributes>
    <illumination>0</illumination>
    <channel>0</channel>
    <tile>14</tile>
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
    <MissingViews/>
    </SequenceDescription>
    <ViewRegistrations>
    <ViewRegistration timepoint="0" setup="0">
    <ViewTransform type="affine">
    <Name>InterpolatedAffineModel3D</Name>
    <affine>
    1.0064694598726402 -0.005935317175007711 -0.002340606752535989 -67.19158118915246 -0.002190828085734458 1.027782168030016 0.002481932369365794 300.09290336146523 0.001290833396627382 -0.005145523893176262 1.0023908834260729 -29.018209730401942
    </affine>
    </ViewTransform>
    </ViewRegistration>
    </ViewRegistrations>
    <ViewInterestPoints>
    <ViewInterestPointsFile timepoint="0" setup="0" label="beads" params="DOG (Spark) s=1.8 t=0.003 overlappingOnly=true min=false max=true downsampleXY=8 downsampleZ=8 minIntensity=0.0 maxIntensity=20000.0">tpId_0_viewSetupId_0/beads</ViewInterestPointsFile>
    </ViewInterestPoints>
    <BoundingBoxes/>
    <PointSpreadFunctions/>
    <StitchingResults/>
    <IntensityAdjustments/>
    </SpimData>
    """
    model = SpimData2.from_xml(data)