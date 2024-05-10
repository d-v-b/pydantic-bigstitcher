demo_xml = """
<?xml version="1.0" encoding="UTF-8"?>
<SpimData version="0.2">
  <BasePath type="relative">.</BasePath>
  <SequenceDescription>
    <ImageLoader format="bdv.multimg.zarr" version="1.0">
      <zarr type="absolute">/data/foo_dataset/SPIM.ome.zarr</zarr>
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
          <path>tile_x_0004_y_0002_z_0000_ch_488.zarr</path>
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
        <Tile>
          <id>1</id>
          <name>tile_x_0000_y_0001_z_0000_ch_488</name>
        </Tile>
        <Tile>
          <id>2</id>
          <name>tile_x_0000_y_0002_z_0000_ch_488</name>
        </Tile>
        <Tile>
          <id>3</id>
          <name>tile_x_0001_y_0000_z_0000_ch_488</name>
        </Tile>
        <Tile>
          <id>4</id>
          <name>tile_x_0001_y_0001_z_0000_ch_488</name>
        </Tile>
        <Tile>
          <id>5</id>
          <name>tile_x_0001_y_0002_z_0000_ch_488</name>
        </Tile>
        <Tile>
          <id>6</id>
          <name>tile_x_0002_y_0000_z_0000_ch_488</name>
        </Tile>
        <Tile>
          <id>7</id>
          <name>tile_x_0002_y_0001_z_0000_ch_488</name>
        </Tile>
        <Tile>
          <id>8</id>
          <name>tile_x_0002_y_0002_z_0000_ch_488</name>
        </Tile>
        <Tile>
          <id>9</id>
          <name>tile_x_0003_y_0000_z_0000_ch_488</name>
        </Tile>
        <Tile>
          <id>10</id>
          <name>tile_x_0003_y_0001_z_0000_ch_488</name>
        </Tile>
        <Tile>
          <id>11</id>
          <name>tile_x_0003_y_0002_z_0000_ch_488</name>
        </Tile>
        <Tile>
          <id>12</id>
          <name>tile_x_0004_y_0000_z_0000_ch_488</name>
        </Tile>
        <Tile>
          <id>13</id>
          <name>tile_x_0004_y_0001_z_0000_ch_488</name>
        </Tile>
        <Tile>
          <id>14</id>
          <name>tile_x_0004_y_0002_z_0000_ch_488</name>
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
  <ViewRegistrations>
    <ViewRegistration timepoint="0" setup="0">
      <ViewTransform type="affine">
        <Name>AffineModel3D regularized with an RigidModel3D, lambda = 0.1</Name>
        <affine>0.9990407284329631 0.006294762826228883 -0.0018936408042257633 -35.4616465867072 -0.004211752487216202 0.9997544969400599 -3.685859256398284E-4 11.822642190798302 0.0024962860876907864 0.0011824161816296971 0.9999449502009171 61.301084226971604</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>TranslationModel3D</Name>
        <affine>1.0 0.0 0.0 16.143134199814995 0.0 1.0 0.0 62.808413727239895 0.0 0.0 1.0 57.03870763658597</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>Translation to Nominal Grid</Name>
        <affine>1.0 0.0 0.0 -7096.0 0.0 1.0 0.0 -23408.0003 0.0 0.0 1.0 -28672.0</affine>
      </ViewTransform>
    </ViewRegistration>
    <ViewRegistration timepoint="0" setup="1">
      <ViewTransform type="affine">
        <Name>AffineModel3D regularized with an RigidModel3D, lambda = 0.1</Name>
        <affine>0.9997011949686007 0.0057135025842539764 -0.0018156872345211788 -39.537231501966026 -0.005078906168030526 0.9994600543539546 8.770014357758721E-4 25.940773338060655 0.0018250636979544302 -0.0015373381661381073 0.9994369993192339 14.521111460745889</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>TranslationModel3D</Name>
        <affine>1.0 0.0 0.0 -1.0754098745620695 0.0 1.0 0.0 2.897698529347508 0.0 0.0 1.0 2.2279627875414008</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>Translation to Nominal Grid</Name>
        <affine>1.0 0.0 0.0 -7096.0 0.0 1.0 0.0 -14364.0011 0.0 0.0 1.0 -28672.0</affine>
      </ViewTransform>
    </ViewRegistration>
    <ViewRegistration timepoint="0" setup="2">
      <ViewTransform type="affine">
        <Name>AffineModel3D regularized with an RigidModel3D, lambda = 0.1</Name>
        <affine>1.0005905673971454 0.006412476235022581 -2.0898004686118214E-4 -6.882247305717769 -0.006640515087785624 1.0006041976808946 0.001069367575059085 36.19679755714826 4.447101191215066E-5 -0.003030998890847906 1.0002768488334746 25.213536190523985</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>TranslationModel3D</Name>
        <affine>1.0 0.0 0.0 -8.989298727489427 0.0 1.0 0.0 -53.26993785541072 0.0 0.0 1.0 -65.48247229839944</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>Translation to Nominal Grid</Name>
        <affine>1.0 0.0 0.0 -7096.0 0.0 1.0 0.0 -5320.0003 0.0 0.0 1.0 -28672.0</affine>
      </ViewTransform>
    </ViewRegistration>
    <ViewRegistration timepoint="0" setup="3">
      <ViewTransform type="affine">
        <Name>AffineModel3D regularized with an RigidModel3D, lambda = 0.1</Name>
        <affine>0.9997377963914404 -0.001535510820803689 -7.846423471881332E-4 -45.652727376229166 8.467650195800372E-4 0.9993540226803085 4.930488388557084E-4 14.889697979281221 6.461368076833254E-4 9.043603604862002E-4 0.9993008732953462 7.177818684301524</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>TranslationModel3D</Name>
        <affine>1.0 0.0 0.0 29.00791550629765 0.0 1.0 0.0 58.22389606836077 0.0 0.0 1.0 54.340164141171044</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>Translation to Nominal Grid</Name>
        <affine>1.0 0.0 0.0 -19159.2002 0.0 1.0 0.0 -23408.0003 0.0 0.0 1.0 -28672.0</affine>
      </ViewTransform>
    </ViewRegistration>
    <ViewRegistration timepoint="0" setup="4">
      <ViewTransform type="affine">
        <Name>AffineModel3D regularized with an RigidModel3D, lambda = 0.1</Name>
        <affine>0.9998471277461982 6.180937321114939E-4 3.5157427233897766E-4 9.442066091897836 -3.114354292800365E-5 0.9995287053919484 5.613751287532819E-5 -2.760765537296942 -1.693655488560358E-4 -4.4214223932252054E-4 1.0000675526668572 -3.2901178271085243</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>TranslationModel3D</Name>
        <affine>1.0 0.0 0.0 -2.277692367350028 0.0 1.0 0.0 0.35164175487170723 0.0 0.0 1.0 -4.57972604731367</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>Translation to Nominal Grid</Name>
        <affine>1.0 0.0 0.0 -19159.2002 0.0 1.0 0.0 -14364.0011 0.0 0.0 1.0 -28672.0</affine>
      </ViewTransform>
    </ViewRegistration>
    <ViewRegistration timepoint="0" setup="5">
      <ViewTransform type="affine">
        <Name>AffineModel3D regularized with an RigidModel3D, lambda = 0.1</Name>
        <affine>1.0004515454982839 4.001039878961502E-4 2.261439293137072E-4 13.30364188809012 -4.2718552823626095E-4 1.0008114367951453 2.1023600631153597E-5 -2.1301475486843886 -3.16584225553764E-4 -0.0019680202828332724 1.0002438307764367 -8.737983899930217</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>TranslationModel3D</Name>
        <affine>1.0 0.0 0.0 -20.050656294788496 0.0 1.0 0.0 -44.8663350348188 0.0 0.0 1.0 -52.572395550681904</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>Translation to Nominal Grid</Name>
        <affine>1.0 0.0 0.0 -19159.2002 0.0 1.0 0.0 -5320.0003 0.0 0.0 1.0 -28672.0</affine>
      </ViewTransform>
    </ViewRegistration>
    <ViewRegistration timepoint="0" setup="6">
      <ViewTransform type="affine">
        <Name>AffineModel3D regularized with an RigidModel3D, lambda = 0.1</Name>
        <affine>0.9996462797264349 6.768871031500913E-4 5.531903139723655E-5 1.3555930815757455 5.613961727412094E-4 0.9992030354663004 3.377863695846844E-4 7.669320156170571 2.1136493320542352E-4 0.0017232708888473378 0.9996685359466916 23.458958478225437</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>TranslationModel3D</Name>
        <affine>1.0 0.0 0.0 24.850038400181802 0.0 1.0 0.0 61.52162034592766 0.0 0.0 1.0 43.44689732267216</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>Translation to Nominal Grid</Name>
        <affine>1.0 0.0 0.0 -31222.3997 0.0 1.0 0.0 -23408.0003 0.0 0.0 1.0 -28672.0</affine>
      </ViewTransform>
    </ViewRegistration>
    <ViewRegistration timepoint="0" setup="7">
      <ViewTransform type="affine">
        <Name>AffineModel3D regularized with an RigidModel3D, lambda = 0.1</Name>
        <affine>1.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 1.0 0.0</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>TranslationModel3D</Name>
        <affine>1.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 1.0 0.0</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>Translation to Nominal Grid</Name>
        <affine>1.0 0.0 0.0 -31222.3997 0.0 1.0 0.0 -14364.0011 0.0 0.0 1.0 -28672.0</affine>
      </ViewTransform>
    </ViewRegistration>
    <ViewRegistration timepoint="0" setup="8">
      <ViewTransform type="affine">
        <Name>AffineModel3D regularized with an RigidModel3D, lambda = 0.1</Name>
        <affine>1.0004807838200651 -3.14262337320284E-4 -8.603637816452575E-5 8.337695442542797 -1.246659377950418E-4 1.0007783195342626 2.2779086785465155E-4 5.596436361067468 -5.7999407929057414E-5 -0.0012553641195780921 0.9999297034679016 -8.689544782551057</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>TranslationModel3D</Name>
        <affine>1.0 0.0 0.0 -19.309317739742255 0.0 1.0 0.0 -47.63659668013679 0.0 0.0 1.0 -48.5487178031035</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>Translation to Nominal Grid</Name>
        <affine>1.0 0.0 0.0 -31222.3997 0.0 1.0 0.0 -5320.0 0.0 0.0 1.0 -28672.0</affine>
      </ViewTransform>
    </ViewRegistration>
    <ViewRegistration timepoint="0" setup="9">
      <ViewTransform type="affine">
        <Name>AffineModel3D regularized with an RigidModel3D, lambda = 0.1</Name>
        <affine>0.9995339755067989 -0.001816120193531207 -0.0014584566612401415 -74.18895816043022 0.0014297880328536826 0.9994291977057244 5.998254648643864E-4 42.68142724216666 0.002262088078919027 2.1227132867179463E-4 1.0004238768347942 77.6534047698134</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>TranslationModel3D</Name>
        <affine>1.0 0.0 0.0 100.88963064627751 0.0 1.0 0.0 19.234505707800054 0.0 0.0 1.0 14.840311744646897</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>Translation to Nominal Grid</Name>
        <affine>1.0 0.0 0.0 -43285.5993 0.0 1.0 0.0 -23407.9988 0.0 0.0 1.0 -28672.0</affine>
      </ViewTransform>
    </ViewRegistration>
    <ViewRegistration timepoint="0" setup="10">
      <ViewTransform type="affine">
        <Name>AffineModel3D regularized with an RigidModel3D, lambda = 0.1</Name>
        <affine>1.0001518889376402 -0.0015688711853567472 -0.0020890621033956705 -58.16943971800367 0.0012351206503306855 1.0000202586866898 2.476808027360136E-4 38.436694916404974 0.0023680859585749003 -4.614678887983196E-4 0.9998236267161411 63.2578130433807</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>TranslationModel3D</Name>
        <affine>1.0 0.0 0.0 68.39085637155222 0.0 1.0 0.0 -45.071750663558305 0.0 0.0 1.0 -48.427730994191734</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>Translation to Nominal Grid</Name>
        <affine>1.0 0.0 0.0 -43285.5993 0.0 1.0 0.0 -14364.0002 0.0 0.0 1.0 -28672.0</affine>
      </ViewTransform>
    </ViewRegistration>
    <ViewRegistration timepoint="0" setup="11">
      <ViewTransform type="affine">
        <Name>AffineModel3D regularized with an RigidModel3D, lambda = 0.1</Name>
        <affine>1.0008223236276133 -0.0018027389095623815 -0.0021193369380708765 -35.216653928339205 8.036925811576193E-4 1.0008891000574098 3.3257013049869765E-4 27.899497929779 0.002344202195636627 -0.0019297133838478923 1.0001030775323667 59.58507108967865</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>TranslationModel3D</Name>
        <affine>1.0 0.0 0.0 38.82806274246832 0.0 1.0 0.0 -87.17629088402282 0.0 0.0 1.0 -96.44938488192383</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>Translation to Nominal Grid</Name>
        <affine>1.0 0.0 0.0 -43285.5993 0.0 1.0 0.0 -5320.0 0.0 0.0 1.0 -28672.0</affine>
      </ViewTransform>
    </ViewRegistration>
    <ViewRegistration timepoint="0" setup="12">
      <ViewTransform type="affine">
        <Name>AffineModel3D regularized with an RigidModel3D, lambda = 0.1</Name>
        <affine>0.9996714262819602 -0.007064675795275623 -0.005767986319960421 -185.16645086693026 0.004811893779500349 1.0030828638981704 0.0024295775672808686 227.3429164995418 0.006602825865129266 -0.0025775943424044927 1.0000202614760607 186.66849733729705</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>TranslationModel3D</Name>
        <affine>1.0 0.0 0.0 105.80386118985189 0.0 1.0 0.0 18.431134697048037 0.0 0.0 1.0 2.0667254727759428</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>Translation to Nominal Grid</Name>
        <affine>1.0 0.0 0.0 -55348.7988 0.0 1.0 0.0 -23407.9988 0.0 0.0 1.0 -28672.0</affine>
      </ViewTransform>
    </ViewRegistration>
    <ViewRegistration timepoint="0" setup="13">
      <ViewTransform type="affine">
        <Name>AffineModel3D regularized with an RigidModel3D, lambda = 0.1</Name>
        <affine>0.9996561496770723 -0.006448633193306039 -0.00613142043428698 -182.69485473838483 0.0061989765185218445 1.0002030197077871 0.003123813391602593 261.4872479558257 0.006145729176284897 -0.0033056403309336805 0.9999424849864433 154.70702984423872</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>TranslationModel3D</Name>
        <affine>1.0 0.0 0.0 67.80153994659486 0.0 1.0 0.0 -42.05790466137023 0.0 0.0 1.0 -46.14816359271754</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>Translation to Nominal Grid</Name>
        <affine>1.0 0.0 0.0 -55348.7988 0.0 1.0 0.0 -14364.0002 0.0 0.0 1.0 -28672.0</affine>
      </ViewTransform>
    </ViewRegistration>
    <ViewRegistration timepoint="0" setup="14">
      <ViewTransform type="affine">
        <Name>AffineModel3D regularized with an RigidModel3D, lambda = 0.1</Name>
        <affine>1.0003479470170809 -0.005947813917623783 -0.006245371853781449 -149.67401826240547 0.006009390592580764 1.0007020406194167 0.0029176518201615106 252.1125820820771 0.006296695387376433 -0.004740397443144695 0.9999390684875037 155.01774848850386</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>TranslationModel3D</Name>
        <affine>1.0 0.0 0.0 34.797806836344535 0.0 1.0 0.0 -90.89368887659293 0.0 0.0 1.0 -87.09514971224417</affine>
      </ViewTransform>
      <ViewTransform type="affine">
        <Name>Translation to Nominal Grid</Name>
        <affine>1.0 0.0 0.0 -55348.7988 0.0 1.0 0.0 -5320.0 0.0 0.0 1.0 -28672.0</affine>
      </ViewTransform>
    </ViewRegistration>
  </ViewRegistrations>
  <ViewInterestPoints>
    <ViewInterestPointsFile timepoint="0" setup="0" label="beads" params="DOG s=4.0 t=0.001 min=false max=true imageSigmaX=0.5 imageSigmaY=0.5 imageSigmaZ=0.5 downsampleXYIndex=0 downsampleZ=4 minIntensity=0.0 maxIntensity=2000.0">tpId_0_viewSetupId_0/beads</ViewInterestPointsFile>
    <ViewInterestPointsFile timepoint="0" setup="1" label="beads" params="DOG s=4.0 t=0.001 min=false max=true imageSigmaX=0.5 imageSigmaY=0.5 imageSigmaZ=0.5 downsampleXYIndex=0 downsampleZ=4 minIntensity=0.0 maxIntensity=2000.0">tpId_0_viewSetupId_1/beads</ViewInterestPointsFile>
    <ViewInterestPointsFile timepoint="0" setup="2" label="beads" params="DOG s=4.0 t=0.001 min=false max=true imageSigmaX=0.5 imageSigmaY=0.5 imageSigmaZ=0.5 downsampleXYIndex=0 downsampleZ=4 minIntensity=0.0 maxIntensity=2000.0">tpId_0_viewSetupId_2/beads</ViewInterestPointsFile>
    <ViewInterestPointsFile timepoint="0" setup="3" label="beads" params="DOG s=4.0 t=0.001 min=false max=true imageSigmaX=0.5 imageSigmaY=0.5 imageSigmaZ=0.5 downsampleXYIndex=0 downsampleZ=4 minIntensity=0.0 maxIntensity=2000.0">tpId_0_viewSetupId_3/beads</ViewInterestPointsFile>
    <ViewInterestPointsFile timepoint="0" setup="4" label="beads" params="DOG s=4.0 t=0.001 min=false max=true imageSigmaX=0.5 imageSigmaY=0.5 imageSigmaZ=0.5 downsampleXYIndex=0 downsampleZ=4 minIntensity=0.0 maxIntensity=2000.0">tpId_0_viewSetupId_4/beads</ViewInterestPointsFile>
    <ViewInterestPointsFile timepoint="0" setup="5" label="beads" params="DOG s=4.0 t=0.001 min=false max=true imageSigmaX=0.5 imageSigmaY=0.5 imageSigmaZ=0.5 downsampleXYIndex=0 downsampleZ=4 minIntensity=0.0 maxIntensity=2000.0">tpId_0_viewSetupId_5/beads</ViewInterestPointsFile>
    <ViewInterestPointsFile timepoint="0" setup="6" label="beads" params="DOG s=4.0 t=0.001 min=false max=true imageSigmaX=0.5 imageSigmaY=0.5 imageSigmaZ=0.5 downsampleXYIndex=0 downsampleZ=4 minIntensity=0.0 maxIntensity=2000.0">tpId_0_viewSetupId_6/beads</ViewInterestPointsFile>
    <ViewInterestPointsFile timepoint="0" setup="7" label="beads" params="DOG s=4.0 t=0.001 min=false max=true imageSigmaX=0.5 imageSigmaY=0.5 imageSigmaZ=0.5 downsampleXYIndex=0 downsampleZ=4 minIntensity=0.0 maxIntensity=2000.0">tpId_0_viewSetupId_7/beads</ViewInterestPointsFile>
    <ViewInterestPointsFile timepoint="0" setup="8" label="beads" params="DOG s=4.0 t=0.001 min=false max=true imageSigmaX=0.5 imageSigmaY=0.5 imageSigmaZ=0.5 downsampleXYIndex=0 downsampleZ=4 minIntensity=0.0 maxIntensity=2000.0">tpId_0_viewSetupId_8/beads</ViewInterestPointsFile>
    <ViewInterestPointsFile timepoint="0" setup="9" label="beads" params="DOG s=4.0 t=0.001 min=false max=true imageSigmaX=0.5 imageSigmaY=0.5 imageSigmaZ=0.5 downsampleXYIndex=0 downsampleZ=4 minIntensity=0.0 maxIntensity=2000.0">tpId_0_viewSetupId_9/beads</ViewInterestPointsFile>
    <ViewInterestPointsFile timepoint="0" setup="10" label="beads" params="DOG s=4.0 t=0.001 min=false max=true imageSigmaX=0.5 imageSigmaY=0.5 imageSigmaZ=0.5 downsampleXYIndex=0 downsampleZ=4 minIntensity=0.0 maxIntensity=2000.0">tpId_0_viewSetupId_10/beads</ViewInterestPointsFile>
    <ViewInterestPointsFile timepoint="0" setup="11" label="beads" params="DOG s=4.0 t=0.001 min=false max=true imageSigmaX=0.5 imageSigmaY=0.5 imageSigmaZ=0.5 downsampleXYIndex=0 downsampleZ=4 minIntensity=0.0 maxIntensity=2000.0">tpId_0_viewSetupId_11/beads</ViewInterestPointsFile>
    <ViewInterestPointsFile timepoint="0" setup="12" label="beads" params="DOG s=4.0 t=0.001 min=false max=true imageSigmaX=0.5 imageSigmaY=0.5 imageSigmaZ=0.5 downsampleXYIndex=0 downsampleZ=4 minIntensity=0.0 maxIntensity=2000.0">tpId_0_viewSetupId_12/beads</ViewInterestPointsFile>
    <ViewInterestPointsFile timepoint="0" setup="13" label="beads" params="DOG s=4.0 t=0.001 min=false max=true imageSigmaX=0.5 imageSigmaY=0.5 imageSigmaZ=0.5 downsampleXYIndex=0 downsampleZ=4 minIntensity=0.0 maxIntensity=2000.0">tpId_0_viewSetupId_13/beads</ViewInterestPointsFile>
    <ViewInterestPointsFile timepoint="0" setup="14" label="beads" params="DOG s=4.0 t=0.001 min=false max=true imageSigmaX=0.5 imageSigmaY=0.5 imageSigmaZ=0.5 downsampleXYIndex=0 downsampleZ=4 minIntensity=0.0 maxIntensity=2000.0">tpId_0_viewSetupId_14/beads</ViewInterestPointsFile>
  </ViewInterestPoints>
  <BoundingBoxes />
  <PointSpreadFunctions />
  <StitchingResults />
  <IntensityAdjustments />
</SpimData>
"""  # noqa: E501
