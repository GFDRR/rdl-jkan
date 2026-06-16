---
attributions:
- entity:
    affiliation: null
    email: null
    name: Common Operational Dataset on Population Statistics (COD-PS)
    url: https://data.humdata.org/dataset/gridded-population-estimates-for-turkey-using-un-cod-ps-estimates-2021-version-1-0
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Global Human Settlement Layer (GHSL)
    url: https://data.humdata.org/dataset/gridded-population-estimates-for-turkey-using-un-cod-ps-estimates-2021-version-1-0
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/gridded-population-estimates-for-turkey-using-un-cod-ps-estimates-2021-version-1-0
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/gridded-population-estimates-for-turkey-using-un-cod-ps-estimates-2021-version-1-0
dataset_id: rdls_exp-tur_worldpop_griddedpopulationestimate_2021
description: 'These data were produced by WorldPop at the University of Southampton.
  These data include gridded estimates of population at approximately 100m for 2021,
  along with estimates of the number of people belonging to individual age-gender
  groups. These results were produced using subnational population estimates for Turkey
  in 2021 provided in the Common Operational Dataset on Population Statistics ( COD-PS
  ) and built-up surfaces/volumes/height covariates extracted from GHSL datasets .
  The constrained and unconstrained top-down disaggregation method was used to produce
  the datasets. The modelling work and geospatial data processing was led by Bondarenko
  M., Priyatikanto R., Sorichetta A. Oversight was provided by Tatem A.J. For further
  details, please, read the Release Statement . Recommended citations Bondarenko M.,
  Priyatikanto R., Sorichetta A., and Tatem A.J.. 2023 Gridded population estimates
  for Turkey using UN COD-PS estimates 2021, version 1.0 . WorldPop University of
  Southampton. doi:10.5258/SOTON/WP00758 License These data may be distributed using
  a Creative Commons Attribution 4.0 International (CC BY 4.0) License, specified
  in legal code. Contact release@worldpop.org for more information. The authors followed
  rigorous procedures designed to ensure that the used data, the applied method and
  thus the results are appropriate and of reasonable quality. If users encounter apparent
  errors or misstatements, they should contact WorldPop at release@worldpop.org. WorldPop,
  University of Southampton, and their sponsors offer these data on a ''where is,
  as is'' basis; do not offer an express or implied warranty of any kind; do not guarantee
  the quality, applicability, accuracy, reliability or completeness of any data provided;
  and shall not be liable for incidental, consequential, or special damages arising
  out of the use of any data that they offer.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/gridded-population-estimates-for-turkey-using-un-cod-ps-estimates-2021-version-1-0]'
details: '**Recommended citations** Bondarenko M., Priyatikanto R., Sorichetta A.,
  and Tatem A.J.. 2023 *Gridded population estimates for Turkey using UN COD-PS estimates
  2021, version 1.0*. WorldPop University of Southampton. doi:10.5258/SOTON/WP00758'
