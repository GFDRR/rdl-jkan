---
attributions:
- entity:
    affiliation: null
    email: null
    name: Common Operational Dataset on Population Statistics (COD-PS)
    url: https://data.humdata.org/dataset/gridded-population-estimates-for-sudan-using-un-cod-ps-estimates-2022-v2
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Global Human Settlement Layer (GHSL)
    url: https://data.humdata.org/dataset/gridded-population-estimates-for-sudan-using-un-cod-ps-estimates-2022-v2
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/gridded-population-estimates-for-sudan-using-un-cod-ps-estimates-2022-v2
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/gridded-population-estimates-for-sudan-using-un-cod-ps-estimates-2022-v2
dataset_id: rdls_exp-sdn_worldpop_griddedpopulationestimate
description: 'These data were produced by WorldPop at the University of Southampton.
  These data include gridded estimates of population at approximately 100m and 1km
  for 2022, along with estimates of the number of people belonging to individual age-gender
  groups. These results were produced using subnational population estimates for Sudan
  in 2022 provided in the Common Operational Dataset on Population Statistics ( COD-PS
  ) and built-up surfaces/volumes covariates extracted from GHSL datasets ; GHS-BUILT-Surface
  epoch 2020 layer , combined with Digitize Africa building footprints , were used
  to delineate settled areas. The constrained and unconstrained top-down disaggregation
  method was used to produce the datasets, i.e. population was only estimated within
  areas classified as containing built settlement. The modelling work and geospatial
  data processing was led by Bondarenko M. and Leasure D.R.. Oversight was provided
  by Tatem A.J. For further details, please, read the Release Statement . Recommended
  citations Bondarenko M., Leasure D.R., and Tatem A.J. 2023 Gridded population estimates
  for Sudan using UN COD-PS estimates 2022, version 2.0. WorldPop, University of Southampton.
  doi:10.5258/SOTON/WP00761 License These data may be distributed using a Creative
  Commons Attribution 4.0 International (CC BY 4.0) License, specified in legal code.
  Contact release@worldpop.org for more information. The authors followed rigorous
  procedures designed to ensure that the used data, the applied method and thus the
  results are appropriate and of reasonable quality. If users encounter apparent errors
  or misstatements, they should contact WorldPop at release@worldpop.org. WorldPop,
  University of Southampton, and their sponsors offer these data on a ''where is,
  as is'' basis; do not offer an express or implied warranty of any kind; do not guarantee
  the quality, applicability, accuracy, reliability or completeness of any data provided;
  and shall not be liable for incidental, consequential, or special damages arising
  out of the use of any data that they offer.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/gridded-population-estimates-for-sudan-using-un-cod-ps-estimates-2022-v2]'
details: CITATION Bondarenko M., Leasure D.R., and Tatem A.J. 2023 Gridded population
  estimates for Sudan using UN COD-PS estimates 2022, version 2.0. WorldPop, University
  of Southampton. doi:10.5258/SOTON/WP00761
