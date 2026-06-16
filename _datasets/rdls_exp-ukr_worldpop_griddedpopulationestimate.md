---
attributions:
- entity:
    affiliation: null
    email: null
    name: German Remote Sensing Data Center (DFD), German Aerospace Center (DLR)
    url: https://data.humdata.org/dataset/gridded-population-estimates-for-ukraine-using-un-cod-ps-estimates-2020-version-2-0
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/gridded-population-estimates-for-ukraine-using-un-cod-ps-estimates-2020-version-2-0
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/gridded-population-estimates-for-ukraine-using-un-cod-ps-estimates-2020-version-2-0
dataset_id: rdls_exp-ukr_worldpop_griddedpopulationestimate
description: 'These data were produced by WorldPop at the University of Southampton
  and the ''Smart Cities and Spatial Development'' team at the German Remote Sensing
  Data Center (DFD) of the German Aerospace Center (DLR). These data include gridded
  estimates of population at approximately 100m and 1km resolution for 2020, along
  with estimates of the number of people belonging to individual age-gender groups.
  These results were produced using subnational population estimates for Ukraine in
  2020 provided in the Common Operational Dataset on Population Statistics ( COD-PS
  ) and building height/area/fraction/volume covariates extracted from the World Settlement
  Footprint (WSF) imperviousness and WSF-3D by DLR . The constrained top-down disaggregation
  method was used to produce the datasets. The modelling work and geospatial data
  processing was led by Bondarenko M., Palacios-Lopez D., Sorichetta A., Leasure D.R.,
  ,Zeidler J., Marconcini M., and Esch T.. Oversight was provided by Tatem A.J. Internal
  WorldPop peer reviews that helped to improve the results and documentation was provided
  by Lazar A.N.. Main data sources The German Aerospace Centre''s (DLR) WSF imperviousness
  and WSF 3D products (WSF-3D). Subnational population estimates for Ukraine in 2020
  provided in the Common Operational Dataset on Population Statistics (COD-PS). The
  subnational population estimates were produced using baseline information from the
  2001 Population Census of Ukraine and annual birth and death registration data since
  then. Subnational Administrative Boundaries for Ukraine provided by OCHA . Geospatial
  covariate layers available at WorldPop. For further details, please, read the Release
  Statement . Release content ukr_pop_2020_100m_constrained_v2.zip ukr_pop_2020_1km_constrained_v2.zip
  ukr_agegender_2020_100m_constrained_v2.zip ukr_agegender_2020_1km_constrained_v2.zip
  ukr_agegender_0_18_2020_100m_constrained_v2.zip ukr_agegender_0_18_2020_1km_constrained_v2.zip
  Recommended citations Bondarenko M., Palacios-Lopez D., Sorichetta A., Leasure D.R.,
  Zeidler J., Marconcini, M., Esch T., and Tatem A.J. 2022 Gridded population estimates
  for Ukraine using UN COD-PS estimates 2020, version 2.0 . WorldPop and DLR, University
  of Southampton. doi:10.5258/SOTON/WP00735 License These data may be distributed
  using a Creative Commons Attribution 4.0 International (CC BY 4.0) License, specified
  in legal code. Contact release[at]worldpop.org for more information . The authors
  followed rigorous procedures designed to ensure that the used data, the applied
  method and thus the results are appropriate and of reasonable quality. If users
  encounter apparent errors or misstatements, they should contact WorldPop at release[at]worldpop.org.
  WorldPop , University of Southampton, and their sponsors offer these data on a ''where
  is, as is'' basis; do not offer an express or implied warranty of any kind; do not
  guarantee the quality, applicability, accuracy, reliability or completeness of any
  data provided; and shall not be liable for incidental, consequential, or special
  damages arising out of the use of any data that they offer.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/gridded-population-estimates-for-ukraine-using-un-cod-ps-estimates-2020-version-2-0]'
