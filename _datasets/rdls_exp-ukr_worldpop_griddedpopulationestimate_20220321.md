---
attributions:
- entity:
    affiliation: null
    email: null
    name: Common Operational Dataset on Population Statistics (COD-PS)
    url: https://data.humdata.org/dataset/gridded-population-estimates-for-ukraine-using-un-cod-ps-estimates-2020-version-1-0
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: LandScan
    url: https://data.humdata.org/dataset/gridded-population-estimates-for-ukraine-using-un-cod-ps-estimates-2020-version-1-0
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/gridded-population-estimates-for-ukraine-using-un-cod-ps-estimates-2020-version-1-0
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/gridded-population-estimates-for-ukraine-using-un-cod-ps-estimates-2020-version-1-0
dataset_id: rdls_exp-ukr_worldpop_griddedpopulationestimate_20220321
description: 'These data were produced by the WorldPop Research Group at the University
  of Southampton. These data include gridded estimates of population at approximately
  100m and 1km resolution for 2020, along with estimates of the number of people belonging
  to individual age-gender groups. These results were produced using Subnational Population
  Statistics 2020 for Ukraine provided in the Common Operational Dataset on Population
  Statistics (COD-PS) and ORNL LandScan HD for Ukraine 2022 settlement layer. The
  datasets are produced using the '' top-down '' method, with both the unconstrained
  and constrained top-down disaggregation methods used to produce two different datasets.
  The differences between constrained and un-constrained methods are described here
  . Main data sources Subnational Population Statistics for Ukraine provided by Common
  Operational Dataset on Population Statistics (COD-PS). The subnational population
  statistics were estimated using baseline information from the 2001 Population Census
  of Ukraine and annual birth and death registration data since the last census. Settlement
  layer ORNL LandScan HD for Ukraine. Subnational Administrative Boundaries for Ukraine
  provided by OCHA. Geospatial covariate layers available at WorldPop. For further
  details, please, read the Release Statement . Release content ukr_pop_2020_100m_unconstrained_v1_0.zip
  ukr_pop_2020_100m_constrained_v1_0.zip ukr_pop_2020_1km_unconstrained_v1_0.zip ukr_pop_2020_1km_constrained_v1_0.zip
  ukr_agegender_2020_100m_unconstrained_v1_0.zip ukr_agegender_2020_100m_constrained_v1_0.zip
  ukr_agegender_2020_1km_unconstrained_v1_0.zip ukr_agegender_2020_1km_constrained_v1_0.zip
  ukr_agegender_0_18_2020_1km_unconstrained_v1_0.zip ukr_agegender_0_18_2020_1km_constrained_v1_0.zip
  Recommended citations Bondarenko M., Sorichetta A., Leasure DR. and Tatem AJ. 2022
  Gridded population estimates for Ukraine using UN COD-PS estimates 2020, version
  1.0 . WorldPop, University of Southampton. doi:10.5258/SOTON/WP00734 License These
  data may be distributed using a Creative Commons Attribution 4.0 International (CC
  BY 4.0) License, specified in legal code. Contact release[at]worldpop.org for more
  information . The authors followed rigorous procedures designed to ensure that the
  used data, the applied method and thus the results are appropriate and of reasonable
  quality. If users encounter apparent errors or misstatements, they should contact
  WorldPop at release[at]worldpop.org. WorldPop , University of Southampton, and their
  sponsors offer these data on a ''where is, as is'' basis; do not offer an express
  or implied warranty of any kind; do not guarantee the quality, applicability, accuracy,
  reliability or completeness of any data provided; and shall not be liable for incidental,
  consequential, or special damages arising out of the use of any data that they offer..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/gridded-population-estimates-for-ukraine-using-un-cod-ps-estimates-2020-version-1-0]'
details: Bondarenko M., Sorichetta A., Leasure DR. and Tatem AJ. 2022 Gridded population
  estimates for Ukraine using UN COD-PS estimates 2020, version 1.0. WorldPop, University
  of Southampton. doi:10.5258/SOTON/WP00734
