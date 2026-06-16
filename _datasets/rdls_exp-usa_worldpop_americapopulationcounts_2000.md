---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop, University of Southampton, UK
    url: https://data.humdata.org/dataset/worldpop-population-counts-for-united-states-of-america
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-united-states-of-america
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-united-states-of-america
dataset_id: rdls_exp-usa_worldpop_americapopulationcounts_2000
description: 'WorldPop produces different types of gridded population count datasets,
  depending on the methods used and end application. Please make sure you have read
  our Mapping Populations overview page before choosing and downloading a dataset.
  Bespoke methods used to produce datasets for specific individual countries are available
  through the WorldPop Open Population Repository (WOPR) link below. These are 100m
  resolution gridded population estimates using customized methods ('' bottom-up ''
  and/or '' top-down '') developed for the latest data available from each country.
  They can also be visualised and explored through the woprVision App . The remaining
  datasets in the links below are produced using the '' top-down '' method, with either
  the unconstrained or constrained top-down disaggregation method used. Please make
  sure you read the Top-down estimation modelling overview page to decide on which
  datasets best meet your needs. Datasets are available to download in Geotiff and
  ASCII XYZ format at a resolution of 3 and 30 arc-seconds (approximately 100m and
  1km at the equator, respectively): - Unconstrained individual countries 2000-2020
  ( 1km resolution ): Consistent 1km resolution population count datasets created
  using unconstrained top-down methods for all countries of the World for each year
  2000-2020. - Unconstrained individual countries 2000-2020 ( 100m resolution ): Consistent
  100m resolution population count datasets created using unconstrained top-down methods
  for all countries of the World for each year 2000-2020. - Unconstrained individual
  countries 2000-2020 UN adjusted ( 100m resolution ): Consistent 100m resolution
  population count datasets created using unconstrained top-down methods for all countries
  of the World for each year 2000-2020 and adjusted to match United Nations national
  population estimates (UN 2019) -Unconstrained individual countries 2000-2020 UN
  adjusted ( 1km resolution ): Consistent 1km resolution population count datasets
  created using unconstrained top-down methods for all countries of the World for
  each year 2000-2020 and adjusted to match United Nations national population estimates
  (UN 2019). -Unconstrained global mosaics 2000-2020 ( 1km resolution ): Mosaiced
  1km resolution versions of the ''Unconstrained individual countries 2000-2020''
  datasets. -Constrained individual countries 2020 ( 100m resolution ): Consistent
  100m resolution population count datasets created using constrained top-down methods
  for all countries of the World for 2020. -Constrained individual countries 2020
  UN adjusted ( 100m resolution ): Consistent 100m resolution population count datasets
  created using constrained top-down methods for all countries of the World for 2020
  and adjusted to match United Nations national population estimates (UN 2019). Older
  datasets produced for specific individual countries and continents, using a set
  of tailored geospatial inputs and differing ''top-down'' methods and time periods
  are still available for download here: Individual countries and Whole Continent
  . Data for earlier dates is available directly from WorldPop. WorldPop (www.worldpop.org
  - School of Geography and Environmental Science, University of Southampton; Department
  of Geography and Geosciences, University of Louisville; Departement de Geographie,
  Universite de Namur) and Center for International Earth Science Information Network
  (CIESIN), Columbia University (2018). Global High Resolution Population Denominators
  Project - Funded by The Bill and Melinda Gates Foundation (OPP1134076). https://dx.doi.org/10.5258/SOTON/WP00645.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-for-united-states-of-america]'