details: null
exposure:
- asset_type:
    description: Gridded population estimates at 100m and 1km resolution for Ukraine
      in 2020, including age-gender disaggregation and children (0-18 years)
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
  description: Gridded population estimates were produced by WorldPop and DLR using
    subnational population estimates for Ukraine in 2020 from the Common Operational
    Database (COD-PS). Census-based population data were spatially disaggregated to
    100m and 1km resolution grids using constrained modeling techniques, with additional
    stratification by age-gender groups and children (0-18 years).
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: German Remote Sensing Data Center (DFD), German Aerospace Center (DLR)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/gridded-population-estimates-for-ukraine-using-un-cod-ps-estimates-2020-version-2-0
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This README file provides information about the data included in the
    data release, how it was produced, source data that were used.
  download_url: https://data.worldpop.org/repo/wopr/UKR/v2/constrained/UKR_population_v2_0_README.pdf
  format: null
  id: resource_24092adf
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UKR_population_v2_0_README.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This geotiff raster, at a spatial resolution of 3 arc-seconds (approximately
    100m at the equator), contains estimates of total population size per grid cell
    across Ukraine. NA values represent areas that were mapped as unsettled based
    on the DLR settlement layer ]. These data are stored as floating-point numbers
    rather than integers to avoid rounding errors in aggregated populations for larger
    areas.
  download_url: https://data.worldpop.org/repo/wopr/UKR/v2/constrained/100m/ukr_population_2020_100m_constrained_v2.zip
  format: null
  id: resource_4f73c380
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_pop_2020_100m_constrained_v2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 34 raster files in geotiff format at a spatial
    resolution of 3 arc-seconds (approximately 100m at the equator). Each raster provides
    gridded population estimates for an age-gender group of settled areas (NA represent
    unsettled areas). Files are labelled with either an 'M' (male) or an 'F' (female)
    followed by the age-range of the group (five year bins). For instance, 'F_00_04'
    and 'M_05_09' are population counts of under 5 year olds for females and between
    5 and 9 years old for males, respectively. Eighty year olds and over are represented
    in the groups 'F_80Plus' and 'M_80Plus'. These data were produced using age-gender
    national proportions from COD-PS . The age-gender proportions were applied to
    the gridded population estimates (ukr_pop_2020_100m_constrained_v2) to allocate
    the population to the different age-gender classes. While this data represents
    population counts, values contain decimals, i.e. fractions of people. This is
    because we do not estimate which grid cell each individual in a given age group
    occupies. For this reason, it is advised to aggregate the rasters at a coarser
    scale. For example, if four grid cells next to each other have values of 0.25
    this indicates that there is 1 person of that age group somewhere in those four
    grid cells.
  download_url: https://data.worldpop.org/repo/wopr/UKR/v2/constrained/100m/ukr_agesex_2020_100m_constrained_v2.zip
  format: null
  id: resource_cb635260
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_agegender_2020_100m_constrained_v2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 3 rasters in geotiff format at a spatial resolution
    of 3 arc-seconds (approximately 100m at the equator). Each raster provides gridded
    population estimates for children-age (0 to 18 years old) of settled areas (NA
    represent unsettled areas). Files are labelled with either an 'M' (male) or an
    'F' (female) or 'F_M' for both male and female. These data were created by applying
    the Sprague multipliers to 'ukr_agegender_2020_100m_constrained_v2 ' raster data.
    Sprague multipliers are used to interpolate data and obtain population estimates
    by single years of age and these are then aggregated to 0 to 18 years of age.
  download_url: https://data.worldpop.org/repo/wopr/UKR/v2/constrained/100m/ukr_agesex_0_18_2020_100m_constrained_v2.zip
  format: null
  id: resource_411a57d2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_agegender_0_18_2020_100m_constrained_v2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This geotiff raster, at a spatial resolution of 30 arc-seconds (approximately
    1km at the equator), contains estimates of total population size per grid cell
    across Ukraine. NA values represent areas that were mapped as unsettled based
    on the DLR settlement layer . The dataset was produced by aggregating the ukr_pop_2020_100m_constrained_v2.tif
    dataset to 1km.
  download_url: https://data.worldpop.org/repo/wopr/UKR/v2/constrained/1km/ukr_population_2020_1km_constrained_v2.zip
  format: null
  id: resource_2438a193
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_population_2020_1km_constrained_v2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 34 rasters in geotiff format at a spatial resolution
    of 30 arc-seconds (approximately 1km at the equator). Each raster provides gridded
    population estimates for an age-gender group of settled areas (NA represent unsettled
    areas). These datasets were produced by aggregating the ukr_agegender_2020_100m_constrained_v2
    datasets respectively to 1km.
  download_url: https://data.worldpop.org/repo/wopr/UKR/v2/constrained/1km/ukr_agesex_2020_1km_constrained_v2.zip
  format: null
  id: resource_3a33ea06
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_agegender_2020_1km_constrained_v2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 3 rasters in geotiff format at a spatial resolution
    of 30 arc-seconds (approximately 1km at the equator). Each raster provides gridded
    population estimates for children-age (0 to 18 years old) of settled areas (NA
    represent unsettled areas). Files are labelled with either an 'M' (male) or an
    'F' (female) or 'F_M' for both male and female. These data were created by applying
    Sprague multipliers to 'ukr_agegender_2020_1km_constrained_v2 ' raster data. The
    Sprague multipliers are used to interpolate data and obtain population estimates
    by single years of age and these are then aggregated to 0 to 18 years of age.
  download_url: https://data.worldpop.org/repo/wopr/UKR/v2/constrained/1km/ukr_agesex_0_18_2020_1km_constrained_v2.zip
  format: null
  id: resource_8e1d7582
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_agegender_0_18_2020_1km_constrained_v2.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ukr_worldpop_griddedpopulationestimate
spatial:
  bbox: null
  centroid: null
  countries:
  - UKR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Gridded population estimates for Ukraine using UN COD-PS estimates 2020, version
  2.0
version: null
vulnerability: null
---