exposure:
- asset_type:
    description: Gridded population estimates at 100m and 1km resolution for Turkey
      in 2021, including age-gender disaggregation
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
  description: Subnational population estimates from COD-PS for Turkey in 2021 were
    spatially disaggregated to 100m and 1km grid cells using WorldPop's dasymetric
    modeling approach, with built-up area and building height covariates from GHSL
    as spatial predictors. Age-gender group estimates were produced alongside total
    population counts in both constrained and unconstrained variants.
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
    name: Global Human Settlement Layer (GHSL)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/gridded-population-estimates-for-turkey-using-un-cod-ps-estimates-2021-version-1-0
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
  url: https://data.humdata.org/dataset/cod-ps-tur
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This README file provides information about the data included in the
    data release, how it was produced, source data that were used.
  download_url: https://data.worldpop.org/repo/wopr/TUR/v1/TUR_population_v1_0_README.pdf
  format: null
  id: resource_f1e85a47
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TUR_population_v1_0_README.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This geotiff raster, at a spatial resolution of 3 arc-seconds (approximately
    100m at the equator), contains estimates of total population size per grid cell
    across Turkey. These results were produced using subnational population estimates
    for Turkey in 2021 provided in the Common Operational Dataset on Population Statistics
    ( COD-PS ). NA values represent areas that were mapped as unsettled based on the
    GHS settlement layer . These data are stored as floating-point numbers rather
    than integers to avoid rounding errors in aggregated populations for larger areas.
  download_url: https://data.worldpop.org/repo/wopr/TUR/v1/constrained/100m/tur_population_2021_100m_constrained_v1.zip
  format: null
  id: resource_0dee2ecc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_population_2021_100m_constrained_v1.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This geotiff raster, at a spatial resolution of 3 arc-seconds (approximately
    100m at the equator), contains estimates of total population size per grid cell
    across Turkey. NA values represent areas that were mapped as water. These data
    are stored as floating-point numbers rather than integers to avoid rounding errors
    in aggregated populations for larger areas.
  download_url: https://data.worldpop.org/repo/wopr/TUR/v1/unconstrained/100m/tur_population_2021_100m_unconstrained_v1.zip
  format: null
  id: resource_ed3f4854
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_population_2021_100m_unconstrained_v1.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This geotiff raster, at a spatial resolution of 30 arc-seconds (approximately
    1km at the equator), contains estimates of total population size per grid cell
    across Turkey. NA values represent areas that were mapped as unsettled based on
    the GHS settlement layer . The dataset was produced by aggregating tur_pop_2021_100m_constrained_v1.tif
    dataset to 1km.
  download_url: https://data.worldpop.org/repo/wopr/TUR/v1/constrained/1km/tur_population_2021_1km_constrained_v1.zip
  format: null
  id: resource_9b4c1586
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ur_population_2021_1km_constrained_v1.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This geotiff raster, at a spatial resolution of 30 arc-seconds (approximately
    1km at the equator), contains estimates of total population size per grid cell
    across Turkey. NA values represent areas that were mapped as water. The dataset
    was produced by aggregating tur_pop_2021_100m_unconstrained_v1_0.tif dataset to
    1km.
  download_url: https://data.worldpop.org/repo/wopr/TUR/v1/unconstrained/1km/tur_population_2021_1km_unconstrained_v1.zip
  format: null
  id: resource_fb7ea43d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_population_2021_1km_unconstrained_v1.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains raster files in geotiff format at a spatial
    resolution of 3 arc-seconds (approximately 100m at the equator). Each raster provides
    gridded population estimates for an age-gender group of settled areas (NA represent
    surface waters). Files are labelled with either an 'M' (male) or an 'F' (female)
    followed by the age-range of the group (five year bins). For instance, 'F_00_04'
    and 'M_05_09' are population counts of under 5 year olds for females and between
    5 and 9 years old for males, respectively. Eighty year olds and over are represented
    in the groups 'F_80Plus' and 'M_80Plus'. These data were produced using age-gender
    national proportions from COD-PS . The age-gender proportions were applied to
    the gridded population estimates (tur_pop_2021_100m_uconstrained_v1) to allocate
    the population to the different age-gender classes. While this data represents
    population counts, values contain decimals, i.e. fractions of people. This is
    because we do not estimate which grid cell each individual in a given age group
    occupies. For this reason, it is advised to aggregate the rasters at a coarser
    scale. For example, if four grid cells next to each other have values of 0.25
    this indicates that there is 1 person of that age group somewhere in those four
    grid cells.
  download_url: https://data.worldpop.org/repo/wopr/TUR/v1/unconstrained/100m/tur_agesex_2021_100m_unconstrained_v1.zip
  format: null
  id: resource_96ba149c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_agegender_2021_100m_unconstrained_v1.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains raster files in geotiff format at a spatial
    resolution of 3 arc-seconds (approximately 100m at the equator). Each raster provides
    gridded population estimates for an age-gender group of settled areas (NA represent
    unsettled areas). Files are labelled with either an 'M' (male) or an 'F' (female)
    followed by the age-range of the group (five year bins). For instance, 'F_00_04'
    and 'M_05_09' are population counts of under 5 year olds for females and between
    5 and 9 years old for males, respectively. Eighty year olds and over are represented
    in the groups 'F_80Plus' and 'M_80Plus'. These data were produced using age-gender
    national proportions from COD-PS . The age-gender proportions were applied to
    the gridded population estimates (tur_pop_2021_100m_constrained_v1) to allocate
    the population to the different age-gender classes. While this data represents
    population counts, values contain decimals, i.e. fractions of people. This is
    because we do not estimate which grid cell each individual in a given age group
    occupies. For this reason, it is advised to aggregate the rasters at a coarser
    scale. For example, if four grid cells next to each other have values of 0.25
    this indicates that there is 1 person of that age group somewhere in those four
    grid cells.
  download_url: https://data.worldpop.org/repo/wopr/TUR/v1/constrained/100m/tur_agesex_2021_100m_constrained_v1.zip
  format: null
  id: resource_20abe8b2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_agegender_2021_100m_constrained_v1.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains raster files in geotiff format at a spatial
    resolution of 30 arc-seconds (approximately 1km at the equator). Each raster provides
    gridded population estimates for an age-gender group across Turkey (NA represent
    surface waters). These datasets were produced by aggregating tur_agegender_2021_100m_uconstrained_v1
    datasets respectively to 1km.
  download_url: https://data.worldpop.org/repo/wopr/TUR/v1/unconstrained/1km/tur_agesex_2021_1km_unconstrained_v1.zip
  format: null
  id: resource_48da9104
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_agegender_2021_1km_unconstrained_v1.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains rasters in geotiff format at a spatial resolution
    of 30 arc-seconds (approximately 1km at the equator). Each raster provides gridded
    population estimates for an age-gender group of settled areas (NA represent unsettled
    areas). These datasets were produced by aggregating tur_agegender_2021_100m_constrained_v1_0
    datasets respectively to 1km.
  download_url: https://data.worldpop.org/repo/wopr/TUR/v1/constrained/1km/tur_agesex_2021_1km_constrained_v1.zip
  format: null
  id: resource_43c1cf8d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_agegender_2021_1km_constrained_v1.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-tur_worldpop_griddedpopulationestimate_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - TUR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-12-31'
  start: '2021-01-01'
temporal_resolution: null
title: Gridded population estimates for Turkey using UN COD-PS estimates 2021, version
  1.0
version: null
vulnerability: null
---