exposure:
- asset_type:
    description: Gridded population estimates for Sudan at 100m and 1km resolution,
      including age-gender disaggregation and school-age population
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
  description: Subnational population estimates from COD-PS for Sudan 2022 were spatially
    disaggregated using WorldPop's dasymetric mapping methodology, with built-up area
    and volume covariates from GHSL datasets as spatial predictors, to produce gridded
    population estimates at 100m and 1km resolution with age-gender and school-age
    breakdowns.
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
- href: https://data.humdata.org/dataset/gridded-population-estimates-for-sudan-using-un-cod-ps-estimates-2022-v2
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
  url: https://data.humdata.org/dataset/cod-ps-sdn
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://ghsl.jrc.ec.europa.eu/download.php
- author_names: null
  date_published: null
  doi: null
  id: reference_3
  name: Methodology documentation
  url: http://digitizeafrica.ai/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This README file provides information about the data included in the
    data release, how it was produced, source data that were used.
  download_url: https://data.worldpop.org/repo/wopr/SDN/population/v2/SDN_population_v2_0_README.pdf
  format: null
  id: resource_ec0b359d
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_population_v2_0_README.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This geotiff raster, at a spatial resolution of 3 arc-seconds (approximately
    100m at the equator), contains estimates of total population size per grid cell
    across Sudan. NA values represent areas that were mapped as unsettled based on
    the GHSL settlement layer and Digitize Africa building footprints . These data
    are stored as floating-point numbers rather than integers to avoid rounding errors
    in aggregated populations for larger areas.
  download_url: https://data.worldpop.org/repo/wopr/SDN/population/v2/constrained/100m/sdn_population_2022_100m_constrained_v2.zip
  format: null
  id: resource_f63e89ac
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sdn_population_2022_100m_constrained_v2.zip
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
    the gridded population estimates (sdn_pop_2022_100m_constrained_v1) to allocate
    the population to the different age-gender classes. While this data represents
    population counts, values contain decimals, i.e. fractions of people. This is
    because we do not estimate which grid cell each individual in a given age group
    occupies and are maintaining the UN COD-PS numbers. For this reason, it is advised
    to aggregate the rasters at a coarser scale. For example, if four grid cells next
    to each other have values of 0.25 this indicates that there is estimated to be
    1 person of that age group somewhere in those four grid cells.
  download_url: https://data.worldpop.org/repo/wopr/SDN/population/v2/constrained/100m/sdn_agesex_2022_100m_constrained_v2.zip
  format: null
  id: resource_069876d5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sdn_agegender_2022_100m_constrained_v2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This geotiff raster, at a spatial resolution of 30 arc-seconds (approximately
    1km at the equator), contains estimates of total population size per grid cell
    across Sudan. NA values represent areas that were mapped as unsettled based on
    the GHSL settlement layer. The dataset was produced by aggregating sdn_population_2022_100m_constrained_v1.tif
    dataset to 1km.
  download_url: https://data.worldpop.org/repo/wopr/SDN/population/v2/constrained/1km/sdn_population_2022_1km_constrained_v2.zip
  format: null
  id: resource_95e6cacd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sdn_population_2022_1km_constrained_v2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains rasters in geotiff format at a spatial resolution
    of 30 arc-seconds (approximately 1km at the equator). Each raster provides gridded
    population estimates for an age-gender group of settled areas (NA represent unsettled
    areas). These datasets were produced by aggregating sdn_agegender_2022_100m_constrained_v1_0
    datasets respectively to 1km.
  download_url: https://data.worldpop.org/repo/wopr/SDN/population/v2/constrained/1km/sdn_agesex_2022_1km_constrained_v2.zip
  format: null
  id: resource_28028b48
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sdn_agegender_2022_1km_constrained_v2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains rasters in geotiff format at a spatial resolution
    of 30 arc-seconds (approximately 1km at the equator). Each raster provides gridded
    population estimates for children, broken down in differing school attendance
    age groupings (0 to 5 years old, 0 to 17 years old, 6 to 13 years old and 14 to
    17 years old) for settled areas (NA represent unsettled areas). Files are labelled
    with either an 'M' (male) or an 'F' (female) or 'F_M' for both male and female.
    These data were created by applying Sprague multipliers to 'sdn_agegender_2022_1km_constrained_v2
    ' raster data. Sprague multipliers are used to interpolate data and obtain population
    estimates by single years of age and these are then aggregated to obtain differing
    age groupings.
  download_url: https://data.worldpop.org/repo/wopr/SDN/population/v2/constrained/1km/sdn_school_age_2022_1km_constrained_v2.zip
  format: null
  id: resource_10243d1d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sdn_school_age_2022_1km_constrained_v2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This zip file contains the zonal statistics calculated using ''sdn_school_age_2022_1km_constrained_v2
    '' and level 2 of Subnational Administrative Boundaries for Sudan provided by
    OCHA on HDX: https://data.humdata.org/dataset/cod-ab-sdn'
  download_url: https://data.worldpop.org/repo/wopr/SDN/population/v2/constrained/csv/sdn_school_age_adm2_2022.zip
  format: null
  id: resource_d3f18b0c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sdn_school_age_adm2_2022.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This zip file contains the zonal statistics of total population calculated
    using ''sdn_agegender_2022_100m_constrained_v2'' and level 2 of Subnational Administrative
    Boundaries for Sudan provided by OCHA on HDX: https://data.humdata.org/dataset/cod-ab-sdn'
  download_url: https://data.worldpop.org/repo/wopr/SDN/population/v2/constrained/csv/sdn_pop_adm2_2022.zip
  format: null
  id: resource_25114237
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sdn_pop_adm2_2022.zip
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
    the gridded population estimates (sdn_pop_2022_100m_uconstrained_v1) to allocate
    the population to the different age-gender classes. While this data represents
    population counts, values contain decimals, i.e. fractions of people. This is
    because we do not estimate which grid cell each individual in a given age group
    occupies. For this reason, it is advised to aggregate the rasters at a coarser
    scale. For example, if four grid cells next to each other have values of 0.25
    this indicates that there is 1 person of that age group somewhere in those four
    grid cells.
  download_url: https://data.worldpop.org/repo/wopr/SDN/population/v2/unconstrained/100m/sdn_agesex_2022_100m_unconstrained_v2.zip
  format: null
  id: resource_760ad53c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sdn_agegender_2022_100m_unconstrained_v2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This geotiff raster, at a spatial resolution of 3 arc-seconds (approximately
    100m at the equator), contains estimates of total population size per grid cell
    across Sudan. NA values represent areas that were mapped as water. These data
    are stored as floating-point numbers rather than integers to avoid rounding errors
    in aggregated populations for larger areas.
  download_url: https://data.worldpop.org/repo/wopr/SDN/population/v2/unconstrained/100m/sdn_population_2022_100m_unconstrained_v2.zip
  format: null
  id: resource_332d937b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sdn_population_2022_100m_unconstrained_v2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains raster files in geotiff format at a spatial
    resolution of 30 arc-seconds (approximately 1km at the equator). Each raster provides
    gridded population estimates for an age-gender group of settled areas (NA represent
    surface waters). Files are labelled with either an 'M' (male) or an 'F' (female)
    followed by the age-range of the group (five year bins). For instance, 'F_00_04'
    and 'M_05_09' are population counts of under 5 year olds for females and between
    5 and 9 years old for males, respectively. Eighty year olds and over are represented
    in the groups 'F_80Plus' and 'M_80Plus'. These data were produced using age-gender
    national proportions from COD-PS . The age-gender proportions were applied to
    the gridded population estimates (sdn_pop_2022_1km_uconstrained_v1) to allocate
    the population to the different age-gender classes. While this data represents
    population counts, values contain decimals, i.e. fractions of people. This is
    because we do not estimate which grid cell each individual in a given age group
    occupies. For this reason, it is advised to aggregate the rasters at a coarser
    scale. For example, if four grid cells next to each other have values of 0.25
    this indicates that there is 1 person of that age group somewhere in those four
    grid cells.
  download_url: https://data.worldpop.org/repo/wopr/SDN/population/v2/unconstrained/1km/sdn_agesex_2022_1km_unconstrained_v2.zip
  format: null
  id: resource_67c88931
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sdn_agegender_2022_1km_unconstrained_v2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This geotiff raster, at a spatial resolution of 30 arc-seconds (approximately
    1km at the equator), contains estimates of total population size per grid cell
    across Sudan. NA values represent areas that were mapped as water. The dataset
    was produced by aggregating sdn_pop_2022_100m_unconstrained_v1_0.tif dataset to
    1km.
  download_url: https://data.worldpop.org/repo/wopr/SDN/population/v2/unconstrained/1km/sdn_population_2022_1km_unconstrained_v2.zip
  format: null
  id: resource_fb20bcd0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sdn_population_2022_1km_unconstrained_v2.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-sdn_worldpop_griddedpopulationestimate
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Gridded population estimates for Sudan using UN COD-PS estimates 2022, version
  2.0
version: null
vulnerability: null
---