details: null
exposure:
- asset_type:
    description: Gridded population counts at 1km resolution for the United States,
      adjusted to official census totals
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: WorldPop produced gridded population estimates using bespoke country-specific
    methods applied to census and ancillary data. The resulting raster datasets represent
    estimated total population per grid cell at 1km resolution (30 arc-seconds), projected
    in WGS84, with multiple variants provided (UN-adjusted and constrained versions)
    for different analytical applications in disaster risk assessment.
  sources:
  - id: source_1
    license: null
    name: WorldPop, University of Southampton, UK
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/worldpop-population-counts-for-united-states-of-america
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://doi.org/10.1371/journal.pone.0107042-
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://doi.org/10.1016/j.compenvurbsys.2019.101444-
- author_names: null
  date_published: null
  doi: null
  id: reference_3
  name: Methodology documentation
  url: https://dx.doi.org/10.5258/SOTON/WP00665
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2020, United States of America)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/USA/usa_ppp_2020.tif
  format: null
  id: resource_b90d9122
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2019, United States of America)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/USA/usa_ppp_2019.tif
  format: null
  id: resource_df71b45c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2018, United States of America)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/USA/usa_ppp_2018.tif
  format: null
  id: resource_4f0f4c77
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2017, United States of America)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/USA/usa_ppp_2017.tif
  format: null
  id: resource_4c381b41
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2016, United States of America)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/USA/usa_ppp_2016.tif
  format: null
  id: resource_fc4cc2a9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/USA/usa_ppp_2020_UNadj.tif
  format: null
  id: resource_16d78859
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2020_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/USA/usa_ppp_2019_UNadj.tif
  format: null
  id: resource_f2582afb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2019_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/USA/usa_ppp_2018_UNadj.tif
  format: null
  id: resource_c712ca65
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2018_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/USA/usa_ppp_2017_UNadj.tif
  format: null
  id: resource_515b5e23
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2017_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/USA/usa_ppp_2016_UNadj.tif
  format: null
  id: resource_f38af0b0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2016_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2020, United States)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/BSGM/USA/usa_ppp_2020_constrained.tif
  format: null
  id: resource_406a4112
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2020_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/BSGM/USA/usa_ppp_2020_UNadj_constrained.tif
  format: null
  id: resource_ef930a07
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2020_UNadj_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2020 United States)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/USA/usa_ppp_2020_1km_Aggregated.tif
  format: null
  id: resource_25063302
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2020_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2020 United States)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/USA/usa_ppp_2020_1km_ASCII_XYZ.zip
  format: null
  id: resource_926a7ecf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2020_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2020 United States)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/USA/50_US_states_1km_2020.zip
  format: null
  id: resource_40f52525
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 50_US_states_1km_2020.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/USA/usa_ppp_2020_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_2590f02c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2020_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/USA/usa_ppp_2020_1km_Aggregated_UNadj.tif
  format: null
  id: resource_0ea7aeaf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2020_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/USA/50_US_states_1km_2020_UNadj.zip
  format: null
  id: resource_ecf3d8bf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 50_US_states_1km_2020_UNadj.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2019 United States)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/USA/usa_ppp_2019_1km_Aggregated.tif
  format: null
  id: resource_131c37f1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2019_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2019 United States)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/USA/usa_ppp_2019_1km_ASCII_XYZ.zip
  format: null
  id: resource_4793607e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2019_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2019 United States)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/USA/50_US_states_1km_2019.zip
  format: null
  id: resource_9974d2da
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 50_US_states_1km_2019.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/USA/usa_ppp_2019_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_c49e323f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2019_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/USA/usa_ppp_2019_1km_Aggregated_UNadj.tif
  format: null
  id: resource_2133bc0d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2019_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/USA/50_US_states_1km_2019_UNadj.zip
  format: null
  id: resource_a169ffd7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 50_US_states_1km_2019_UNadj.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2018 United States)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/USA/usa_ppp_2018_1km_Aggregated.tif
  format: null
  id: resource_cbb73c4c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2018_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2018 United States)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/USA/usa_ppp_2018_1km_ASCII_XYZ.zip
  format: null
  id: resource_bb85aa8c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2018_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2018 United States)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/USA/50_US_states_1km_2018.zip
  format: null
  id: resource_0edededb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 50_US_states_1km_2018.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/USA/usa_ppp_2018_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_65477a3a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2018_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/USA/usa_ppp_2018_1km_Aggregated_UNadj.tif
  format: null
  id: resource_4b13c38a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2018_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/USA/50_US_states_1km_2018_UNadj.zip
  format: null
  id: resource_d2d6c8b5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 50_US_states_1km_2018_UNadj.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2017 United States)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/USA/usa_ppp_2017_1km_Aggregated.tif
  format: null
  id: resource_b23e9cd9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2017_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2017 United States)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/USA/usa_ppp_2017_1km_ASCII_XYZ.zip
  format: null
  id: resource_d908b286
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2017_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2017 United States)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/USA/50_US_states_1km_2017.zip
  format: null
  id: resource_e68e5adf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 50_US_states_1km_2017.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/USA/usa_ppp_2017_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_c31e3da0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2017_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/USA/usa_ppp_2017_1km_Aggregated_UNadj.tif
  format: null
  id: resource_8e0bb11c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2017_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/USA/50_US_states_1km_2017_UNadj.zip
  format: null
  id: resource_cff15982
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 50_US_states_1km_2017_UNadj.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2016 United States)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/USA/usa_ppp_2016_1km_Aggregated.tif
  format: null
  id: resource_cbfccc99
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2016_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2016 United States)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/USA/usa_ppp_2016_1km_ASCII_XYZ.zip
  format: null
  id: resource_c1018fe6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2016_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America - Population Counts (The spatial distribution
    of population in 2016 United States)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/USA/50_US_states_1km_2016.zip
  format: null
  id: resource_cdf5b03e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 50_US_states_1km_2016.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/USA/usa_ppp_2016_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_1ecae4de
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2016_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/USA/usa_ppp_2016_1km_Aggregated_UNadj.tif
  format: null
  id: resource_9c1469bd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_ppp_2016_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, United States
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/USA/50_US_states_1km_2016_UNadj.zip
  format: null
  id: resource_f1047099
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 50_US_states_1km_2016_UNadj.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-usa_worldpop_americapopulationcounts_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - USA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: United States of America - Population Counts
version: null
vulnerability: null
---
