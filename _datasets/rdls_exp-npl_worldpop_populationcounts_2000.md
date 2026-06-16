---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-nepal
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-nepal
dataset_id: rdls_exp-npl_worldpop_populationcounts_2000
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-for-nepal]'
details: null
exposure:
- asset_type:
    description: Gridded population counts at 100m resolution for Nepal, adjusted
      to official census totals
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
license: CC-BY-4.0
lineage:
  description: WorldPop produced gridded population estimates for Nepal by integrating
    census data with geospatial covariates using country-specific methods, generating
    100m resolution rasters adjusted to match official population totals and available
    in multiple variants (UN-adjusted, constrained, aggregated to 1km).
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/worldpop-population-counts-for-nepal
  rel: source
loss: null
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
  description: Nepal - Population Counts (The spatial distribution of population in
    2020, Nepal)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/NPL/npl_ppp_2020.tif
  format: null
  id: resource_d7d9fcbf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Population Counts (The spatial distribution of population in
    2019, Nepal)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/NPL/npl_ppp_2019.tif
  format: null
  id: resource_dd02166d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Population Counts (The spatial distribution of population in
    2018, Nepal)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/NPL/npl_ppp_2018.tif
  format: null
  id: resource_db118c08
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Population Counts (The spatial distribution of population in
    2017, Nepal)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/NPL/npl_ppp_2017.tif
  format: null
  id: resource_a77a4de0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Population Counts (The spatial distribution of population in
    2016, Nepal)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/NPL/npl_ppp_2016.tif
  format: null
  id: resource_a772dd5a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Nepal
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/NPL/npl_ppp_2020_UNadj.tif
  format: null
  id: resource_9bd9b093
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2020_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Nepal
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/NPL/npl_ppp_2019_UNadj.tif
  format: null
  id: resource_5a656fbf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2019_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Nepal
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/NPL/npl_ppp_2018_UNadj.tif
  format: null
  id: resource_87c0cd0f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2018_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Nepal
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/NPL/npl_ppp_2017_UNadj.tif
  format: null
  id: resource_8f31d9a8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2017_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Nepal
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/NPL/npl_ppp_2016_UNadj.tif
  format: null
  id: resource_b6f93a21
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2016_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Population Counts (The spatial distribution of population in
    2020, Nepal)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/BSGM/NPL/npl_ppp_2020_constrained.tif
  format: null
  id: resource_ed3830c3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2020_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Nepal
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/BSGM/NPL/npl_ppp_2020_UNadj_constrained.tif
  format: null
  id: resource_e12166e3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2020_UNadj_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Population Counts (The spatial distribution of population in
    2020 Nepal)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/NPL/npl_ppp_2020_1km_Aggregated.tif
  format: null
  id: resource_c0e4d597
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2020_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Population Counts (The spatial distribution of population in
    2020 Nepal)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/NPL/npl_ppp_2020_1km_ASCII_XYZ.zip
  format: null
  id: resource_a9008a42
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2020_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Nepal
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/NPL/npl_ppp_2020_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_bb3d4a27
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2020_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Nepal
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/NPL/npl_ppp_2020_1km_Aggregated_UNadj.tif
  format: null
  id: resource_bc95f3bb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2020_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Population Counts (The spatial distribution of population in
    2019 Nepal)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/NPL/npl_ppp_2019_1km_Aggregated.tif
  format: null
  id: resource_2dd443a9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2019_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Population Counts (The spatial distribution of population in
    2019 Nepal)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/NPL/npl_ppp_2019_1km_ASCII_XYZ.zip
  format: null
  id: resource_e4f834a1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2019_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Nepal
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/NPL/npl_ppp_2019_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_8141b37c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2019_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Nepal
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/NPL/npl_ppp_2019_1km_Aggregated_UNadj.tif
  format: null
  id: resource_f5f4474a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2019_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Population Counts (The spatial distribution of population in
    2018 Nepal)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/NPL/npl_ppp_2018_1km_Aggregated.tif
  format: null
  id: resource_e915ea19
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2018_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Population Counts (The spatial distribution of population in
    2018 Nepal)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/NPL/npl_ppp_2018_1km_ASCII_XYZ.zip
  format: null
  id: resource_459bb7a3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2018_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Nepal
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/NPL/npl_ppp_2018_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_873877bb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2018_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Nepal
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/NPL/npl_ppp_2018_1km_Aggregated_UNadj.tif
  format: null
  id: resource_72f47a93
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2018_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Population Counts (The spatial distribution of population in
    2017 Nepal)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/NPL/npl_ppp_2017_1km_Aggregated.tif
  format: null
  id: resource_5b8b9fc9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2017_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Population Counts (The spatial distribution of population in
    2017 Nepal)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/NPL/npl_ppp_2017_1km_ASCII_XYZ.zip
  format: null
  id: resource_a70136a0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2017_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Nepal
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/NPL/npl_ppp_2017_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_793e8257
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2017_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Nepal
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/NPL/npl_ppp_2017_1km_Aggregated_UNadj.tif
  format: null
  id: resource_46bd5b33
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2017_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Population Counts (The spatial distribution of population in
    2016 Nepal)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/NPL/npl_ppp_2016_1km_Aggregated.tif
  format: null
  id: resource_7a9bdff6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2016_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Population Counts (The spatial distribution of population in
    2016 Nepal)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/NPL/npl_ppp_2016_1km_ASCII_XYZ.zip
  format: null
  id: resource_28b81c46
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2016_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Nepal
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/NPL/npl_ppp_2016_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_1fc84568
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2016_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Nepal
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/NPL/npl_ppp_2016_1km_Aggregated_UNadj.tif
  format: null
  id: resource_88590b4a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_ppp_2016_1km_Aggregated_UNadj.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-npl_worldpop_populationcounts_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Nepal - Population Counts
version: null
vulnerability: null
---