exposure:
- asset_type:
    description: Gridded population estimates for Ukraine at 100m and 1km resolution
      disaggregated by age and gender groups for 2020
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
  description: Gridded population estimates were produced by WorldPop using subnational
    population statistics from COD-PS 2020 and LandScan ancillary data, spatially
    disaggregated to 100m and 1km resolution grids using constrained and unconstrained
    modeling approaches, with age-gender stratification derived from demographic composition
    data.
  sources:
  - id: source_1
    license: null
    name: Common Operational Dataset on Population Statistics (COD-PS)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: LandScan
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/gridded-population-estimates-for-ukraine-using-un-cod-ps-estimates-2020-version-1-0
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
  download_url: https://data.worldpop.org/repo/wopr/UKR/v1/UKR_population_v1_0_README.pdf
  format: null
  id: resource_f02494fe
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UKR_population_v1_0_README.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This geotiff raster, at a spatial resolution of 3 arc-seconds (approximately
    100m at the equator), contains estimates of total population size per grid cell
    across Ukraine using Subnational Population Statistics 2020 for Ukraine provided
    by Common Operational Dataset on Population Statistics (COD-PS). NA values represent
    areas that were mapped as unsettled based on settlement layer ORNL LandScan HD
    for Ukraine. These data are stored as floating-point numbers rather than integers
    to avoid rounding errors in aggregated populations for larger areas. For further
    details, please, read a Release Statement .
  download_url: https://data.worldpop.org/repo/wopr/UKR/v1/constrained/100m/ukr_population_2020_100m_constrained_v1_0.zip
  format: null
  id: resource_cad71beb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_population_2020_100m_constrained_v1_0.zip
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
    national proportions from COD-PS. The age-gender proportions were applied to the
    gridded population estimates (ukr_pop_2020_100m_constrained_v1_0) to allocate
    the population to the different age-gender classes. While this data represents
    population counts, values contain decimals, i.e. fractions of 3 people. This is
    because we do not estimate which grid cell each individual in a given age group
    occupies. For this reason, it is advised to aggregate the rasters at a coarser
    scale. For example, if four grid cells next to each other have values of 0.25
    this indicates that there is 1 person of that age group somewhere in those four
    grid cells. For further details, please, read a Release Statement .
  download_url: https://data.worldpop.org/repo/wopr/UKR/v1/constrained/100m/ukr_agesex_2020_100m_constrained_v1_0.zip
  format: null
  id: resource_832de3ec
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_agegender_2020_100m_constrained_v1_0.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This geotiff raster, at a spatial resolution of 30 arc-seconds (approximately
    1km at the equator), contains estimates of total population size per grid cell
    across Ukraine. NA values represent areas that were mapped as water. The dataset
    was produced by aggregating kr_pop_2020_100m_unconstrained_v1_0.tif dataset to
    1km. For further details, please, read a Release Statement .
  download_url: https://data.worldpop.org/repo/wopr/UKR/v1/constrained/1km/ukr_population_2020_1km_constrained_v1_0.zip
  format: null
  id: resource_f992886f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_population_2020_1km_constrained_v1_0.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 34 rasters in geotiff format at a spatial resolution
    of 30 arc-seconds (approximately 1km at the equator). Each raster provides gridded
    population estimates for an age-gender group of settled areas (NA represent unsettled
    areas). These datasets were produced by aggregating ukr_agegender_2020_100m_constrained_v1_0
    datasets respectively to 1km. For further details, please, read a Release Statement
    .
  download_url: https://data.worldpop.org/repo/wopr/UKR/v1/constrained/1km/ukr_agesex_2020_1km_constrained_v1_0.zip
  format: null
  id: resource_f74389e0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_agegender_2020_1km_constrained_v1_0.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 3 rasters in geotiff format at a spatial resolution
    of 30 arc-seconds (approximately 1km at the equator). Each raster provides gridded
    population estimates for children-age (0 to 18 years old) across Ukraine (NA represent
    surface waters). Files are labelled with either an 'M' (male) or an 'F' (female)
    or 'F_M' for both male and female. These data were created by applying the Sprague
    multipliers to 'ukr_agegender_2020_1km_constrained ' raster data. The Sprague
    multiplier is used to interpolate five-year binned data and obtain population
    estimates by single years that areand then aggregated to 0 to 18 years of age.
    For further details, please, read a Release Statement .
  download_url: https://data.worldpop.org/repo/wopr/UKR/v1/constrained/1km/ukr_agesex_0_18_2020_1km_constrained_v1_0.zip
  format: null
  id: resource_5abe0184
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_agegender_0_18_2020_1km_constrained_v1_0.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This geotiff raster, at a spatial resolution of 30 arc-seconds (approximately
    1km at the equator), contains estimates of total population size per grid cell
    across Ukraine. NA values represent areas that were mapped as water. The dataset
    was produced by aggregating ukr_pop_2020_100m_unconstrained_v1_0.tif dataset to
    1km. For further details, please, read a Release Statement .
  download_url: https://data.worldpop.org/repo/wopr/UKR/v1/unconstrained/1km/ukr_population_2020_1km_unconstrained_v1_0.zip
  format: null
  id: resource_2a1ef2b4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_population_2020_1km_unconstrained_v1_0.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 34 raster files in geotiff format at a spatial
    resolution of 30 arc-seconds (approximately 1km at the equator). Each raster provides
    gridded population estimates for an age-gender group across Ukraine (NA represent
    surface waters). These datasets were produced by aggregating ukr_agegender_2020_100m_unconstrained_v1_0
    datasets respectively to 1km. For further details, please, read a Release Statement
    .
  download_url: https://data.worldpop.org/repo/wopr/UKR/v1/unconstrained/1km/ukr_agesex_2020_1km_unconstrained_v1_0.zip
  format: null
  id: resource_0a1c13b0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_agegender_2020_1km_unconstrained_v1_0.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 3 rasters in geotiff format at a spatial resolution
    of 30 arc-seconds (approximately 1km at the equator). Each raster provides gridded
    population estimates for children-age (0 to 18 years old) across Ukraine (NA represent
    surface waters). Files are labelled with either an 'M' (male) or an 'F' (female)
    or 'F_M' for both male and female. These data were created by applying the Sprague
    multipliers to 'ukr_agegender_2020_1km_unconstrained ' raster data. The Sprague
    multiplier is used to interpolate five-year binned data and obtain population
    estimates by single years that areand then aggregated to 0 to 18 years of age.
    For further details, please, read a Release Statement .
  download_url: https://data.worldpop.org/repo/wopr/UKR/v1/unconstrained/1km/ukr_agesex_0_18_2020_1km_unconstrained_v1_0.zip
  format: null
  id: resource_fb3bc369
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_agegender_0_18_2020_1km_unconstrained_v1_0.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This geotiff raster, at a spatial resolution of 3 arc-seconds (approximately
    100m at the equator), contains estimates of total population size per grid cell
    across Ukraine. NA values represent areas that were mapped as water. These data
    are stored as floating-point numbers rather than integers to avoid rounding errors
    in aggregated populations for larger areas. For further details, please, read
    a Release Statement .
  download_url: https://data.worldpop.org/repo/wopr/UKR/v1/unconstrained/100m/ukr_population_2020_100m_unconstrained_v1_0.zip
  format: null
  id: resource_961d14da
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_population_2020_100m_unconstrained_v1_0.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This zip file contains 34 rasters in geotiff format at a spatial resolution
    of 3 arc-seconds (approximately 100m at the equator). Each raster provides gridded
    population estimates for an age-gender group across Ukraine (NA represent surface
    waters). Files are labelled with either an ''M'' (male) or an ''F'' (female) followed
    by the age-range of the group (five year bins). For instance, ''F_00_04'' and
    ''M_05_09'' are population counts of under 5 year olds for females and between
    5 and 9 years old for males, respectively. Eighty year olds and over are represented
    in the groups ''F_80Plus'' and ''M_80Plus''. These data were produced using age-gender
    national proportions from COD-PS. The age-gender proportions were applied to the
    gridded population estimates (ukr_pop_2020_100m_unconstrained_v1_0) to allocate
    the population to the different age-gender classes. While this data represents
    population counts, values contain decimals, i.e. fractions of people. This is
    because we do not estimate which grid cell each individual in a given age group
    occupies. For this reason, it is advised to aggregate the rasters at a coarser
    scale. For example, if four grid cells next to each other have values of 0.25
    this indicates that there is 1 person of that age group somewhere in those four
    grid cells. For further details, please, read a Release Statement . NOTE: File
    size is 13GB. if you would like to download a specific agegender group please
    use the following link here'
  download_url: https://data.worldpop.org/repo/wopr/UKR/v1/unconstrained/100m/ukr_agesex_2020_100m_unconstrained_v1_0.zip
  format: null
  id: resource_3abbaf71
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_agegender_2020_100m_unconstrained_v1_0.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ukr_worldpop_griddedpopulationestimate_20220321
spatial:
  bbox: null
  centroid: null
  countries:
  - UKR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-03-21'
temporal_resolution: null
title: Gridded Population Estimates for Ukraine using UN COD-PS Estimates 2020 (version
  1.0)
version: null
vulnerability: null
---
