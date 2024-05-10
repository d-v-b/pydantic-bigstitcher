from pydantic_bigstitcher import PatternTimePoints, SequenceDescription, SpimData2, ZarrImageLoader, ZGroup


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


def test_decode(demo_xml: str) -> None:
    _ = SpimData2.from_xml(demo_xml)
